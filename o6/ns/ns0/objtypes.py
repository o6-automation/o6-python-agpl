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
from . import vartypes as ns0_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="i=58", browseName="BaseObjectType", displayName="BaseObjectType")
class BaseObjectType(_ObjectNode):
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


@o6.objecttype(nodeId="i=61", browseName="FolderType", displayName="FolderType")
class FolderType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=75", browseName="DataTypeSystemType", displayName="DataTypeSystemType")
class DataTypeSystemType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=76", browseName="DataTypeEncodingType", displayName="DataTypeEncodingType")
class DataTypeEncodingType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=77", browseName="ModellingRuleType", displayName="ModellingRuleType")
class ModellingRuleType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=2020", browseName="ServerDiagnosticsType", displayName="ServerDiagnosticsType")
class ServerDiagnosticsType(BaseObjectType):
    enabledFlag: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2025", browseName="EnabledFlag", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1, accessLevel=3, userAccessLevel=1)
    )
    samplingIntervalDiagnosticsArray: ns0_vartypes.SamplingIntervalDiagnosticsArrayType | None = o6.hasComponent(
        ns0_vartypes.SamplingIntervalDiagnosticsArrayType(
            nodeId="i=2022",
            browseName="SamplingIntervalDiagnosticsArray",
            modellingRule="Optional",
            dataType=ns0_datypes.SamplingIntervalDiagnosticsDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    serverDiagnosticsSummary: ns0_vartypes.ServerDiagnosticsSummaryType
    sessionsDiagnosticsSummary: SessionsDiagnosticsSummaryType
    subscriptionDiagnosticsArray: ns0_vartypes.SubscriptionDiagnosticsArrayType = o6.hasComponent(
        ns0_vartypes.SubscriptionDiagnosticsArrayType(
            nodeId="i=2023",
            browseName="SubscriptionDiagnosticsArray",
            modellingRule="Mandatory",
            dataType=ns0_datypes.SubscriptionDiagnosticsDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.objecttype(nodeId="i=2026", browseName="SessionsDiagnosticsSummaryType", displayName="SessionsDiagnosticsSummaryType")
class SessionsDiagnosticsSummaryType(BaseObjectType):
    clientName_: SessionDiagnosticsObjectType | None
    sessionDiagnosticsArray: ns0_vartypes.SessionDiagnosticsArrayType = o6.hasComponent(
        ns0_vartypes.SessionDiagnosticsArrayType(
            nodeId="i=2027", browseName="SessionDiagnosticsArray", modellingRule="Mandatory", dataType=ns0_datypes.SessionDiagnosticsDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    sessionSecurityDiagnosticsArray: ns0_vartypes.SessionSecurityDiagnosticsArrayType = o6.hasComponent(
        ns0_vartypes.SessionSecurityDiagnosticsArrayType(
            nodeId="i=2028",
            browseName="SessionSecurityDiagnosticsArray",
            modellingRule="Mandatory",
            dataType=ns0_datypes.SessionSecurityDiagnosticsDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.objecttype(nodeId="i=2033", browseName="VendorServerInfoType", displayName="VendorServerInfoType")
class VendorServerInfoType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=2299", browseName="StateMachineType", displayName="StateMachineType")
class StateMachineType(BaseObjectType):
    currentState: ns0_vartypes.StateVariableType
    lastTransition: ns0_vartypes.TransitionVariableType | None


@o6.objecttype(nodeId="i=2307", browseName="StateType", displayName="StateType")
class StateType(BaseObjectType):
    stateNumber: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2308", browseName="StateNumber", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2309", browseName="InitialStateType", displayName="InitialStateType")
class InitialStateType(StateType):
    pass


@o6.objecttype(nodeId="i=2310", browseName="TransitionType", displayName="TransitionType")
class TransitionType(BaseObjectType):
    transitionNumber: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2312", browseName="TransitionNumber", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2340", browseName="AggregateFunctionType", displayName="AggregateFunctionType")
class AggregateFunctionType(BaseObjectType):
    pass


o6.call(nodeId="i=2426", browseName="Start", modellingRule="OptionalPlaceholder")

o6.call(nodeId="i=2427", browseName="Suspend", modellingRule="OptionalPlaceholder")

o6.call(nodeId="i=2428", browseName="Resume", modellingRule="OptionalPlaceholder")

o6.call(nodeId="i=2429", browseName="Halt", modellingRule="OptionalPlaceholder")

o6.call(nodeId="i=2430", browseName="Reset", modellingRule="OptionalPlaceholder")

o6.call(nodeId="i=2947", browseName="Unshelve", modellingRule="Mandatory")

o6.call(nodeId="i=2948", browseName="OneShotShelve", modellingRule="Mandatory")

ns0_vartypes.PropertyType(
    nodeId="i=2991",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=2949",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ShelvingTime", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=2949", browseName="TimedShelve", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=2991"]))

ns0_vartypes.PropertyType(
    nodeId="i=3876",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=3875",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0_datypes.Argument(
            name="SubscriptionId", dataType=o6.NodeId("i=288"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The identifier for the subscription to refresh.")
        )
    ],
)
o6.call(nodeId="i=3875", browseName="ConditionRefresh", inputArgs=o6.hasProperty(o6.ns["i=3876"]))

o6.call(nodeId="i=9027", browseName="Enable", modellingRule="Mandatory")

o6.call(nodeId="i=9028", browseName="Disable", modellingRule="Mandatory")

ns0_vartypes.PropertyType(
    nodeId="i=9030",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=9029",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(
            name="EventId", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The identifier for the event to comment.")
        ),
        ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="i=9029", browseName="AddComment", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=9030"]))

ns0_vartypes.PropertyType(
    nodeId="i=9070",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=9069",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SelectedResponse", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=9069", browseName="Respond", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=9070"]))

ns0_vartypes.PropertyType(
    nodeId="i=9112",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=9111",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(
            name="EventId", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The identifier for the event to comment.")
        ),
        ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="i=9111", browseName="Acknowledge", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=9112"]))

ns0_vartypes.PropertyType(
    nodeId="i=9114",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=9113",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(
            name="EventId", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The identifier for the event to comment.")
        ),
        ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="i=9113", browseName="Confirm", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=9114"]))


@o6.objecttype(nodeId="i=11163", browseName="BaseConditionClassType", displayName="BaseConditionClassType", isAbstract=True)
class BaseConditionClassType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=11164", browseName="ProcessConditionClassType", displayName="ProcessConditionClassType", isAbstract=True)
class ProcessConditionClassType(BaseConditionClassType):
    pass


@o6.objecttype(nodeId="i=11165", browseName="MaintenanceConditionClassType", displayName="MaintenanceConditionClassType", isAbstract=True)
class MaintenanceConditionClassType(BaseConditionClassType):
    pass


@o6.objecttype(nodeId="i=11166", browseName="SystemConditionClassType", displayName="SystemConditionClassType", isAbstract=True)
class SystemConditionClassType(BaseConditionClassType):
    pass


@o6.objecttype(nodeId="i=11187", browseName="AggregateConfigurationType", displayName="AggregateConfigurationType")
class AggregateConfigurationType(BaseObjectType):
    percentDataBad: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11189", browseName="PercentDataBad", modellingRule="Mandatory", dataType=o6.Byte, valueRank=-1)
    )
    percentDataGood: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11190", browseName="PercentDataGood", modellingRule="Mandatory", dataType=o6.Byte, valueRank=-1)
    )
    treatUncertainAsBad: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11188", browseName="TreatUncertainAsBad", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    useSlopedExtrapolation: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11191", browseName="UseSlopedExtrapolation", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )


ns0_vartypes.PropertyType(
    nodeId="i=11490",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=11489",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SubscriptionId", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=11491",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=11489",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="ServerHandles", dataType=o6.NodeId("i=7"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="ClientHandles", dataType=o6.NodeId("i=7"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="i=11489", browseName="GetMonitoredItems", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=11490"]), outputArgs=o6.hasProperty(o6.ns["i=11491"]))

ns0_vartypes.PropertyType(
    nodeId="i=11581",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=11580",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Mode", dataType=o6.NodeId("i=3"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=11582",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=11580",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=11580", browseName="Open", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=11581"]), outputArgs=o6.hasProperty(o6.ns["i=11582"]))

ns0_vartypes.PropertyType(
    nodeId="i=11584",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=11583",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=11583", browseName="Close", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=11584"]))

ns0_vartypes.PropertyType(
    nodeId="i=11586",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=11585",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Length", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=11587",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=11585",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Data", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=11585", browseName="Read", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=11586"]), outputArgs=o6.hasProperty(o6.ns["i=11587"]))

ns0_vartypes.PropertyType(
    nodeId="i=11589",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=11588",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Data", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=11588", browseName="Write", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=11589"]))

ns0_vartypes.PropertyType(
    nodeId="i=11591",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=11590",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=11592",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=11590",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Position", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=11590", browseName="GetPosition", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=11591"]), outputArgs=o6.hasProperty(o6.ns["i=11592"]))

ns0_vartypes.PropertyType(
    nodeId="i=11594",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=11593",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Position", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=11593", browseName="SetPosition", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=11594"]))


@o6.objecttype(nodeId="i=11645", browseName="NamespacesType", displayName="NamespacesType")
class NamespacesType(BaseObjectType):
    namespaceIdentifier_: NamespaceMetadataType | None


@o6.objecttype(nodeId="i=11564", browseName="OperationLimitsType", displayName="OperationLimitsType")
class OperationLimitsType(FolderType):
    maxMonitoredItemsPerCall: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11574", browseName="MaxMonitoredItemsPerCall", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerBrowse: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11570", browseName="MaxNodesPerBrowse", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerHistoryReadData: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12161", browseName="MaxNodesPerHistoryReadData", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerHistoryReadEvents: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12162", browseName="MaxNodesPerHistoryReadEvents", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerHistoryUpdateData: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12163", browseName="MaxNodesPerHistoryUpdateData", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerHistoryUpdateEvents: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12164", browseName="MaxNodesPerHistoryUpdateEvents", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerMethodCall: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11569", browseName="MaxNodesPerMethodCall", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerNodeManagement: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11573", browseName="MaxNodesPerNodeManagement", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerRead: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11565", browseName="MaxNodesPerRead", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerRegisterNodes: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11571", browseName="MaxNodesPerRegisterNodes", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerTranslateBrowsePathsToNodeIds: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11572", browseName="MaxNodesPerTranslateBrowsePathsToNodeIds", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNodesPerWrite: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11567", browseName="MaxNodesPerWrite", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )


ns0_vartypes.PropertyType(
    nodeId="i=12544",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12543",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Masks", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=12545",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=12543",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=12543", browseName="OpenWithMasks", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=12544"]), outputArgs=o6.hasProperty(o6.ns["i=12545"]))

ns0_vartypes.PropertyType(
    nodeId="i=12547",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=12546",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ApplyChangesRequired", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=12705",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12546",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=12546", browseName="CloseAndUpdate", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=12705"]), outputArgs=o6.hasProperty(o6.ns["i=12547"]))

ns0_vartypes.PropertyType(
    nodeId="i=12549",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12548",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="Certificate", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="IsTrustedCertificate", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=12548", browseName="AddCertificate", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=12549"]))

ns0_vartypes.PropertyType(
    nodeId="i=12551",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12550",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="Thumbprint", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="IsTrustedCertificate", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=12550", browseName="RemoveCertificate", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=12551"]))


@o6.objecttype(nodeId="i=12556", browseName="CertificateType", displayName="CertificateType", isAbstract=True)
class CertificateType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=12557", browseName="ApplicationCertificateType", displayName="ApplicationCertificateType", isAbstract=True)
class ApplicationCertificateType(CertificateType):
    pass


@o6.objecttype(nodeId="i=12558", browseName="HttpsCertificateType", displayName="HttpsCertificateType")
class HttpsCertificateType(CertificateType):
    pass


@o6.objecttype(nodeId="i=12559", browseName="RsaMinApplicationCertificateType", displayName="RsaMinApplicationCertificateType")
class RsaMinApplicationCertificateType(ApplicationCertificateType):
    pass


@o6.objecttype(nodeId="i=12560", browseName="RsaSha256ApplicationCertificateType", displayName="RsaSha256ApplicationCertificateType")
class RsaSha256ApplicationCertificateType(ApplicationCertificateType):
    pass


ns0_vartypes.PropertyType(
    nodeId="i=12617",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12616",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0_datypes.Argument(name="CertificateGroupId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CertificateTypeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Certificate", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="IssuerCertificates", dataType=o6.NodeId("i=15"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="PrivateKeyFormat", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="PrivateKey", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=12618",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=12616",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ApplyChangesRequired", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=12616", browseName="UpdateCertificate", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=12617"]), outputArgs=o6.hasProperty(o6.ns["i=12618"]))

ns0_vartypes.PropertyType(
    nodeId="i=12732",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12731",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0_datypes.Argument(name="CertificateGroupId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CertificateTypeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SubjectName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RegeneratePrivateKey", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Nonce", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=12733",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=12731",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="CertificateRequest", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=12731", browseName="CreateSigningRequest", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=12732"]), outputArgs=o6.hasProperty(o6.ns["i=12733"]))

ns0_vartypes.PropertyType(
    nodeId="i=12747",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12746",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="SubscriptionId", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="LifetimeInHours", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=12748",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=12746",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="RevisedLifetimeInHours", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=12746", browseName="SetSubscriptionDurable", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=12747"]), outputArgs=o6.hasProperty(o6.ns["i=12748"]))

ns0_vartypes.PropertyType(
    nodeId="i=12776",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=12775",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Certificates", dataType=o6.NodeId("i=15"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=12775", browseName="GetRejectedList", modellingRule="Mandatory", outputArgs=o6.hasProperty(o6.ns["i=12776"]))

ns0_vartypes.PropertyType(
    nodeId="i=12872",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12871",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SubscriptionId", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=12871", browseName="ResendData", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=12872"]))

ns0_vartypes.PropertyType(
    nodeId="i=12884",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12883",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0_datypes.Argument(name="State", dataType=o6.NodeId("i=852"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="EstimatedReturnTime", dataType=o6.NodeId("i=13"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SecondsTillShutdown", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Reason", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Restart", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=12883", browseName="RequestServerStateChange", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=12884"]))

ns0_vartypes.PropertyType(
    nodeId="i=12913",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=12912",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(
            name="SubscriptionId", dataType=o6.NodeId("i=288"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The identifier for the subscription to refresh.")
        ),
        ns0_datypes.Argument(
            name="MonitoredItemId", dataType=o6.NodeId("i=288"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("The identifier for the monitored item to refresh.")
        ),
    ],
)
o6.call(nodeId="i=12912", browseName="ConditionRefresh2", inputArgs=o6.hasProperty(o6.ns["i=12913"]))

ns0_vartypes.PropertyType(
    nodeId="i=13388",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=13387",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DirectoryName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=13389",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=13387",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=13387", browseName="CreateDirectory", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=13388"]), outputArgs=o6.hasProperty(o6.ns["i=13389"]))

ns0_vartypes.PropertyType(
    nodeId="i=13391",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=13390",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="FileName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RequestFileOpen", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=13392",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=13390",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="FileNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=13390", browseName="CreateFile", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=13391"]), outputArgs=o6.hasProperty(o6.ns["i=13392"]))

ns0_vartypes.PropertyType(
    nodeId="i=13394",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=13393",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ObjectToDelete", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=13393", browseName="Delete", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=13394"]))

ns0_vartypes.PropertyType(
    nodeId="i=13396",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=13395",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="ObjectToMoveOrCopy", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="TargetDirectory", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CreateCopy", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="NewName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=13397",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=13395",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="NewNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=13395", browseName="MoveOrCopy", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=13396"]), outputArgs=o6.hasProperty(o6.ns["i=13397"]))


@o6.objecttype(nodeId="i=13353", browseName="FileDirectoryType", displayName="FileDirectoryType")
class FileDirectoryType(FolderType):
    createDirectory: o6.node.MethodNode = o6.hasComponent(o6.ns["i=13387"])
    createFile: o6.node.MethodNode = o6.hasComponent(o6.ns["i=13390"])
    delete: o6.node.MethodNode = o6.hasComponent(o6.ns["i=13393"])
    fileDirectoryName_: FileDirectoryType | None
    fileName_: FileType | None
    moveOrCopy: o6.node.MethodNode = o6.hasComponent(o6.ns["i=13395"])


@o6.objecttype(nodeId="i=13813", browseName="CertificateGroupFolderType", displayName="CertificateGroupFolderType")
class CertificateGroupFolderType(FolderType):
    additionalGroup_: CertificateGroupType | None
    defaultApplicationGroup: CertificateGroupType
    defaultHttpsGroup: CertificateGroupType | None
    defaultUserTokenGroup: CertificateGroupType | None


ns0_vartypes.PropertyType(
    nodeId="i=14226",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=14225",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="GroupId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=14225", browseName="RemoveGroup", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=14226"]))

ns0_vartypes.PropertyType(
    nodeId="i=14433",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=14432",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ConnectionId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=14432", browseName="RemoveConnection", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=14433"]))

ns0_vartypes.PropertyType(
    nodeId="i=14494",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=14493",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FieldNameAliases", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="FieldFlags", dataType=o6.NodeId("i=15904"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="VariablesToAdd", dataType=o6.NodeId("i=14273"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=14495",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=14493",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0_datypes.Argument(name="DataSetNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="AddResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="i=14493", browseName="AddPublishedDataItems", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=14494"]), outputArgs=o6.hasProperty(o6.ns["i=14495"]))

ns0_vartypes.PropertyType(
    nodeId="i=14497",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=14496",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="EventNotifier", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FieldNameAliases", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="FieldFlags", dataType=o6.NodeId("i=15904"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="SelectedFields", dataType=o6.NodeId("i=601"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="Filter", dataType=o6.NodeId("i=586"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=14498",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=14496",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="ConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="DataSetNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=14496", browseName="AddPublishedEvents", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=14497"]), outputArgs=o6.hasProperty(o6.ns["i=14498"]))

ns0_vartypes.PropertyType(
    nodeId="i=14500",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=14499",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=14499", browseName="RemovePublishedDataSet", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=14500"]))

ns0_vartypes.PropertyType(
    nodeId="i=14556",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=14555",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="ConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FieldNameAliases", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="PromotedFields", dataType=o6.NodeId("i=1"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="VariablesToAdd", dataType=o6.NodeId("i=14273"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=14557",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=14555",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="NewConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="AddResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="i=14555", browseName="AddVariables", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=14556"]), outputArgs=o6.hasProperty(o6.ns["i=14557"]))

ns0_vartypes.PropertyType(
    nodeId="i=14559",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=14558",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="ConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="VariablesToRemove", dataType=o6.NodeId("i=7"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=14560",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=14558",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="NewConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RemoveResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="i=14558", browseName="RemoveVariables", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=14559"]), outputArgs=o6.hasProperty(o6.ns["i=14560"]))


@o6.objecttype(nodeId="i=14643", browseName="PubSubStatusType", displayName="PubSubStatusType")
class PubSubStatusType(BaseObjectType):
    disable: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="i=14646", browseName="Disable", modellingRule="Optional"))
    enable: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="i=14645", browseName="Enable", modellingRule="Optional"))
    state: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=14644", browseName="State", modellingRule="Mandatory", dataType=ns0_datypes.PubSubState, valueRank=-1)
    )


ns0_vartypes.PropertyType(
    nodeId="i=15053",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15052",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="ConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FieldNameAliases", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="PromotedFields", dataType=o6.NodeId("i=1"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="SelectedFields", dataType=o6.NodeId("i=601"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=15517",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15052",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="NewConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15052", browseName="ModifyFieldSelection", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=15053"]), outputArgs=o6.hasProperty(o6.ns["i=15517"]))


@o6.objecttype(nodeId="i=15108", browseName="SubscribedDataSetType", displayName="SubscribedDataSetType")
class SubscribedDataSetType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=15109", browseName="ChoiceStateType", displayName="ChoiceStateType")
class ChoiceStateType(StateType):
    pass


ns0_vartypes.PropertyType(
    nodeId="i=15116",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15115",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="ConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="TargetVariablesToAdd", dataType=o6.NodeId("i=14744"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=15117",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15115",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="AddResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=15115", browseName="AddTargetVariables", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=15116"]), outputArgs=o6.hasProperty(o6.ns["i=15117"]))

ns0_vartypes.PropertyType(
    nodeId="i=15119",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15118",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="ConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="TargetsToRemove", dataType=o6.NodeId("i=7"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=15120",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15118",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="RemoveResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=15118", browseName="RemoveTargetVariables", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=15119"]), outputArgs=o6.hasProperty(o6.ns["i=15120"]))


@o6.objecttype(nodeId="i=15111", browseName="TargetVariablesType", displayName="TargetVariablesType")
class TargetVariablesType(SubscribedDataSetType):
    addTargetVariables: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=15115"])
    removeTargetVariables: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=15118"])
    targetVariables: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=15114", browseName="TargetVariables", modellingRule="Mandatory", dataType=ns0_datypes.FieldTargetDataType, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(nodeId="i=15127", browseName="SubscribedDataSetMirrorType", displayName="SubscribedDataSetMirrorType")
class SubscribedDataSetMirrorType(SubscribedDataSetType):
    pass


@o6.objecttype(nodeId="i=15305", browseName="DataSetWriterTransportType", displayName="DataSetWriterTransportType", isAbstract=True)
class DataSetWriterTransportType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=15319", browseName="DataSetReaderTransportType", displayName="DataSetReaderTransportType", isAbstract=True)
class DataSetReaderTransportType(BaseObjectType):
    pass


ns0_vartypes.PropertyType(
    nodeId="i=15462",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15461",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0_datypes.Argument(name="SecurityGroupName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="KeyLifetime", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SecurityPolicyUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="MaxFutureKeyCount", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="MaxPastKeyCount", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=15463",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15461",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="SecurityGroupId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SecurityGroupNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=15461", browseName="AddSecurityGroup", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15462"]), outputArgs=o6.hasProperty(o6.ns["i=15463"]))

ns0_vartypes.PropertyType(
    nodeId="i=15465",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15464",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SecurityGroupNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15464", browseName="RemoveSecurityGroup", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15465"]))

ns0_vartypes.PropertyType(
    nodeId="i=15492",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15491",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="FieldName", dataType=o6.NodeId("i=20"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FieldValue", dataType=o6.NodeId("i=24"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=15493",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15491",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="FieldId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15491", browseName="AddExtensionField", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15492"]), outputArgs=o6.hasProperty(o6.ns["i=15493"]))

ns0_vartypes.PropertyType(
    nodeId="i=15495",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15494",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="FieldId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15494", browseName="RemoveExtensionField", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15495"]))


@o6.objecttype(nodeId="i=15489", browseName="ExtensionFieldsType", displayName="ExtensionFieldsType")
class ExtensionFieldsType(BaseObjectType):
    addExtensionField: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15491"])
    extensionFieldName_: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15490", browseName="<ExtensionFieldName>", modellingRule="OptionalPlaceholder", valueRank=-1)
    )
    removeExtensionField: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15494"])


ns0_vartypes.PropertyType(
    nodeId="i=15506",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15505",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="VersionToUpdate", dataType=o6.NodeId("i=20998"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Targets", dataType=o6.NodeId("i=15538"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="RevertAfterTime", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RestartDelayTime", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=15507",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15505",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0_datypes.Argument(name="UpdateResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="NewVersion", dataType=o6.NodeId("i=20998"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="UpdateId", dataType=o6.NodeId("i=14"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=15505", browseName="CloseAndUpdate", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15506"]), outputArgs=o6.hasProperty(o6.ns["i=15507"]))

ns0_vartypes.PropertyType(
    nodeId="i=15511",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15508",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="UpdateId", dataType=o6.NodeId("i=14"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15508", browseName="ConfirmUpdate", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15511"]))

ns0_vartypes.PropertyType(
    nodeId="i=15625",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15624",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Rule", dataType=o6.NodeId("i=15634"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15624", browseName="AddIdentity", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=15625"]))

ns0_vartypes.PropertyType(
    nodeId="i=15627",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15626",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Rule", dataType=o6.NodeId("i=15634"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15626", browseName="RemoveIdentity", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=15627"]))

ns0_vartypes.PropertyType(
    nodeId="i=15747",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15746",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="GenerateOptions", dataType=o6.NodeId("i=24"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=15748",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15746",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0_datypes.Argument(name="FileNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=15746", browseName="GenerateFileForRead", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15747"]), outputArgs=o6.hasProperty(o6.ns["i=15748"]))

ns0_vartypes.PropertyType(
    nodeId="i=15750",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15749",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="FileNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=16359",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15749",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="GenerateOptions", dataType=o6.NodeId("i=24"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15749", browseName="GenerateFileForWrite", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=16359"]), outputArgs=o6.hasProperty(o6.ns["i=15750"]))

ns0_vartypes.PropertyType(
    nodeId="i=15752",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15751",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=15753",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15751",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15751", browseName="CloseAndCommit", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15752"]), outputArgs=o6.hasProperty(o6.ns["i=15753"]))


@o6.objecttype(nodeId="i=15744", browseName="TemporaryFileTransferType", displayName="TemporaryFileTransferType")
class TemporaryFileTransferType(BaseObjectType):
    clientProcessingTimeout: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15745", browseName="ClientProcessingTimeout", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    closeAndCommit: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15751"])
    generateFileForRead: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15746"])
    generateFileForWrite: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15749"])
    transferState_: FileTransferStateMachineType | None


ns0_vartypes.PropertyType(
    nodeId="i=15908",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15907",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0_datypes.Argument(name="SecurityGroupId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="StartingTokenId", dataType=o6.NodeId("i=288"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RequestedKeyCount", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=15909",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15907",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0_datypes.Argument(name="SecurityPolicyUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FirstTokenId", dataType=o6.NodeId("i=288"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Keys", dataType=o6.NodeId("i=15"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="TimeToNextKey", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="KeyLifetime", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=15907", browseName="GetSecurityKeys", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=15908"]), outputArgs=o6.hasProperty(o6.ns["i=15909"]))

ns0_vartypes.PropertyType(
    nodeId="i=15911",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15910",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SecurityGroupId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=15912",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15910",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SecurityGroupNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15910", browseName="GetSecurityGroup", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=15911"]), outputArgs=o6.hasProperty(o6.ns["i=15912"]))


@o6.objecttype(nodeId="i=15906", browseName="PubSubKeyServiceType", displayName="PubSubKeyServiceType")
class PubSubKeyServiceType(BaseObjectType):
    getSecurityGroup: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=15910"])
    getSecurityKeys: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=15907"])
    keyPushTargets: PubSubKeyPushTargetFolderType | None
    securityGroups: SecurityGroupFolderType | None


ns0_vartypes.PropertyType(
    nodeId="i=15998",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=15997",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="RoleName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="NamespaceUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=15999",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=15997",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="RoleNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=15997", browseName="AddRole", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=15998"]), outputArgs=o6.hasProperty(o6.ns["i=15999"]))

ns0_vartypes.PropertyType(
    nodeId="i=16001",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16000",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="RoleNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=16000", browseName="RemoveRole", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=16001"]))


@o6.objecttype(nodeId="i=15607", browseName="RoleSetType", displayName="RoleSetType")
class RoleSetType(BaseObjectType):
    addRole: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15997"])
    removeRole: o6.node.MethodNode = o6.hasComponent(o6.ns["i=16000"])
    roleName_: RoleType | None


ns0_vartypes.PropertyType(
    nodeId="i=16177",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16176",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ApplicationUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=16176", browseName="AddApplication", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=16177"]))

ns0_vartypes.PropertyType(
    nodeId="i=16179",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16178",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ApplicationUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=16178", browseName="RemoveApplication", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=16179"]))

ns0_vartypes.PropertyType(
    nodeId="i=16181",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16180",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Endpoint", dataType=o6.NodeId("i=15528"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=16180", browseName="AddEndpoint", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=16181"]))

ns0_vartypes.PropertyType(
    nodeId="i=16183",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16182",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Endpoint", dataType=o6.NodeId("i=15528"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=16182", browseName="RemoveEndpoint", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=16183"]))

o6.call(nodeId="i=16402", browseName="Silence", modellingRule="Optional")

o6.call(nodeId="i=16403", browseName="Suppress", modellingRule="Optional")


@o6.objecttype(nodeId="i=16405", browseName="AlarmGroupType", displayName="AlarmGroupType")
class AlarmGroupType(FolderType):
    alarmConditionInstance_: AlarmConditionType | None


ns0_vartypes.PropertyType(
    nodeId="i=16599",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16598",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Configuration", dataType=o6.NodeId("i=15617"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=16600",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=16598",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ConnectionId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=16598", browseName="AddConnection", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=16599"]), outputArgs=o6.hasProperty(o6.ns["i=16600"]))


@o6.objecttype(nodeId="i=16662", browseName="ApplicationConfigurationFolderType", displayName="ApplicationConfigurationFolderType")
class ApplicationConfigurationFolderType(FolderType):
    applicationName_: ApplicationConfigurationType | None


ns0_vartypes.PropertyType(
    nodeId="i=16958",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16935",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="DataSetMetaData", dataType=o6.NodeId("i=14523"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="VariablesToAdd", dataType=o6.NodeId("i=14273"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=16959",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=16935",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="DataSetNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="AddResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(
    nodeId="i=16935", browseName="AddPublishedDataItemsTemplate", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=16958"]), outputArgs=o6.hasProperty(o6.ns["i=16959"])
)

ns0_vartypes.PropertyType(
    nodeId="i=16961",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16960",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="DataSetMetaData", dataType=o6.NodeId("i=14523"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="EventNotifier", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SelectedFields", dataType=o6.NodeId("i=601"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="Filter", dataType=o6.NodeId("i=586"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=16971",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=16960",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(
    nodeId="i=16960", browseName="AddPublishedEventsTemplate", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=16961"]), outputArgs=o6.hasProperty(o6.ns["i=16971"])
)

ns0_vartypes.PropertyType(
    nodeId="i=16995",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16994",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=16996",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=16994",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetFolderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=16994", browseName="AddDataSetFolder", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=16995"]), outputArgs=o6.hasProperty(o6.ns["i=16996"]))

ns0_vartypes.PropertyType(
    nodeId="i=17007",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=16997",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetFolderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=16997", browseName="RemoveDataSetFolder", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17007"]))


@o6.objecttype(nodeId="i=14477", browseName="DataSetFolderType", displayName="DataSetFolderType")
class DataSetFolderType(FolderType):
    addDataSetFolder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16994"])
    addPublishedDataItems: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=14493"])
    addPublishedDataItemsTemplate: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16935"])
    addPublishedEvents: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=14496"])
    addPublishedEventsTemplate: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16960"])
    dataSetFolderName_: DataSetFolderType | None
    publishedDataSetName_: PublishedDataSetType | None
    removeDataSetFolder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16997"])
    removePublishedDataSet: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=14499"])


@o6.objecttype(nodeId="i=17218", browseName="SafetyConditionClassType", displayName="SafetyConditionClassType", isAbstract=True)
class SafetyConditionClassType(BaseConditionClassType):
    pass


@o6.objecttype(nodeId="i=17219", browseName="HighlyManagedAlarmConditionClassType", displayName="HighlyManagedAlarmConditionClassType", isAbstract=True)
class HighlyManagedAlarmConditionClassType(BaseConditionClassType):
    pass


@o6.objecttype(nodeId="i=17220", browseName="TrainingConditionClassType", displayName="TrainingConditionClassType", isAbstract=True)
class TrainingConditionClassType(BaseConditionClassType):
    pass


@o6.objecttype(nodeId="i=17221", browseName="TestingConditionClassType", displayName="TestingConditionClassType", isAbstract=True)
class TestingConditionClassType(BaseConditionClassType):
    pass


ns0_vartypes.PropertyType(
    nodeId="i=17297",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17296",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0_datypes.Argument(name="SecurityGroupId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SecurityPolicyUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CurrentTokenId", dataType=o6.NodeId("i=288"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CurrentKey", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="FutureKeys", dataType=o6.NodeId("i=15"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="TimeToNextKey", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="KeyLifetime", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=17296", browseName="SetSecurityKeys", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17297"]))

ns0_vartypes.PropertyType(
    nodeId="i=17387",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17386",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="ConfigurationVersion", dataType=o6.NodeId("i=14593"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="TargetVariablesToAdd", dataType=o6.NodeId("i=14744"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=17388",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=17386",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="AddResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=17386", browseName="CreateTargetVariables", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17387"]), outputArgs=o6.hasProperty(o6.ns["i=17388"]))

ns0_vartypes.PropertyType(
    nodeId="i=17390",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17389",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="ParentNodeName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RolePermissions", dataType=o6.NodeId("i=96"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=17391",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=17389",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ParentNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=17389", browseName="CreateDataSetMirror", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17390"]), outputArgs=o6.hasProperty(o6.ns["i=17391"]))

ns0_vartypes.PropertyType(
    nodeId="i=17428",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17427",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Configuration", dataType=o6.NodeId("i=15480"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=17456",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=17427",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="GroupId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=17427", browseName="AddWriterGroup", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17428"]), outputArgs=o6.hasProperty(o6.ns["i=17456"]))

ns0_vartypes.PropertyType(
    nodeId="i=17507",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17465",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Configuration", dataType=o6.NodeId("i=15520"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=17508",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=17465",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="GroupId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=17465", browseName="AddReaderGroup", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17507"]), outputArgs=o6.hasProperty(o6.ns["i=17508"]))

ns0_vartypes.PropertyType(
    nodeId="i=17523",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17522",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ResourceUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ProfileUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="EndpointUrls", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=17524",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=17522",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="CredentialNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=17522", browseName="CreateCredential", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17523"]), outputArgs=o6.hasProperty(o6.ns["i=17524"]))


@o6.objecttype(nodeId="i=17496", browseName="KeyCredentialConfigurationFolderType", displayName="KeyCredentialConfigurationFolderType")
class KeyCredentialConfigurationFolderType(FolderType):
    createCredential: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17522"])
    serviceName_: KeyCredentialConfigurationType | None


ns0_vartypes.PropertyType(
    nodeId="i=17535",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17534",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="CredentialId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RequestedSecurityPolicyUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=17536",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=17534",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="PublicKey", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RevisedSecurityPolicyUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=17534", browseName="GetEncryptingKey", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17535"]), outputArgs=o6.hasProperty(o6.ns["i=17536"]))


@o6.objecttype(nodeId="i=17589", browseName="DictionaryEntryType", displayName="DictionaryEntryType", isAbstract=True)
class DictionaryEntryType(BaseObjectType):
    dictionaryEntryName_: DictionaryEntryType | None


@o6.objecttype(nodeId="i=17591", browseName="DictionaryFolderType", displayName="DictionaryFolderType")
class DictionaryFolderType(FolderType):
    dictionaryEntryName_: DictionaryEntryType | None = o6.hasComponent(
        DictionaryEntryType(nodeId="i=17593", browseName="<DictionaryEntryName>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
    )
    dictionaryFolderName_: DictionaryFolderType | None


@o6.objecttype(nodeId="i=17598", browseName="IrdiDictionaryEntryType", displayName="IrdiDictionaryEntryType")
class IrdiDictionaryEntryType(DictionaryEntryType):
    pass


@o6.objecttype(nodeId="i=17600", browseName="UriDictionaryEntryType", displayName="UriDictionaryEntryType")
class UriDictionaryEntryType(DictionaryEntryType):
    pass


@o6.objecttype(nodeId="i=17602", browseName="BaseInterfaceType", displayName="BaseInterfaceType", isAbstract=True)
class BaseInterfaceType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=2004", browseName="ServerType", displayName="ServerType")
class ServerType(BaseObjectType):
    auditing: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2742", browseName="Auditing", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    estimatedReturnTime: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12882", browseName="EstimatedReturnTime", modellingRule="Optional", dataType=o6.DateTime, valueRank=-1)
    )
    getMonitoredItems: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=11489"])
    localTime: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17612", browseName="LocalTime", modellingRule="Optional", dataType=ns0_datypes.TimeZoneDataType, valueRank=-1)
    )
    namespaceArray: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2006", browseName="NamespaceArray", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    namespaces: NamespacesType | None = o6.hasComponent(NamespacesType(nodeId="i=11527", browseName="Namespaces", modellingRule="Optional"))
    requestServerStateChange: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=12883"])
    resendData: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=12871"])
    serverArray: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2005", browseName="ServerArray", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    serverCapabilities: ServerCapabilitiesType
    serverDiagnostics: ServerDiagnosticsType
    serverRedundancy: ServerRedundancyType
    serverStatus: ns0_vartypes.ServerStatusType
    serviceLevel: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2008", browseName="ServiceLevel", modellingRule="Mandatory", dataType=o6.Byte, valueRank=-1)
    )
    setSubscriptionDurable: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=12746"])
    urisVersion: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15003", browseName="UrisVersion", modellingRule="Optional", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )
    vendorServerInfo: VendorServerInfoType = o6.hasComponent(VendorServerInfoType(nodeId="i=2011", browseName="VendorServerInfo", modellingRule="Mandatory"))


@o6.objecttype(nodeId="i=2771", browseName="FiniteStateMachineType", displayName="FiniteStateMachineType", isAbstract=True)
class FiniteStateMachineType(StateMachineType):
    availableStates: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=17635", browseName="AvailableStates", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    availableTransitions: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=17636", browseName="AvailableTransitions", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    currentState: ns0_vartypes.FiniteStateVariableType
    lastTransition: ns0_vartypes.FiniteTransitionVariableType | None


@o6.objecttype(nodeId="i=2391", browseName="ProgramStateMachineType", displayName="ProgramStateMachineType")
class ProgramStateMachineType(FiniteStateMachineType):
    autoDelete: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2394", browseName="AutoDelete", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    creatable: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=2392", browseName="Creatable", dataType=o6.Boolean, valueRank=-1))
    currentState: ns0_vartypes.FiniteStateVariableType
    deletable: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2393", browseName="Deletable", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    finalResultData: BaseObjectType | None = o6.hasComponent(BaseObjectType(nodeId="i=3850", browseName="FinalResultData", modellingRule="Optional"))
    halt: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=2429"])
    halted: StateType
    haltedToReady: TransitionType
    instanceCount: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=2396", browseName="InstanceCount", dataType=o6.UInt32, valueRank=-1))
    lastTransition: ns0_vartypes.FiniteTransitionVariableType
    maxInstanceCount: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=2397", browseName="MaxInstanceCount", dataType=o6.UInt32, valueRank=-1))
    maxRecycleCount: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=2398", browseName="MaxRecycleCount", dataType=o6.UInt32, valueRank=-1))
    programDiagnostic: ns0_vartypes.ProgramDiagnostic2Type | None
    ready: StateType
    readyToHalted: TransitionType
    readyToRunning: TransitionType
    recycleCount: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2395", browseName="RecycleCount", modellingRule="Mandatory", dataType=o6.Int32, valueRank=-1)
    )
    reset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=2430"])
    resume: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=2428"])
    running: StateType
    runningToHalted: TransitionType
    runningToReady: TransitionType
    runningToSuspended: TransitionType
    start: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=2426"])
    suspend: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=2427"])
    suspended: StateType
    suspendedToHalted: TransitionType
    suspendedToReady: TransitionType
    suspendedToRunning: TransitionType


@o6.objecttype(nodeId="i=9318", browseName="ExclusiveLimitStateMachineType", displayName="ExclusiveLimitStateMachineType")
class ExclusiveLimitStateMachineType(FiniteStateMachineType):
    high: StateType
    highHigh: StateType
    highHighToHigh: TransitionType
    highToHighHigh: TransitionType
    low: StateType
    lowLow: StateType
    lowLowToLow: TransitionType
    lowToLowLow: TransitionType


@o6.objecttype(nodeId="i=15803", browseName="FileTransferStateMachineType", displayName="FileTransferStateMachineType")
class FileTransferStateMachineType(FiniteStateMachineType):
    applyWrite: StateType
    applyWriteToError: TransitionType
    applyWriteToIdle: TransitionType
    error: StateType
    errorToIdle: TransitionType
    idle: InitialStateType
    idleToApplyWrite: TransitionType
    idleToReadPrepare: TransitionType
    readPrepare: StateType
    readPrepareToError: TransitionType
    readPrepareToReadTransfer: TransitionType
    readTransfer: StateType
    readTransferToError: TransitionType
    readTransferToIdle: TransitionType
    reset: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="i=15843", browseName="Reset", modellingRule="Mandatory"))


@o6.objecttype(nodeId="i=17721", browseName="ConnectionTransportType", displayName="ConnectionTransportType", isAbstract=True)
class ConnectionTransportType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=15155", browseName="BrokerConnectionTransportType", displayName="BrokerConnectionTransportType")
class BrokerConnectionTransportType(ConnectionTransportType):
    authenticationProfileUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15178", browseName="AuthenticationProfileUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    resourceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15156", browseName="ResourceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=14209", browseName="PubSubConnectionType", displayName="PubSubConnectionType")
class PubSubConnectionType(BaseObjectType):
    addReaderGroup: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17465"])
    addWriterGroup: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17427"])
    address: NetworkAddressType
    connectionProperties: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=17485", browseName="ConnectionProperties", modellingRule="Mandatory", dataType=ns0_datypes.KeyValuePair, valueRank=1, arrayDimensions=[0]
        )
    )
    diagnostics: PubSubDiagnosticsConnectionType | None
    publisherId: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=14595", browseName="PublisherId", modellingRule="Mandatory", valueRank=-1))
    readerGroupName_: ReaderGroupType | None
    removeGroup: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=14225"])
    status: PubSubStatusType
    transportProfileUri: ns0_vartypes.SelectionListType
    transportSettings: ConnectionTransportType | None = o6.hasComponent(
        ConnectionTransportType(nodeId="i=17203", browseName="TransportSettings", modellingRule="Optional", _allow_abstract=True)
    )
    writerGroupName_: WriterGroupType | None


@o6.objecttype(nodeId="i=14232", browseName="PubSubGroupType", displayName="PubSubGroupType", isAbstract=True)
class PubSubGroupType(BaseObjectType):
    groupProperties: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17488", browseName="GroupProperties", modellingRule="Mandatory", dataType=ns0_datypes.KeyValuePair, valueRank=1, arrayDimensions=[0])
    )
    maxNetworkMessageSize: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17724", browseName="MaxNetworkMessageSize", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    securityGroupId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15927", browseName="SecurityGroupId", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    securityKeyServices: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=15928", browseName="SecurityKeyServices", modellingRule="Optional", dataType=ns0_datypes.EndpointDescription, valueRank=1, arrayDimensions=[0]
        )
    )
    securityMode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15926", browseName="SecurityMode", modellingRule="Mandatory", dataType=ns0_datypes.MessageSecurityMode, valueRank=-1)
    )
    status: PubSubStatusType


o6.call(nodeId="i=17868", browseName="Unsuppress", modellingRule="Optional")

o6.call(nodeId="i=17869", browseName="RemoveFromService", modellingRule="Optional")

o6.call(nodeId="i=17870", browseName="PlaceInService", modellingRule="Optional")

ns0_vartypes.PropertyType(
    nodeId="i=17976",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17969",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Configuration", dataType=o6.NodeId("i=15597"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=17987",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=17969",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetWriterNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=17969", browseName="AddDataSetWriter", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17976"]), outputArgs=o6.hasProperty(o6.ns["i=17987"]))

ns0_vartypes.PropertyType(
    nodeId="i=17993",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=17992",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetWriterNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=17992", browseName="RemoveDataSetWriter", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=17993"]))


@o6.objecttype(nodeId="i=17997", browseName="WriterGroupTransportType", displayName="WriterGroupTransportType", isAbstract=True)
class WriterGroupTransportType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=17998", browseName="WriterGroupMessageType", displayName="WriterGroupMessageType", isAbstract=True)
class WriterGroupMessageType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=17725", browseName="WriterGroupType", displayName="WriterGroupType")
class WriterGroupType(PubSubGroupType):
    addDataSetWriter: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17969"])
    dataSetWriterName_: DataSetWriterType | None
    diagnostics: PubSubDiagnosticsWriterGroupType | None
    headerLayoutUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17559", browseName="HeaderLayoutUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    keepAliveTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17738", browseName="KeepAliveTime", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    localeIds: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17740", browseName="LocaleIds", modellingRule="Mandatory", dataType=ns0_datypes.LocaleId, valueRank=1, arrayDimensions=[0])
    )
    messageSettings: WriterGroupMessageType | None = o6.hasComponent(
        WriterGroupMessageType(nodeId="i=17742", browseName="MessageSettings", modellingRule="Optional", _allow_abstract=True)
    )
    priority: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17739", browseName="Priority", modellingRule="Mandatory", dataType=o6.Byte, valueRank=-1)
    )
    publishingInterval: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17737", browseName="PublishingInterval", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    removeDataSetWriter: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17992"])
    transportSettings: WriterGroupTransportType | None = o6.hasComponent(
        WriterGroupTransportType(nodeId="i=17741", browseName="TransportSettings", modellingRule="Optional", _allow_abstract=True)
    )
    writerGroupId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17736", browseName="WriterGroupId", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )


ns0_vartypes.PropertyType(
    nodeId="i=18007",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=18006",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="CredentialId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CredentialSecret", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CertificateThumbprint", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SecurityPolicyUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=18006", browseName="UpdateCredential", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=18007"]))


@o6.objecttype(nodeId="i=17852", browseName="AuthorizationServiceConfigurationType", displayName="AuthorizationServiceConfigurationType")
class AuthorizationServiceConfigurationType(BaseObjectType):
    issuerEndpointUrl: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18073", browseName="IssuerEndpointUrl", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    serviceCertificate: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17860", browseName="ServiceCertificate", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )
    serviceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18072", browseName="ServiceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


o6.call(nodeId="i=18199", browseName="Reset", modellingRule="Optional")


@o6.objecttype(nodeId="i=18001", browseName="KeyCredentialConfigurationType", displayName="KeyCredentialConfigurationType")
class KeyCredentialConfigurationType(BaseObjectType):
    credentialId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18657", browseName="CredentialId", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    deleteCredential: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="i=18008", browseName="DeleteCredential", modellingRule="Optional"))
    endpointUrls: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18004", browseName="EndpointUrls", modellingRule="Optional", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    getEncryptingKey: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17534"])
    profileUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18165", browseName="ProfileUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    resourceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18069", browseName="ResourceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    serviceStatus: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18005", browseName="ServiceStatus", modellingRule="Optional", dataType=o6.StatusCode, valueRank=-1)
    )
    updateCredential: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=18006"])


@o6.objecttype(nodeId="i=18665", browseName="StatisticalConditionClassType", displayName="StatisticalConditionClassType", isAbstract=True)
class StatisticalConditionClassType(BaseConditionClassType):
    pass


o6.call(nodeId="i=18666", browseName="Reset", modellingRule="Mandatory")


@o6.objecttype(nodeId="i=17279", browseName="AlarmMetricsType", displayName="AlarmMetricsType")
class AlarmMetricsType(BaseObjectType):
    alarmCount: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=17280", browseName="AlarmCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    averageAlarmRate: ns0_vartypes.AlarmRateVariableType
    currentAlarmRate: ns0_vartypes.AlarmRateVariableType
    maximumActiveState: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=17281", browseName="MaximumActiveState", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    maximumAlarmRate: ns0_vartypes.AlarmRateVariableType
    maximumReAlarmCount: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=17283", browseName="MaximumReAlarmCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maximumUnAck: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=17282", browseName="MaximumUnAck", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    reset: o6.node.MethodNode = o6.hasComponent(o6.ns["i=18666"])
    startTime: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=17991", browseName="StartTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


@o6.objecttype(nodeId="i=18973", browseName="LldpInformationType", displayName="LldpInformationType")
class LldpInformationType(BaseObjectType):
    localSystemData: LldpLocalSystemType
    ports: FolderType
    remoteStatistics: LldpRemoteStatisticsType | None


@o6.objecttype(nodeId="i=18996", browseName="LldpRemoteStatisticsType", displayName="LldpRemoteStatisticsType")
class LldpRemoteStatisticsType(BaseObjectType):
    lastChangeTime: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=18997", browseName="LastChangeTime", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    remoteAgeouts: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19001", browseName="RemoteAgeouts", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    remoteDeletes: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=18999", browseName="RemoteDeletes", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    remoteDrops: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19000", browseName="RemoteDrops", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    remoteInserts: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=18998", browseName="RemoteInserts", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(nodeId="i=19002", browseName="LldpLocalSystemType", displayName="LldpLocalSystemType")
class LldpLocalSystemType(BaseObjectType):
    chassisId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19004", browseName="ChassisId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    chassisIdSubtype: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19003", browseName="ChassisIdSubtype", modellingRule="Mandatory", dataType=ns0_datypes.ChassisIdSubtype, valueRank=-1)
    )
    systemCapabilitiesEnabled: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19008", browseName="SystemCapabilitiesEnabled", modellingRule="Optional", dataType=ns0_datypes.LldpSystemCapabilitiesMap, valueRank=-1)
    )
    systemCapabilitiesSupported: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=19007", browseName="SystemCapabilitiesSupported", modellingRule="Optional", dataType=ns0_datypes.LldpSystemCapabilitiesMap, valueRank=-1
        )
    )
    systemDescription: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19006", browseName="SystemDescription", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    systemName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19005", browseName="SystemName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=19009", browseName="LldpPortInformationType", displayName="LldpPortInformationType")
class LldpPortInformationType(BaseObjectType):
    destMacAddress: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19011", browseName="DestMacAddress", modellingRule="Mandatory", dataType=o6.Byte, valueRank=1, arrayDimensions=[6])
    )
    ietfBaseNetworkInterfaceName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19010", browseName="IetfBaseNetworkInterfaceName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    managementAddressTxPort: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=19015", browseName="ManagementAddressTxPort", modellingRule="Optional", dataType=ns0_datypes.LldpManagementAddressTxPortType, valueRank=1, arrayDimensions=[0]
        )
    )
    portDescription: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19014", browseName="PortDescription", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    portId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19013", browseName="PortId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    portIdSubtype: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19012", browseName="PortIdSubtype", modellingRule="Mandatory", dataType=ns0_datypes.PortIdSubtype, valueRank=-1)
    )
    remoteSystemsData: FolderType | None


@o6.objecttype(nodeId="i=19033", browseName="LldpRemoteSystemType", displayName="LldpRemoteSystemType")
class LldpRemoteSystemType(BaseObjectType):
    chassisId: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19037", browseName="ChassisId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    chassisIdSubtype: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19036", browseName="ChassisIdSubtype", modellingRule="Mandatory", dataType=ns0_datypes.ChassisIdSubtype, valueRank=-1)
    )
    managementAddress: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(
            nodeId="i=19047", browseName="ManagementAddress", modellingRule="Optional", dataType=ns0_datypes.LldpManagementAddressType, valueRank=1, arrayDimensions=[0]
        )
    )
    portDescription: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19040", browseName="PortDescription", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    portId: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19039", browseName="PortId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    portIdSubtype: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19038", browseName="PortIdSubtype", modellingRule="Mandatory", dataType=ns0_datypes.PortIdSubtype, valueRank=-1)
    )
    remoteChanges: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19045", browseName="RemoteChanges", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    remoteIndex: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19035", browseName="RemoteIndex", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    remoteTooManyNeighbors: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19046", browseName="RemoteTooManyNeighbors", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    remoteUnknownTlv: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(
            nodeId="i=19078", browseName="RemoteUnknownTlv", modellingRule="Optional", dataType=ns0_datypes.LldpTlvType, valueRank=1, arrayDimensions=[0]
        )
    )
    systemCapabilitiesEnabled: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(
            nodeId="i=19044", browseName="SystemCapabilitiesEnabled", modellingRule="Optional", dataType=ns0_datypes.LldpSystemCapabilitiesMap, valueRank=-1
        )
    )
    systemCapabilitiesSupported: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(
            nodeId="i=19043", browseName="SystemCapabilitiesSupported", modellingRule="Optional", dataType=ns0_datypes.LldpSystemCapabilitiesMap, valueRank=-1
        )
    )
    systemDescription: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19042", browseName="SystemDescription", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    systemName: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19041", browseName="SystemName", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    timeMark: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19034", browseName="TimeMark", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2330", browseName="HistoryServerCapabilitiesType", displayName="HistoryServerCapabilitiesType")
class HistoryServerCapabilitiesType(BaseObjectType):
    accessHistoryDataCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2331", browseName="AccessHistoryDataCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    accessHistoryEventsCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2332", browseName="AccessHistoryEventsCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    aggregateFunctions: FolderType = o6.hasComponent(FolderType(nodeId="i=11172", browseName="AggregateFunctions", modellingRule="Mandatory"))
    deleteAtTimeCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2338", browseName="DeleteAtTimeCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    deleteEventCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11501", browseName="DeleteEventCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    deleteRawCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2337", browseName="DeleteRawCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    insertAnnotationCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11270", browseName="InsertAnnotationCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    insertDataCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2334", browseName="InsertDataCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    insertEventCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11278", browseName="InsertEventCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    maxReturnDataValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11268", browseName="MaxReturnDataValues", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxReturnEventValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11269", browseName="MaxReturnEventValues", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    replaceDataCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2335", browseName="ReplaceDataCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    replaceEventCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11279", browseName="ReplaceEventCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    serverTimestampSupported: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19094", browseName="ServerTimestampSupported", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    updateDataCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2336", browseName="UpdateDataCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    updateEventCapability: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11280", browseName="UpdateEventCapability", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2029", browseName="SessionDiagnosticsObjectType", displayName="SessionDiagnosticsObjectType")
class SessionDiagnosticsObjectType(BaseObjectType):
    currentRoleIds: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19303", browseName="CurrentRoleIds", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    sessionDiagnostics: ns0_vartypes.SessionDiagnosticsVariableType
    sessionSecurityDiagnostics: ns0_vartypes.SessionSecurityDiagnosticsType
    subscriptionDiagnosticsArray: ns0_vartypes.SubscriptionDiagnosticsArrayType = o6.hasComponent(
        ns0_vartypes.SubscriptionDiagnosticsArrayType(
            nodeId="i=2032",
            browseName="SubscriptionDiagnosticsArray",
            modellingRule="Mandatory",
            dataType=ns0_datypes.SubscriptionDiagnosticsDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.objecttype(nodeId="i=19323", browseName="UserCertificateType", displayName="UserCertificateType", isAbstract=True)
class UserCertificateType(CertificateType):
    pass


@o6.objecttype(nodeId="i=19324", browseName="TlsCertificateType", displayName="TlsCertificateType", isAbstract=True)
class TlsCertificateType(CertificateType):
    pass


@o6.objecttype(nodeId="i=19325", browseName="TlsServerCertificateType", displayName="TlsServerCertificateType")
class TlsServerCertificateType(TlsCertificateType):
    pass


@o6.objecttype(nodeId="i=19326", browseName="TlsClientCertificateType", displayName="TlsClientCertificateType")
class TlsClientCertificateType(TlsCertificateType):
    pass


ns0_vartypes.PropertyType(
    nodeId="i=19338",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=19337",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0_datypes.Argument(name="CertificateGroupId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CertificateTypeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SubjectName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="DnsNames", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="IpAddresses", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="LifetimeInDays", dataType=o6.NodeId("i=5"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="KeySizeInBits", dataType=o6.NodeId("i=5"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=19339",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=19337",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Certificate", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[])],
)
o6.call(
    nodeId="i=19337", browseName="CreateSelfSignedCertificate", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=19338"]), outputArgs=o6.hasProperty(o6.ns["i=19339"])
)

ns0_vartypes.PropertyType(
    nodeId="i=19341",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=19340",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="CertificateGroupId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="CertificateTypeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=19340", browseName="DeleteCertificate", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=19341"]))

ns0_vartypes.PropertyType(
    nodeId="i=19354",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=19353",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0_datypes.Argument(name="StartTime", dataType=o6.NodeId("i=13"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="EndTime", dataType=o6.NodeId("i=13"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="MaxReturnRecords", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="MinimumSeverity", dataType=o6.NodeId("i=5"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RequestMask", dataType=o6.NodeId("i=19749"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ContinuationPointIn", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=19355",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=19353",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="Results", dataType=o6.NodeId("i=19745"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ContinuationPointOut", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=19353", browseName="GetRecords", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=19354"]), outputArgs=o6.hasProperty(o6.ns["i=19355"]))


@o6.objecttype(nodeId="i=19370", browseName="LogEntryConditionClassType", displayName="LogEntryConditionClassType", isAbstract=True)
class LogEntryConditionClassType(BaseConditionClassType):
    pass


@o6.objecttype(nodeId="i=19677", browseName="PubSubDiagnosticsType", displayName="PubSubDiagnosticsType", isAbstract=True)
class PubSubDiagnosticsType(BaseObjectType):
    counters: BaseObjectType
    diagnosticsLevel: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19678", browseName="DiagnosticsLevel", modellingRule="Mandatory", dataType=ns0_datypes.DiagnosticsLevel, valueRank=-1)
    )
    liveValues: BaseObjectType = o6.hasComponent(BaseObjectType(nodeId="i=19722", browseName="LiveValues", modellingRule="Mandatory"))
    reset: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="i=19689", browseName="Reset", modellingRule="Mandatory"))
    subError: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19690", browseName="SubError", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    totalError: ns0_vartypes.PubSubDiagnosticsCounterType
    totalInformation: ns0_vartypes.PubSubDiagnosticsCounterType


@o6.objecttype(nodeId="i=19732", browseName="PubSubDiagnosticsRootType", displayName="PubSubDiagnosticsRootType")
class PubSubDiagnosticsRootType(PubSubDiagnosticsType):
    liveValues: BaseObjectType


@o6.objecttype(nodeId="i=19786", browseName="PubSubDiagnosticsConnectionType", displayName="PubSubDiagnosticsConnectionType")
class PubSubDiagnosticsConnectionType(PubSubDiagnosticsType):
    liveValues: BaseObjectType


@o6.objecttype(nodeId="i=19820", browseName="DataTypeRefinementType", displayName="DataTypeRefinementType")
class DataTypeRefinementType(BaseObjectType):
    fieldDescription_: ns0_vartypes.BaseDataVariableType = o6.reference(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19821", browseName="<FieldDescription>", modellingRule="MandatoryPlaceholder", valueRank=-2), "i=19815"
    )


@o6.objecttype(nodeId="i=19822", browseName="SubtypeRestrictionType", displayName="SubtypeRestrictionType")
class SubtypeRestrictionType(BaseObjectType):
    fieldDescription_: ns0_vartypes.BaseDataVariableType = o6.reference(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19823", browseName="<FieldDescription>", modellingRule="MandatoryPlaceholder", valueRank=-2), "i=19819"
    )


@o6.objecttype(nodeId="i=19834", browseName="PubSubDiagnosticsWriterGroupType", displayName="PubSubDiagnosticsWriterGroupType")
class PubSubDiagnosticsWriterGroupType(PubSubDiagnosticsType):
    counters: BaseObjectType
    liveValues: BaseObjectType


ns0_vartypes.PropertyType(
    nodeId="i=19840",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=19839",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SerializationFilterProperties", dataType=o6.NodeId("i=14533"), valueRank=1, arrayDimensions=[0])],
)
ns0_vartypes.PropertyType(
    nodeId="i=19841",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=19839",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Results", dataType=o6.NodeId("i=6"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=19839", browseName="ConfigureSerialization", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=19840"]), outputArgs=o6.hasProperty(o6.ns["i=19841"]))


@o6.objecttype(nodeId="i=19824", browseName="SerializationEntityType", displayName="SerializationEntityType")
class SerializationEntityType(BaseObjectType):
    configureSerialization: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=19839"])
    considerSubElementSerializationProperties: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19829", browseName="ConsiderSubElementSerializationProperties", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    customMetaDataProperties: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=19830", browseName="CustomMetaDataProperties", modellingRule="Optional", dataType=ns0_datypes.KeyValuePair, valueRank=1, arrayDimensions=[0]
        )
    )
    customMetaDataRef: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19835", browseName="CustomMetaDataRef", modellingRule="Optional", dataType=o6.NodeId, valueRank=-1)
    )
    excludeReferenceTypes: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19827", browseName="ExcludeReferenceTypes", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    includeDictionaryReference: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19838", browseName="IncludeDictionaryReference", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    includeReferenceTypes: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19826", browseName="IncludeReferenceTypes", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    includeSourceTimestamp: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19837", browseName="IncludeSourceTimestamp", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    includeStatus: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19836", browseName="IncludeStatus", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    serializationDepth: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19828", browseName="SerializationDepth", modellingRule="Optional", dataType=o6.UInt16, valueRank=-1)
    )
    serializedData: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=19825", browseName="SerializedData", modellingRule="Mandatory", dataType=ns0_datypes.Structure, valueRank=-1)
    )


@o6.objecttype(nodeId="i=19903", browseName="PubSubDiagnosticsReaderGroupType", displayName="PubSubDiagnosticsReaderGroupType")
class PubSubDiagnosticsReaderGroupType(PubSubDiagnosticsType):
    counters: BaseObjectType
    liveValues: BaseObjectType


@o6.objecttype(nodeId="i=19968", browseName="PubSubDiagnosticsDataSetWriterType", displayName="PubSubDiagnosticsDataSetWriterType")
class PubSubDiagnosticsDataSetWriterType(PubSubDiagnosticsType):
    counters: BaseObjectType
    liveValues: BaseObjectType


@o6.objecttype(nodeId="i=20027", browseName="PubSubDiagnosticsDataSetReaderType", displayName="PubSubDiagnosticsDataSetReaderType")
class PubSubDiagnosticsDataSetReaderType(PubSubDiagnosticsType):
    counters: BaseObjectType
    liveValues: BaseObjectType


ns0_vartypes.PropertyType(
    nodeId="i=21083",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=21082",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Configuration", dataType=o6.NodeId("i=15623"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=21084",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=21082",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetReaderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=21082", browseName="AddDataSetReader", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=21083"]), outputArgs=o6.hasProperty(o6.ns["i=21084"]))

ns0_vartypes.PropertyType(
    nodeId="i=21086",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=21085",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetReaderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=21085", browseName="RemoveDataSetReader", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=21086"]))


@o6.objecttype(nodeId="i=21090", browseName="ReaderGroupTransportType", displayName="ReaderGroupTransportType", isAbstract=True)
class ReaderGroupTransportType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=21091", browseName="ReaderGroupMessageType", displayName="ReaderGroupMessageType", isAbstract=True)
class ReaderGroupMessageType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=17999", browseName="ReaderGroupType", displayName="ReaderGroupType")
class ReaderGroupType(PubSubGroupType):
    addDataSetReader: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=21082"])
    dataSetReaderName_: DataSetReaderType | None
    diagnostics: PubSubDiagnosticsReaderGroupType | None
    messageSettings: ReaderGroupMessageType | None = o6.hasComponent(
        ReaderGroupMessageType(nodeId="i=21081", browseName="MessageSettings", modellingRule="Optional", _allow_abstract=True)
    )
    removeDataSetReader: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=21085"])
    transportSettings: ReaderGroupTransportType | None = o6.hasComponent(
        ReaderGroupTransportType(nodeId="i=21080", browseName="TransportSettings", modellingRule="Optional", _allow_abstract=True)
    )


@o6.objecttype(nodeId="i=21096", browseName="DataSetWriterMessageType", displayName="DataSetWriterMessageType", isAbstract=True)
class DataSetWriterMessageType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=15298", browseName="DataSetWriterType", displayName="DataSetWriterType")
class DataSetWriterType(BaseObjectType):
    dataSetFieldContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21093", browseName="DataSetFieldContentMask", modellingRule="Mandatory", dataType=ns0_datypes.DataSetFieldContentMask, valueRank=-1)
    )
    dataSetWriterId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21092", browseName="DataSetWriterId", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    dataSetWriterProperties: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=17493", browseName="DataSetWriterProperties", modellingRule="Mandatory", dataType=ns0_datypes.KeyValuePair, valueRank=1, arrayDimensions=[0]
        )
    )
    diagnostics: PubSubDiagnosticsDataSetWriterType | None
    keyFrameCount: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21094", browseName="KeyFrameCount", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    messageSettings: DataSetWriterMessageType | None = o6.hasComponent(
        DataSetWriterMessageType(nodeId="i=21095", browseName="MessageSettings", modellingRule="Optional", _allow_abstract=True)
    )
    status: PubSubStatusType
    transportSettings: DataSetWriterTransportType | None = o6.hasComponent(
        DataSetWriterTransportType(nodeId="i=15303", browseName="TransportSettings", modellingRule="Optional", _allow_abstract=True)
    )


@o6.objecttype(nodeId="i=21104", browseName="DataSetReaderMessageType", displayName="DataSetReaderMessageType", isAbstract=True)
class DataSetReaderMessageType(BaseObjectType):
    pass


@o6.objecttype(nodeId="i=15306", browseName="DataSetReaderType", displayName="DataSetReaderType")
class DataSetReaderType(BaseObjectType):
    createDataSetMirror: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17389"])
    createTargetVariables: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17386"])
    dataSetFieldContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21101", browseName="DataSetFieldContentMask", modellingRule="Mandatory", dataType=ns0_datypes.DataSetFieldContentMask, valueRank=-1)
    )
    dataSetMetaData: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21100", browseName="DataSetMetaData", modellingRule="Mandatory", dataType=ns0_datypes.DataSetMetaDataType, valueRank=-1)
    )
    dataSetReaderProperties: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=17494", browseName="DataSetReaderProperties", modellingRule="Mandatory", dataType=ns0_datypes.KeyValuePair, valueRank=1, arrayDimensions=[0]
        )
    )
    dataSetWriterId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21099", browseName="DataSetWriterId", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    diagnostics: PubSubDiagnosticsDataSetReaderType | None
    headerLayoutUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17564", browseName="HeaderLayoutUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    keyFrameCount: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17563", browseName="KeyFrameCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    messageReceiveTimeout: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21102", browseName="MessageReceiveTimeout", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    messageSettings: DataSetReaderMessageType | None = o6.hasComponent(
        DataSetReaderMessageType(nodeId="i=21103", browseName="MessageSettings", modellingRule="Optional", _allow_abstract=True)
    )
    publisherId: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=21097", browseName="PublisherId", modellingRule="Mandatory", valueRank=-1))
    securityGroupId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15933", browseName="SecurityGroupId", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    securityKeyServices: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=15934", browseName="SecurityKeyServices", modellingRule="Optional", dataType=ns0_datypes.EndpointDescription, valueRank=1, arrayDimensions=[0]
        )
    )
    securityMode: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15932", browseName="SecurityMode", modellingRule="Optional", dataType=ns0_datypes.MessageSecurityMode, valueRank=-1)
    )
    status: PubSubStatusType
    subscribedDataSet: SubscribedDataSetType = o6.hasComponent(SubscribedDataSetType(nodeId="i=15316", browseName="SubscribedDataSet", modellingRule="Mandatory"))
    transportSettings: DataSetReaderTransportType | None = o6.hasComponent(
        DataSetReaderTransportType(nodeId="i=15311", browseName="TransportSettings", modellingRule="Optional", _allow_abstract=True)
    )
    writerGroupId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21098", browseName="WriterGroupId", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )


@o6.objecttype(nodeId="i=21105", browseName="UadpWriterGroupMessageType", displayName="UadpWriterGroupMessageType")
class UadpWriterGroupMessageType(WriterGroupMessageType):
    dataSetOrdering: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21107", browseName="DataSetOrdering", modellingRule="Mandatory", dataType=ns0_datypes.DataSetOrderingType, valueRank=-1)
    )
    groupVersion: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21106", browseName="GroupVersion", modellingRule="Mandatory", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )
    networkMessageContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=21108", browseName="NetworkMessageContentMask", modellingRule="Mandatory", dataType=ns0_datypes.UadpNetworkMessageContentMask, valueRank=-1
        )
    )
    publishingOffset: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21110", browseName="PublishingOffset", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=1, arrayDimensions=[0])
    )
    samplingOffset: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21109", browseName="SamplingOffset", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )


@o6.objecttype(nodeId="i=21111", browseName="UadpDataSetWriterMessageType", displayName="UadpDataSetWriterMessageType")
class UadpDataSetWriterMessageType(DataSetWriterMessageType):
    configuredSize: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21113", browseName="ConfiguredSize", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    dataSetMessageContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=21112", browseName="DataSetMessageContentMask", modellingRule="Mandatory", dataType=ns0_datypes.UadpDataSetMessageContentMask, valueRank=-1
        )
    )
    dataSetOffset: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21115", browseName="DataSetOffset", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    networkMessageNumber: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21114", browseName="NetworkMessageNumber", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )


@o6.objecttype(nodeId="i=21116", browseName="UadpDataSetReaderMessageType", displayName="UadpDataSetReaderMessageType")
class UadpDataSetReaderMessageType(DataSetReaderMessageType):
    dataSetClassId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21120", browseName="DataSetClassId", modellingRule="Mandatory", dataType=o6.Guid, valueRank=-1)
    )
    dataSetMessageContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=21122", browseName="DataSetMessageContentMask", modellingRule="Mandatory", dataType=ns0_datypes.UadpDataSetMessageContentMask, valueRank=-1
        )
    )
    dataSetOffset: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17477", browseName="DataSetOffset", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    groupVersion: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21117", browseName="GroupVersion", modellingRule="Mandatory", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )
    networkMessageContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=21121", browseName="NetworkMessageContentMask", modellingRule="Mandatory", dataType=ns0_datypes.UadpNetworkMessageContentMask, valueRank=-1
        )
    )
    networkMessageNumber: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21119", browseName="NetworkMessageNumber", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    processingOffset: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21124", browseName="ProcessingOffset", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    publishingInterval: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21123", browseName="PublishingInterval", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    receiveOffset: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21125", browseName="ReceiveOffset", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )


@o6.objecttype(nodeId="i=21126", browseName="JsonWriterGroupMessageType", displayName="JsonWriterGroupMessageType")
class JsonWriterGroupMessageType(WriterGroupMessageType):
    networkMessageContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=21127", browseName="NetworkMessageContentMask", modellingRule="Mandatory", dataType=ns0_datypes.JsonNetworkMessageContentMask, valueRank=-1
        )
    )


@o6.objecttype(nodeId="i=21128", browseName="JsonDataSetWriterMessageType", displayName="JsonDataSetWriterMessageType")
class JsonDataSetWriterMessageType(DataSetWriterMessageType):
    dataSetMessageContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=21129", browseName="DataSetMessageContentMask", modellingRule="Mandatory", dataType=ns0_datypes.JsonDataSetMessageContentMask, valueRank=-1
        )
    )


@o6.objecttype(nodeId="i=21130", browseName="JsonDataSetReaderMessageType", displayName="JsonDataSetReaderMessageType")
class JsonDataSetReaderMessageType(DataSetReaderMessageType):
    dataSetMessageContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=21132", browseName="DataSetMessageContentMask", modellingRule="Mandatory", dataType=ns0_datypes.JsonDataSetMessageContentMask, valueRank=-1
        )
    )
    networkMessageContentMask: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=21131", browseName="NetworkMessageContentMask", modellingRule="Mandatory", dataType=ns0_datypes.JsonNetworkMessageContentMask, valueRank=-1
        )
    )


@o6.objecttype(nodeId="i=21136", browseName="BrokerWriterGroupTransportType", displayName="BrokerWriterGroupTransportType")
class BrokerWriterGroupTransportType(WriterGroupTransportType):
    authenticationProfileUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15247", browseName="AuthenticationProfileUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    queueName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21137", browseName="QueueName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    requestedDeliveryGuarantee: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=15249", browseName="RequestedDeliveryGuarantee", modellingRule="Mandatory", dataType=ns0_datypes.BrokerTransportQualityOfService, valueRank=-1
        )
    )
    resourceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15246", browseName="ResourceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=21138", browseName="BrokerDataSetWriterTransportType", displayName="BrokerDataSetWriterTransportType")
class BrokerDataSetWriterTransportType(DataSetWriterTransportType):
    authenticationProfileUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15251", browseName="AuthenticationProfileUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    metaDataQueueName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21140", browseName="MetaDataQueueName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    metaDataUpdateTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21141", browseName="MetaDataUpdateTime", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    queueName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21139", browseName="QueueName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    requestedDeliveryGuarantee: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=15330", browseName="RequestedDeliveryGuarantee", modellingRule="Mandatory", dataType=ns0_datypes.BrokerTransportQualityOfService, valueRank=-1
        )
    )
    resourceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15250", browseName="ResourceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=21142", browseName="BrokerDataSetReaderTransportType", displayName="BrokerDataSetReaderTransportType")
class BrokerDataSetReaderTransportType(DataSetReaderTransportType):
    authenticationProfileUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15419", browseName="AuthenticationProfileUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    metaDataQueueName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21144", browseName="MetaDataQueueName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    queueName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21143", browseName="QueueName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    requestedDeliveryGuarantee: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=15420", browseName="RequestedDeliveryGuarantee", modellingRule="Mandatory", dataType=ns0_datypes.BrokerTransportQualityOfService, valueRank=-1
        )
    )
    resourceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15334", browseName="ResourceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=21145", browseName="NetworkAddressType", displayName="NetworkAddressType", isAbstract=True)
class NetworkAddressType(BaseObjectType):
    networkInterface: ns0_vartypes.SelectionListType


@o6.objecttype(nodeId="i=21147", browseName="NetworkAddressUrlType", displayName="NetworkAddressUrlType")
class NetworkAddressUrlType(NetworkAddressType):
    url: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=21149", browseName="Url", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=23455", browseName="AliasNameType", displayName="AliasNameType")
class AliasNameType(BaseObjectType):
    pass


ns0_vartypes.PropertyType(
    nodeId="i=23463",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=23462",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="AliasNameSearchPattern", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ReferenceTypeFilter", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=23464",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=23462",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="AliasNodeList", dataType=o6.NodeId("i=23468"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=23462", browseName="FindAlias", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=23463"]), outputArgs=o6.hasProperty(o6.ns["i=23464"]))


@o6.objecttype(nodeId="i=23513", browseName="IOrderedObjectType", displayName="IOrderedObjectType", isAbstract=True)
class IOrderedObjectType(BaseInterfaceType):
    numberInList: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23517", browseName="NumberInList", modellingRule="Mandatory", dataType=ns0_datypes.Number, valueRank=-1)
    )


@o6.objecttype(nodeId="i=23518", browseName="OrderedListType", displayName="OrderedListType")
class OrderedListType(BaseObjectType):
    nodeVersion: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23525", browseName="NodeVersion", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    orderedObject_: BaseObjectType | None


ns0_vartypes.PropertyType(
    nodeId="i=23527",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=23526",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Certificates", dataType=o6.NodeId("i=15"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=23526", browseName="GetRejectedList", modellingRule="Optional", outputArgs=o6.hasProperty(o6.ns["i=23527"]))


@o6.objecttype(nodeId="i=12555", browseName="CertificateGroupType", displayName="CertificateGroupType")
class CertificateGroupType(BaseObjectType):
    certificateExpired: CertificateExpirationAlarmType | None
    certificateTypes: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=13631", browseName="CertificateTypes", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    getRejectedList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=23526"])
    purpose: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19398", browseName="Purpose", modellingRule="Optional", dataType=o6.NodeId, valueRank=-1)
    )
    trustList: TrustListType
    trustListOutOfDate: TrustListOutOfDateAlarmType | None


@o6.objecttype(nodeId="i=23537", browseName="EccApplicationCertificateType", displayName="EccApplicationCertificateType", isAbstract=True)
class EccApplicationCertificateType(ApplicationCertificateType):
    pass


@o6.objecttype(nodeId="i=23538", browseName="EccNistP256ApplicationCertificateType", displayName="EccNistP256ApplicationCertificateType")
class EccNistP256ApplicationCertificateType(EccApplicationCertificateType):
    pass


@o6.objecttype(nodeId="i=23539", browseName="EccNistP384ApplicationCertificateType", displayName="EccNistP384ApplicationCertificateType")
class EccNistP384ApplicationCertificateType(EccApplicationCertificateType):
    pass


@o6.objecttype(nodeId="i=23540", browseName="EccBrainpoolP256r1ApplicationCertificateType", displayName="EccBrainpoolP256r1ApplicationCertificateType")
class EccBrainpoolP256r1ApplicationCertificateType(EccApplicationCertificateType):
    pass


@o6.objecttype(nodeId="i=23541", browseName="EccBrainpoolP384r1ApplicationCertificateType", displayName="EccBrainpoolP384r1ApplicationCertificateType")
class EccBrainpoolP384r1ApplicationCertificateType(EccApplicationCertificateType):
    pass


@o6.objecttype(nodeId="i=23542", browseName="EccCurve25519ApplicationCertificateType", displayName="EccCurve25519ApplicationCertificateType")
class EccCurve25519ApplicationCertificateType(EccApplicationCertificateType):
    pass


@o6.objecttype(nodeId="i=23543", browseName="EccCurve448ApplicationCertificateType", displayName="EccCurve448ApplicationCertificateType")
class EccCurve448ApplicationCertificateType(EccApplicationCertificateType):
    pass


@o6.objecttype(nodeId="i=23556", browseName="AuthorizationServicesConfigurationFolderType", displayName="AuthorizationServicesConfigurationFolderType")
class AuthorizationServicesConfigurationFolderType(FolderType):
    serviceName_: AuthorizationServiceConfigurationType | None


ns0_vartypes.PropertyType(
    nodeId="i=23812",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=23811",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SubscribedDataSet", dataType=o6.NodeId("i=23600"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=23813",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=23811",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SubscribedDataSetNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=23811", browseName="AddSubscribedDataSet", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=23812"]), outputArgs=o6.hasProperty(o6.ns["i=23813"]))

ns0_vartypes.PropertyType(
    nodeId="i=23815",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=23814",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SubscribedDataSetNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=23814", browseName="RemoveSubscribedDataSet", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=23815"]))

ns0_vartypes.PropertyType(
    nodeId="i=23817",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=23816",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=23818",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=23816",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetFolderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=23816", browseName="AddDataSetFolder", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=23817"]), outputArgs=o6.hasProperty(o6.ns["i=23818"]))

ns0_vartypes.PropertyType(
    nodeId="i=23820",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=23819",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DataSetFolderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=23819", browseName="RemoveDataSetFolder", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=23820"]))


@o6.objecttype(nodeId="i=23795", browseName="SubscribedDataSetFolderType", displayName="SubscribedDataSetFolderType")
class SubscribedDataSetFolderType(FolderType):
    addDataSetFolder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=23816"])
    addSubscribedDataSet: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=23811"])
    removeDataSetFolder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=23819"])
    removeSubscribedDataSet: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=23814"])
    standaloneSubscribedDataSetName_: StandaloneSubscribedDataSetType | None
    subscribedDataSetFolderName_: SubscribedDataSetFolderType | None


@o6.objecttype(nodeId="i=23828", browseName="StandaloneSubscribedDataSetType", displayName="StandaloneSubscribedDataSetType")
class StandaloneSubscribedDataSetType(BaseObjectType):
    dataSetMetaData: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23830", browseName="DataSetMetaData", modellingRule="Mandatory", dataType=ns0_datypes.DataSetMetaDataType, valueRank=-1)
    )
    isConnected: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23831", browseName="IsConnected", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    subscribedDataSet: SubscribedDataSetType = o6.hasComponent(SubscribedDataSetType(nodeId="i=23829", browseName="SubscribedDataSet", modellingRule="Mandatory"))


ns0_vartypes.PropertyType(
    nodeId="i=23964",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=23963",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="AliasNameSearchPattern", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ReferenceTypeFilter", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=23971",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=23963",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="AliasNodeList", dataType=o6.NodeId("i=24051"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=23963", browseName="FindAliasVerbose", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=23964"]), outputArgs=o6.hasProperty(o6.ns["i=23971"]))

ns0_vartypes.PropertyType(
    nodeId="i=23973",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=23972",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="AliasNames", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="TargetNodes", dataType=o6.NodeId("i=18"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="TargetServers", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="TargetReferenceType", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=23974",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=23972",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ErrorCodes", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=23972", browseName="AddAliasesToCategory", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=23973"]), outputArgs=o6.hasProperty(o6.ns["i=23974"]))

ns0_vartypes.PropertyType(
    nodeId="i=23976",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=23975",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="AliasNames", dataType=o6.NodeId("i=12"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="TargetNodes", dataType=o6.NodeId("i=18"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=23986",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=23975",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ErrorCodes", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=23975", browseName="DeleteAliasesFromCategory", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=23976"]), outputArgs=o6.hasProperty(o6.ns["i=23986"]))


@o6.objecttype(nodeId="i=15620", browseName="RoleType", displayName="RoleType")
class RoleType(BaseObjectType):
    addApplication: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16176"])
    addEndpoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16180"])
    addIdentity: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=15624"])
    applications: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16174", browseName="Applications", modellingRule="Optional", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    applicationsExclude: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15410", browseName="ApplicationsExclude", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1, accessLevel=3, userAccessLevel=1)
    )
    customConfiguration: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24139", browseName="CustomConfiguration", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    endpoints: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16175", browseName="Endpoints", modellingRule="Optional", dataType=ns0_datypes.EndpointType, valueRank=1, arrayDimensions=[0])
    )
    endpointsExclude: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15411", browseName="EndpointsExclude", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1, accessLevel=3, userAccessLevel=1)
    )
    identities: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=16173", browseName="Identities", modellingRule="Mandatory", dataType=ns0_datypes.IdentityMappingRuleType, valueRank=1, arrayDimensions=[0]
        )
    )
    removeApplication: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16178"])
    removeEndpoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16182"])
    removeIdentity: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=15626"])


@o6.objecttype(nodeId="i=24148", browseName="IIetfBaseNetworkInterfaceType", displayName="IIetfBaseNetworkInterfaceType", isAbstract=True)
class IIetfBaseNetworkInterfaceType(BaseInterfaceType):
    adminStatus: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24149", browseName="AdminStatus", modellingRule="Mandatory", dataType=ns0_datypes.InterfaceAdminStatus, valueRank=-1)
    )
    operStatus: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24150", browseName="OperStatus", modellingRule="Mandatory", dataType=ns0_datypes.InterfaceOperStatus, valueRank=-1)
    )
    physAddress: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24151", browseName="PhysAddress", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    speed: ns0_vartypes.AnalogUnitType


@o6.objecttype(nodeId="i=24158", browseName="IIeeeBaseEthernetPortType", displayName="IIeeeBaseEthernetPortType", isAbstract=True)
class IIeeeBaseEthernetPortType(BaseInterfaceType):
    duplex: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24165", browseName="Duplex", modellingRule="Mandatory", dataType=ns0_datypes.Duplex, valueRank=-1)
    )
    maxFrameLength: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24166", browseName="MaxFrameLength", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    speed: ns0_vartypes.AnalogUnitType


@o6.objecttype(nodeId="i=24167", browseName="IBaseEthernetCapabilitiesType", displayName="IBaseEthernetCapabilitiesType", isAbstract=True)
class IBaseEthernetCapabilitiesType(BaseInterfaceType):
    vlanTagCapable: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24168", browseName="VlanTagCapable", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24169", browseName="ISrClassType", displayName="ISrClassType", isAbstract=True)
class ISrClassType(BaseInterfaceType):
    id: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24170", browseName="Id", modellingRule="Mandatory", dataType=o6.Byte, valueRank=-1)
    )
    priority: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24171", browseName="Priority", modellingRule="Mandatory", dataType=o6.Byte, valueRank=-1)
    )
    vid: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24172", browseName="Vid", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24173", browseName="IIeeeBaseTsnStreamType", displayName="IIeeeBaseTsnStreamType", isAbstract=True)
class IIeeeBaseTsnStreamType(BaseInterfaceType):
    accumulatedLatency: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24177", browseName="AccumulatedLatency", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    srClassId: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24178", browseName="SrClassId", modellingRule="Optional", dataType=o6.Byte, valueRank=-1)
    )
    state: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24176", browseName="State", modellingRule="Mandatory", dataType=ns0_datypes.TsnStreamState, valueRank=-1)
    )
    streamId: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24174", browseName="StreamId", modellingRule="Mandatory", dataType=o6.Byte, valueRank=1, arrayDimensions=[8])
    )
    streamName: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24175", browseName="StreamName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24179", browseName="IIeeeBaseTsnTrafficSpecificationType", displayName="IIeeeBaseTsnTrafficSpecificationType", isAbstract=True)
class IIeeeBaseTsnTrafficSpecificationType(BaseInterfaceType):
    interval: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24182", browseName="Interval", modellingRule="Mandatory", dataType=ns0_datypes.UnsignedRationalNumber, valueRank=-1)
    )
    maxFrameSize: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24181", browseName="MaxFrameSize", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxIntervalFrames: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24180", browseName="MaxIntervalFrames", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24183", browseName="IIeeeBaseTsnStatusStreamType", displayName="IIeeeBaseTsnStatusStreamType", isAbstract=True)
class IIeeeBaseTsnStatusStreamType(BaseInterfaceType):
    failureCode: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24186", browseName="FailureCode", modellingRule="Mandatory", dataType=ns0_datypes.TsnFailureCode, valueRank=-1)
    )
    failureSystemIdentifier: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24187", browseName="FailureSystemIdentifier", modellingRule="Mandatory", dataType=o6.Byte, valueRank=2, arrayDimensions=[0, 8])
    )
    listenerStatus: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24185", browseName="ListenerStatus", modellingRule="Optional", dataType=ns0_datypes.TsnListenerStatus, valueRank=-1)
    )
    talkerStatus: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24184", browseName="TalkerStatus", modellingRule="Optional", dataType=ns0_datypes.TsnTalkerStatus, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24188", browseName="IIeeeTsnInterfaceConfigurationType", displayName="IIeeeTsnInterfaceConfigurationType", isAbstract=True)
class IIeeeTsnInterfaceConfigurationType(BaseInterfaceType):
    interfaceName: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24190", browseName="InterfaceName", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    macAddress: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24189", browseName="MacAddress", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24191", browseName="IIeeeTsnInterfaceConfigurationTalkerType", displayName="IIeeeTsnInterfaceConfigurationTalkerType", isAbstract=True)
class IIeeeTsnInterfaceConfigurationTalkerType(IIeeeTsnInterfaceConfigurationType):
    timeAwareOffset: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24194", browseName="TimeAwareOffset", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24195", browseName="IIeeeTsnInterfaceConfigurationListenerType", displayName="IIeeeTsnInterfaceConfigurationListenerType", isAbstract=True)
class IIeeeTsnInterfaceConfigurationListenerType(IIeeeTsnInterfaceConfigurationType):
    receiveOffset: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24198", browseName="ReceiveOffset", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24199", browseName="IIeeeTsnMacAddressType", displayName="IIeeeTsnMacAddressType", isAbstract=True)
class IIeeeTsnMacAddressType(BaseInterfaceType):
    destinationAddress: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24200", browseName="DestinationAddress", modellingRule="Mandatory", dataType=o6.Byte, valueRank=1, arrayDimensions=[6])
    )
    sourceAddress: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24201", browseName="SourceAddress", modellingRule="Optional", dataType=o6.Byte, valueRank=1, arrayDimensions=[6])
    )


@o6.objecttype(nodeId="i=24202", browseName="IIeeeTsnVlanTagType", displayName="IIeeeTsnVlanTagType", isAbstract=True)
class IIeeeTsnVlanTagType(BaseInterfaceType):
    priorityCodePoint: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24204", browseName="PriorityCodePoint", modellingRule="Mandatory", dataType=o6.Byte, valueRank=-1)
    )
    vlanId: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24203", browseName="VlanId", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24205", browseName="IPriorityMappingEntryType", displayName="IPriorityMappingEntryType", isAbstract=True)
class IPriorityMappingEntryType(BaseInterfaceType):
    mappingUri: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24206", browseName="MappingUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    priorityLabel: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24207", browseName="PriorityLabel", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    priorityValue_DSCP: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24209", browseName="PriorityValue_DSCP", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    priorityValue_PCP: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24208", browseName="PriorityValue_PCP", modellingRule="Optional", dataType=o6.Byte, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24233", browseName="IIeeeAutoNegotiationStatusType", displayName="IIeeeAutoNegotiationStatusType", isAbstract=True)
class IIeeeAutoNegotiationStatusType(BaseInterfaceType):
    negotiationStatus: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=24234", browseName="NegotiationStatus", modellingRule="Mandatory", dataType=ns0_datypes.NegotiationStatus, valueRank=-1)
    )


ns0_vartypes.PropertyType(
    nodeId="i=24270",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24269",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="UserName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Password", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="UserConfiguration", dataType=o6.NodeId("i=24279"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Description", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=24269", browseName="AddUser", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=24270"]))

ns0_vartypes.PropertyType(
    nodeId="i=24272",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24271",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0_datypes.Argument(name="UserName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ModifyPassword", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Password", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ModifyUserConfiguration", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="UserConfiguration", dataType=o6.NodeId("i=24279"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ModifyDescription", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Description", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=24271", browseName="ModifyUser", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=24272"]))

ns0_vartypes.PropertyType(
    nodeId="i=24274",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24273",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="UserName", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24273", browseName="RemoveUser", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=24274"]))

ns0_vartypes.PropertyType(
    nodeId="i=24276",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24275",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="OldPassword", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="NewPassword", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=24275", browseName="ChangePassword", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=24276"]))


@o6.objecttype(nodeId="i=24264", browseName="UserManagementType", displayName="UserManagementType")
class UserManagementType(BaseObjectType):
    addUser: o6.node.MethodNode = o6.hasComponent(o6.ns["i=24269"])
    changePassword: o6.node.MethodNode = o6.hasComponent(o6.ns["i=24275"])
    modifyUser: o6.node.MethodNode = o6.hasComponent(o6.ns["i=24271"])
    passwordLength: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24266", browseName="PasswordLength", modellingRule="Mandatory", dataType=ns0_datypes.Range, valueRank=-1)
    )
    passwordOptions: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24267", browseName="PasswordOptions", modellingRule="Mandatory", dataType=ns0_datypes.PasswordOptionsMask, valueRank=-1)
    )
    passwordRestrictions: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24268", browseName="PasswordRestrictions", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=-1)
    )
    removeUser: o6.node.MethodNode = o6.hasComponent(o6.ns["i=24273"])
    users: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24265", browseName="Users", modellingRule="Mandatory", dataType=ns0_datypes.UserManagementDataType, valueRank=1, arrayDimensions=[0])
    )


ns0_vartypes.PropertyType(
    nodeId="i=24313",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24312",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="SelectedResponse", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=24312", browseName="Respond2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24313"]))

ns0_vartypes.PropertyType(
    nodeId="i=24317",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24316",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24316", browseName="Suppress2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24317"]))

ns0_vartypes.PropertyType(
    nodeId="i=24319",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24318",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24318", browseName="Unsuppress2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24319"]))

ns0_vartypes.PropertyType(
    nodeId="i=24321",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24320",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24320", browseName="RemoveFromService2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24321"]))

ns0_vartypes.PropertyType(
    nodeId="i=24323",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24322",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24322", browseName="PlaceInService2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24323"]))

ns0_vartypes.PropertyType(
    nodeId="i=24325",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24324",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24324", browseName="Reset2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24325"]))

ns0_vartypes.PropertyType(
    nodeId="i=24373",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24372",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ContinuationPointIn", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24372", browseName="ReleaseContinuationPoint", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24373"]))


@o6.objecttype(nodeId="i=19352", browseName="LogObjectType", displayName="LogObjectType")
class LogObjectType(BaseObjectType):
    getRecords: o6.node.MethodNode = o6.hasComponent(o6.ns["i=19353"])
    maxRecords: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19356", browseName="MaxRecords", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxStorageDuration: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19357", browseName="MaxStorageDuration", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    minimumSeverity: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19744", browseName="MinimumSeverity", modellingRule="Optional", dataType=o6.UInt16, valueRank=-1)
    )
    releaseContinuationPoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24372"])


ns0_vartypes.PropertyType(
    nodeId="i=25154",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=24744",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Groups", dataType=o6.NodeId("i=17"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=24744", browseName="GetGroupMemberships", modellingRule="Optional", outputArgs=o6.hasProperty(o6.ns["i=25154"]))

ns0_vartypes.PropertyType(
    nodeId="i=24757",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24756",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="ShelvingTime", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=24756", browseName="TimedShelve2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24757"]))

ns0_vartypes.PropertyType(
    nodeId="i=24759",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24758",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24758", browseName="Unshelve2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24759"]))

ns0_vartypes.PropertyType(
    nodeId="i=24761",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=24760",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Comment", dataType=o6.NodeId("i=21"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=24760", browseName="OneShotShelve2", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=24761"]))


@o6.objecttype(nodeId="i=2929", browseName="ShelvedStateMachineType", displayName="ShelvedStateMachineType")
class ShelvedStateMachineType(FiniteStateMachineType):
    oneShotShelve: o6.node.MethodNode = o6.hasComponent(o6.ns["i=2948"])
    oneShotShelve2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24760"])
    oneShotShelved: StateType
    oneShotShelvedToTimedShelved: TransitionType
    oneShotShelvedToUnshelved: TransitionType
    timedShelve: o6.node.MethodNode = o6.hasComponent(o6.ns["i=2949"])
    timedShelve2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24756"])
    timedShelved: StateType
    timedShelvedToOneShotShelved: TransitionType
    timedShelvedToUnshelved: TransitionType
    unshelve: o6.node.MethodNode = o6.hasComponent(o6.ns["i=2947"])
    unshelve2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24758"])
    unshelveTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9115", browseName="UnshelveTime", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    unshelved: StateType
    unshelvedToOneShotShelved: TransitionType
    unshelvedToTimedShelved: TransitionType


@o6.objecttype(nodeId="i=11575", browseName="FileType", displayName="FileType")
class FileType(BaseObjectType):
    close: o6.node.MethodNode = o6.hasComponent(o6.ns["i=11583"])
    getPosition: o6.node.MethodNode = o6.hasComponent(o6.ns["i=11590"])
    lastModifiedTime: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25200", browseName="LastModifiedTime", modellingRule="Optional", dataType=o6.DateTime, valueRank=-1)
    )
    maxByteStringLength: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24244", browseName="MaxByteStringLength", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    mimeType: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=13341", browseName="MimeType", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    open: o6.node.MethodNode = o6.hasComponent(o6.ns["i=11580"])
    openCount: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11579", browseName="OpenCount", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    read: o6.node.MethodNode = o6.hasComponent(o6.ns["i=11585"])
    setPosition: o6.node.MethodNode = o6.hasComponent(o6.ns["i=11593"])
    size: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=11576", browseName="Size", modellingRule="Mandatory", dataType=o6.UInt64, valueRank=-1))
    userWritable: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12687", browseName="UserWritable", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    writable: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12686", browseName="Writable", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    write: o6.node.MethodNode = o6.hasComponent(o6.ns["i=11588"])


@o6.objecttype(nodeId="i=11595", browseName="AddressSpaceFileType", displayName="AddressSpaceFileType")
class AddressSpaceFileType(FileType):
    exportNamespace: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="i=11615", browseName="ExportNamespace", modellingRule="Optional"))


@o6.objecttype(nodeId="i=15437", browseName="ConfigurationFileType", displayName="ConfigurationFileType")
class ConfigurationFileType(FileType):
    activityTimeout: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15503", browseName="ActivityTimeout", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    closeAndUpdate: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15505"])
    confirmUpdate: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15508"])
    currentVersion: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15439", browseName="CurrentVersion", modellingRule="Mandatory", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )
    lastUpdateTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15438", browseName="LastUpdateTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    supportedDataType: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15504", browseName="SupportedDataType", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(nodeId="i=15550", browseName="ApplicationConfigurationFileType", displayName="ApplicationConfigurationFileType")
class ApplicationConfigurationFileType(ConfigurationFileType):
    availableNetworks: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15551", browseName="AvailableNetworks", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    availablePorts: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15552", browseName="AvailablePorts", modellingRule="Mandatory", dataType=ns0_datypes.NumericRange, valueRank=-1)
    )
    certificateGroupPurposes: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19416", browseName="CertificateGroupPurposes", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    certificateTypes: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15555", browseName="CertificateTypes", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    maxCertificateGroups: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19415", browseName="MaxCertificateGroups", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    maxEndpoints: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19414", browseName="MaxEndpoints", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    securityPolicyUris: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15553", browseName="SecurityPolicyUris", modellingRule="Mandatory", dataType=ns0_datypes.UriString, valueRank=1, arrayDimensions=[0])
    )
    userTokenTypes: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15554", browseName="UserTokenTypes", modellingRule="Mandatory", dataType=ns0_datypes.UserTokenPolicy, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="i=25218", browseName="IVlanIdType", displayName="IVlanIdType", isAbstract=True)
class IVlanIdType(BaseInterfaceType):
    vlanId: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=25219", browseName="VlanId", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )


BaseObjectType(nodeId="i=25226", browseName="<InterfaceName>", modellingRule="OptionalPlaceholder")
o6.reference(o6.ns["i=25226"], "i=17603", IIetfBaseNetworkInterfaceType)


@o6.objecttype(nodeId="i=25221", browseName="IetfBaseNetworkInterfaceType", displayName="IetfBaseNetworkInterfaceType", interfaces=[IIetfBaseNetworkInterfaceType])
class IetfBaseNetworkInterfaceType(BaseObjectType):
    adminStatus: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=25222", browseName="AdminStatus", modellingRule="Mandatory", dataType=ns0_datypes.InterfaceAdminStatus, valueRank=-1)
    )
    interfaceName_: BaseObjectType | None = o6.reference(o6.ns["i=25226"], "i=25238")
    operStatus: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=25223", browseName="OperStatus", modellingRule="Mandatory", dataType=ns0_datypes.InterfaceOperStatus, valueRank=-1)
    )
    physAddress: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=25224", browseName="PhysAddress", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    speed: ns0_vartypes.AnalogUnitType


ns0_vartypes.PropertyType(
    nodeId="i=25230",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25229",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="MappingUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="PriorityLabel", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="PriorityValue_PCP", dataType=o6.NodeId("i=3"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="PriorityValue_DSCP", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=25229", browseName="AddPriorityMappingEntry", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=25230"]))

ns0_vartypes.PropertyType(
    nodeId="i=25232",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25231",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="MappingUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="PriorityLabel", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
    ],
)
o6.call(nodeId="i=25231", browseName="DeletePriorityMappingEntry", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=25232"]))


@o6.objecttype(nodeId="i=25227", browseName="PriorityMappingTableType", displayName="PriorityMappingTableType")
class PriorityMappingTableType(BaseObjectType):
    addPriorityMappingEntry: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=25229"])
    deletePriorityMappingEntry: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=25231"])
    priorityMapppingEntries: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=25228", browseName="PriorityMapppingEntries", modellingRule="Mandatory", dataType=ns0_datypes.PriorityMappingEntryType, valueRank=1, arrayDimensions=[0]
        )
    )


ns0_vartypes.PropertyType(
    nodeId="i=25313",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25312",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=25314",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=25312",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SecurityGroupFolderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=25312", browseName="AddSecurityGroupFolder", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=25313"]), outputArgs=o6.hasProperty(o6.ns["i=25314"]))

ns0_vartypes.PropertyType(
    nodeId="i=25316",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25315",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SecurityGroupFolderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=25315", browseName="RemoveSecurityGroupFolder", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=25316"]))


@o6.objecttype(nodeId="i=15452", browseName="SecurityGroupFolderType", displayName="SecurityGroupFolderType")
class SecurityGroupFolderType(FolderType):
    addSecurityGroup: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15461"])
    addSecurityGroupFolder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=25312"])
    removeSecurityGroup: o6.node.MethodNode = o6.hasComponent(o6.ns["i=15464"])
    removeSecurityGroupFolder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=25315"])
    securityGroupFolderName_: SecurityGroupFolderType | None
    securityGroupName_: SecurityGroupType | None
    supportedSecurityPolicyUris: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25317", browseName="SupportedSecurityPolicyUris", modellingRule="Optional", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )


ns0_vartypes.PropertyType(
    nodeId="i=25367",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25366",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0_datypes.Argument(name="ApplicationUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="EndpointUrl", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="SecurityPolicyUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="UserTokenType", dataType=o6.NodeId("i=304"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RequestedKeyCount", dataType=o6.NodeId("i=5"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RetryInterval", dataType=o6.NodeId("i=290"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=25368",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=25366",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="PushTargetId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=25366", browseName="AddPushTarget", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=25367"]), outputArgs=o6.hasProperty(o6.ns["i=25368"]))

ns0_vartypes.PropertyType(
    nodeId="i=25370",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25369",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="PushTargetId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=25369", browseName="RemovePushTarget", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=25370"]))

ns0_vartypes.PropertyType(
    nodeId="i=25372",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25371",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=25373",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=25371",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="PushTargetFolderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=25371", browseName="AddPushTargetFolder", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=25372"]), outputArgs=o6.hasProperty(o6.ns["i=25373"]))

ns0_vartypes.PropertyType(
    nodeId="i=25375",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25374",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="PushTargetFolderNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
o6.call(nodeId="i=25374", browseName="RemovePushTargetFolder", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=25375"]))


@o6.objecttype(nodeId="i=25346", browseName="PubSubKeyPushTargetFolderType", displayName="PubSubKeyPushTargetFolderType")
class PubSubKeyPushTargetFolderType(FolderType):
    addPushTarget: o6.node.MethodNode = o6.hasComponent(o6.ns["i=25366"])
    addPushTargetFolder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=25371"])
    pushTargetFolderName_: PubSubKeyPushTargetFolderType | None
    pushTargetName_: PubSubKeyPushTargetType | None
    removePushTarget: o6.node.MethodNode = o6.hasComponent(o6.ns["i=25369"])
    removePushTargetFolder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=25374"])


ns0_vartypes.PropertyType(
    nodeId="i=25506",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25505",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0_datypes.Argument(name="TransportProfileUri", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="NumReqWriterGroupIds", dataType=o6.NodeId("i=5"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="NumReqDataSetWriterIds", dataType=o6.NodeId("i=5"), valueRank=-1, arrayDimensions=[]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=25507",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=25505",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0_datypes.Argument(name="DefaultPublisherId", dataType=o6.NodeId("i=24"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="WriterGroupIds", dataType=o6.NodeId("i=5"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="DataSetWriterIds", dataType=o6.NodeId("i=5"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="i=25505", browseName="ReserveIds", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=25506"]), outputArgs=o6.hasProperty(o6.ns["i=25507"]))

ns0_vartypes.PropertyType(
    nodeId="i=25509",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25508",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0_datypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="RequireCompleteUpdate", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ConfigurationReferences", dataType=o6.NodeId("i=25519"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0_vartypes.PropertyType(
    nodeId="i=25510",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=25508",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0_datypes.Argument(name="ChangesApplied", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[]),
        ns0_datypes.Argument(name="ReferencesResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="ConfigurationValues", dataType=o6.NodeId("i=25520"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="ConfigurationObjects", dataType=o6.NodeId("i=17"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="i=25508", browseName="CloseAndUpdate", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=25509"]), outputArgs=o6.hasProperty(o6.ns["i=25510"]))


@o6.objecttype(nodeId="i=25482", browseName="PubSubConfigurationType", displayName="PubSubConfigurationType")
class PubSubConfigurationType(FileType):
    closeAndUpdate: o6.node.MethodNode = o6.hasComponent(o6.ns["i=25508"])
    reserveIds: o6.node.MethodNode = o6.hasComponent(o6.ns["i=25505"])


@o6.objecttype(nodeId="i=14509", browseName="PublishedDataSetType", displayName="PublishedDataSetType")
class PublishedDataSetType(BaseObjectType):
    configurationVersion: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=14519", browseName="ConfigurationVersion", modellingRule="Mandatory", dataType=ns0_datypes.ConfigurationVersionDataType, valueRank=-1)
    )
    cyclicDataSet: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25521", browseName="CyclicDataSet", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    dataSetClassId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16759", browseName="DataSetClassId", modellingRule="Optional", dataType=o6.Guid, valueRank=-1)
    )
    dataSetMetaData: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15229", browseName="DataSetMetaData", modellingRule="Mandatory", dataType=ns0_datypes.DataSetMetaDataType, valueRank=-1)
    )
    dataSetWriterName_: DataSetWriterType | None
    extensionFields: ExtensionFieldsType | None


@o6.objecttype(nodeId="i=14534", browseName="PublishedDataItemsType", displayName="PublishedDataItemsType")
class PublishedDataItemsType(PublishedDataSetType):
    addVariables: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=14555"])
    publishedData: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=14548", browseName="PublishedData", modellingRule="Mandatory", dataType=ns0_datypes.PublishedVariableDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    removeVariables: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=14558"])


@o6.objecttype(nodeId="i=14572", browseName="PublishedEventsType", displayName="PublishedEventsType")
class PublishedEventsType(PublishedDataSetType):
    eventNotifier: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=14586", browseName="EventNotifier", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    filter: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=14588", browseName="Filter", modellingRule="Mandatory", dataType=ns0_datypes.ContentFilter, valueRank=-1)
    )
    modifyFieldSelection: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=15052"])
    selectedFields: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=14587", browseName="SelectedFields", modellingRule="Mandatory", dataType=ns0_datypes.SimpleAttributeOperand, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(nodeId="i=15064", browseName="DatagramConnectionTransportType", displayName="DatagramConnectionTransportType")
class DatagramConnectionTransportType(ConnectionTransportType):
    datagramQos: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25526", browseName="DatagramQos", modellingRule="Optional", dataType=ns0_datypes.QosDataType, valueRank=1, arrayDimensions=[0])
    )
    discoveryAddress: NetworkAddressType
    discoveryAnnounceRate: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23839", browseName="DiscoveryAnnounceRate", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    discoveryMaxMessageSize: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23840", browseName="DiscoveryMaxMessageSize", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    qosCategory: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25525", browseName="QosCategory", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=21133", browseName="DatagramWriterGroupTransportType", displayName="DatagramWriterGroupTransportType")
class DatagramWriterGroupTransportType(WriterGroupTransportType):
    address: NetworkAddressType | None
    datagramQos: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23847", browseName="DatagramQos", modellingRule="Optional", dataType=ns0_datypes.TransmitQosDataType, valueRank=1, arrayDimensions=[0])
    )
    discoveryAnnounceRate: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23848", browseName="DiscoveryAnnounceRate", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    messageRepeatCount: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21134", browseName="MessageRepeatCount", modellingRule="Optional", dataType=o6.Byte, valueRank=-1)
    )
    messageRepeatDelay: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=21135", browseName="MessageRepeatDelay", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    qosCategory: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25527", browseName="QosCategory", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    topic: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23849", browseName="Topic", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=24016", browseName="DatagramDataSetReaderTransportType", displayName="DatagramDataSetReaderTransportType")
class DatagramDataSetReaderTransportType(DataSetReaderTransportType):
    address: NetworkAddressType | None
    datagramQos: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24022", browseName="DatagramQos", modellingRule="Optional", dataType=ns0_datypes.ReceiveQosDataType, valueRank=1, arrayDimensions=[0])
    )
    qosCategory: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25528", browseName="QosCategory", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    topic: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24023", browseName="Topic", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=15471", browseName="SecurityGroupType", displayName="SecurityGroupType")
class SecurityGroupType(BaseObjectType):
    forceKeyRotation: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="i=25625", browseName="ForceKeyRotation", modellingRule="Optional"))
    invalidateKeys: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="i=25624", browseName="InvalidateKeys", modellingRule="Optional"))
    keyLifetime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15046", browseName="KeyLifetime", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    maxFutureKeyCount: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15048", browseName="MaxFutureKeyCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxPastKeyCount: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15056", browseName="MaxPastKeyCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    securityGroupId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15472", browseName="SecurityGroupId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    securityPolicyUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15047", browseName="SecurityPolicyUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


ns0_vartypes.PropertyType(
    nodeId="i=25642",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25641",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SecurityGroupIds", dataType=o6.NodeId("i=17"), valueRank=1, arrayDimensions=[0])],
)
ns0_vartypes.PropertyType(
    nodeId="i=25643",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=25641",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="ConnectResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=25641", browseName="ConnectSecurityGroups", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=25642"]), outputArgs=o6.hasProperty(o6.ns["i=25643"]))

ns0_vartypes.PropertyType(
    nodeId="i=25645",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=25644",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="SecurityGroupIds", dataType=o6.NodeId("i=17"), valueRank=1, arrayDimensions=[0])],
)
ns0_vartypes.PropertyType(
    nodeId="i=25646",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=25644",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="DisconnectResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=25644", browseName="DisconnectSecurityGroups", modellingRule="Mandatory", inputArgs=o6.hasProperty(o6.ns["i=25645"]), outputArgs=o6.hasProperty(o6.ns["i=25646"]))


@o6.objecttype(nodeId="i=25337", browseName="PubSubKeyPushTargetType", displayName="PubSubKeyPushTargetType")
class PubSubKeyPushTargetType(BaseObjectType):
    applicationUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25634", browseName="ApplicationUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    connectSecurityGroups: o6.node.MethodNode = o6.hasComponent(o6.ns["i=25641"])
    disconnectSecurityGroups: o6.node.MethodNode = o6.hasComponent(o6.ns["i=25644"])
    endpointUrl: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25635", browseName="EndpointUrl", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    lastPushErrorTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25640", browseName="LastPushErrorTime", modellingRule="Mandatory", dataType=o6.DateTime, valueRank=-1)
    )
    lastPushExecutionTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25639", browseName="LastPushExecutionTime", modellingRule="Mandatory", dataType=o6.DateTime, valueRank=-1)
    )
    requestedKeyCount: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25637", browseName="RequestedKeyCount", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    retryInterval: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25638", browseName="RetryInterval", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    securityGroupName_: SecurityGroupType | None
    securityPolicyUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25340", browseName="SecurityPolicyUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    triggerKeyUpdate: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="i=25647", browseName="TriggerKeyUpdate", modellingRule="Mandatory"))
    userTokenType: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25636", browseName="UserTokenType", modellingRule="Mandatory", dataType=ns0_datypes.UserTokenPolicy, valueRank=-1)
    )


ns0_vartypes.PropertyType(
    nodeId="i=26874",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=26873",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Tickets", dataType=o6.NodeId("i=25726"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=26873", browseName="RequestTickets", modellingRule="Mandatory", outputArgs=o6.hasProperty(o6.ns["i=26874"]))

ns0_vartypes.PropertyType(
    nodeId="i=26876",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=26875",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="Registrars", dataType=o6.NodeId("i=308"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="i=26875", browseName="SetRegistrarEndpoints", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=26876"]))


@o6.objecttype(nodeId="i=26871", browseName="ProvisionableDeviceType", displayName="ProvisionableDeviceType")
class ProvisionableDeviceType(BaseObjectType):
    applicationName_: ApplicationConfigurationType | None
    isSingleton: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=26872", browseName="IsSingleton", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    requestTickets: o6.node.MethodNode = o6.hasComponent(o6.ns["i=26873"])
    setRegistrarEndpoints: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=26875"])


@o6.objecttype(nodeId="i=2013", browseName="ServerCapabilitiesType", displayName="ServerCapabilitiesType")
class ServerCapabilitiesType(BaseObjectType):
    aggregateFunctions: FolderType = o6.hasComponent(FolderType(nodeId="i=2754", browseName="AggregateFunctions", modellingRule="Mandatory"))
    conformanceUnits: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24094", browseName="ConformanceUnits", modellingRule="Optional", dataType=o6.QualifiedName, valueRank=1, arrayDimensions=[0])
    )
    localeIdArray: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2016", browseName="LocaleIdArray", modellingRule="Mandatory", dataType=ns0_datypes.LocaleId, valueRank=1, arrayDimensions=[0])
    )
    maxArrayLength: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11549", browseName="MaxArrayLength", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxBrowseContinuationPoints: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2732", browseName="MaxBrowseContinuationPoints", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    maxByteStringLength: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12910", browseName="MaxByteStringLength", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxHistoryContinuationPoints: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2734", browseName="MaxHistoryContinuationPoints", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    maxLogObjectContinuationPoints: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19809", browseName="MaxLogObjectContinuationPoints", modellingRule="Optional", dataType=o6.UInt16, valueRank=-1)
    )
    maxMonitoredItems: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24090", browseName="MaxMonitoredItems", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxMonitoredItemsPerSubscription: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24103", browseName="MaxMonitoredItemsPerSubscription", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxMonitoredItemsQueueSize: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=31770", browseName="MaxMonitoredItemsQueueSize", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxQueryContinuationPoints: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2733", browseName="MaxQueryContinuationPoints", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    maxSelectClauseParameters: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24092", browseName="MaxSelectClauseParameters", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxSessions: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24088", browseName="MaxSessions", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxStringLength: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11550", browseName="MaxStringLength", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxSubscriptions: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24089", browseName="MaxSubscriptions", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxSubscriptionsPerSession: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24091", browseName="MaxSubscriptionsPerSession", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxWhereClauseParameters: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24093", browseName="MaxWhereClauseParameters", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    minSupportedSampleRate: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2017", browseName="MinSupportedSampleRate", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    modellingRules: FolderType = o6.hasComponent(FolderType(nodeId="i=2019", browseName="ModellingRules", modellingRule="Mandatory"))
    operationLimits: OperationLimitsType | None = o6.hasComponent(OperationLimitsType(nodeId="i=11551", browseName="OperationLimits", modellingRule="Optional"))
    roleSet: RoleSetType | None
    serverProfileArray: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2014", browseName="ServerProfileArray", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    softwareCertificates: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=3049", browseName="SoftwareCertificates", modellingRule="Mandatory", dataType=ns0_datypes.SignedSoftwareCertificate, valueRank=1, arrayDimensions=[0]
        )
    )
    vendorCapability_: ns0_vartypes.ServerVendorCapabilityType | None = o6.hasComponent(
        ns0_vartypes.ServerVendorCapabilityType(nodeId="i=11562", browseName="<VendorCapability>", modellingRule="OptionalPlaceholder", _allow_abstract=True, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2041", browseName="BaseEventType", displayName="BaseEventType", isAbstract=True)
class BaseEventType(BaseObjectType):
    conditionClassId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=31771", browseName="ConditionClassId", modellingRule="Optional", dataType=o6.NodeId, valueRank=-1)
    )
    conditionClassName: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=31772", browseName="ConditionClassName", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=-1)
    )
    conditionSubClassId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=31773", browseName="ConditionSubClassId", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    conditionSubClassName: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=31774", browseName="ConditionSubClassName", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )
    eventId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2042", browseName="EventId", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )
    eventType: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2043", browseName="EventType", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    localTime: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3190", browseName="LocalTime", modellingRule="Optional", dataType=ns0_datypes.TimeZoneDataType, valueRank=-1)
    )
    message: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2050", browseName="Message", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    receiveTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2047", browseName="ReceiveTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    severity: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2051", browseName="Severity", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    sourceName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2045", browseName="SourceName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    sourceNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2044", browseName="SourceNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    time: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2046", browseName="Time", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2052",
    browseName="AuditEventType",
    displayName="AuditEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditEventType(BaseEventType):
    actionTimeStamp: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2053", browseName="ActionTimeStamp", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    clientApplicationUri: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19811", browseName="ClientApplicationUri", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    clientAuditEntryId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2056", browseName="ClientAuditEntryId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    clientUserId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2057", browseName="ClientUserId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    serverId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2055", browseName="ServerId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    status: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2054", browseName="Status", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2058",
    browseName="AuditSecurityEventType",
    displayName="AuditSecurityEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditSecurityEventType(AuditEventType):
    statusCodeId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17615", browseName="StatusCodeId", modellingRule="Optional", dataType=o6.StatusCode, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2059",
    browseName="AuditChannelEventType",
    displayName="AuditChannelEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditChannelEventType(AuditSecurityEventType):
    secureChannelId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2745", browseName="SecureChannelId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2060",
    browseName="AuditOpenSecureChannelEventType",
    displayName="AuditOpenSecureChannelEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditOpenSecureChannelEventType(AuditChannelEventType):
    certificateErrorEventId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24135", browseName="CertificateErrorEventId", modellingRule="Optional", dataType=o6.ByteString, valueRank=-1)
    )
    clientCertificate: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2061", browseName="ClientCertificate", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )
    clientCertificateThumbprint: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2746", browseName="ClientCertificateThumbprint", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    requestType: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2062", browseName="RequestType", modellingRule="Mandatory", dataType=ns0_datypes.SecurityTokenRequestType, valueRank=-1)
    )
    requestedLifetime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2066", browseName="RequestedLifetime", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    securityMode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2065", browseName="SecurityMode", modellingRule="Mandatory", dataType=ns0_datypes.MessageSecurityMode, valueRank=-1)
    )
    securityPolicyUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2063", browseName="SecurityPolicyUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2069",
    browseName="AuditSessionEventType",
    displayName="AuditSessionEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditSessionEventType(AuditSecurityEventType):
    sessionId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2070", browseName="SessionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2071",
    browseName="AuditCreateSessionEventType",
    displayName="AuditCreateSessionEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCreateSessionEventType(AuditSessionEventType):
    clientCertificate: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2073", browseName="ClientCertificate", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )
    clientCertificateThumbprint: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2747", browseName="ClientCertificateThumbprint", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    revisedSessionTimeout: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2074", browseName="RevisedSessionTimeout", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    secureChannelId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2072", browseName="SecureChannelId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2075",
    browseName="AuditActivateSessionEventType",
    displayName="AuditActivateSessionEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditActivateSessionEventType(AuditSessionEventType):
    clientSoftwareCertificates: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=2076", browseName="ClientSoftwareCertificates", modellingRule="Mandatory", dataType=ns0_datypes.SignedSoftwareCertificate, valueRank=1, arrayDimensions=[0]
        )
    )
    currentRoleIds: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19304", browseName="CurrentRoleIds", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    secureChannelId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11485", browseName="SecureChannelId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    userIdentityToken: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2077", browseName="UserIdentityToken", modellingRule="Mandatory", dataType=ns0_datypes.UserIdentityToken, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2078",
    browseName="AuditCancelEventType",
    displayName="AuditCancelEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCancelEventType(AuditSessionEventType):
    requestHandle: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2079", browseName="RequestHandle", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2080",
    browseName="AuditCertificateEventType",
    displayName="AuditCertificateEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCertificateEventType(AuditSecurityEventType):
    certificate: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2081", browseName="Certificate", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2082",
    browseName="AuditCertificateDataMismatchEventType",
    displayName="AuditCertificateDataMismatchEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCertificateDataMismatchEventType(AuditCertificateEventType):
    invalidHostname: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2083", browseName="InvalidHostname", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    invalidUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2084", browseName="InvalidUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2085",
    browseName="AuditCertificateExpiredEventType",
    displayName="AuditCertificateExpiredEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCertificateExpiredEventType(AuditCertificateEventType):
    pass


@o6.objecttype(
    nodeId="i=2086",
    browseName="AuditCertificateInvalidEventType",
    displayName="AuditCertificateInvalidEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCertificateInvalidEventType(AuditCertificateEventType):
    pass


@o6.objecttype(
    nodeId="i=2087",
    browseName="AuditCertificateUntrustedEventType",
    displayName="AuditCertificateUntrustedEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCertificateUntrustedEventType(AuditCertificateEventType):
    pass


@o6.objecttype(
    nodeId="i=2088",
    browseName="AuditCertificateRevokedEventType",
    displayName="AuditCertificateRevokedEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCertificateRevokedEventType(AuditCertificateEventType):
    pass


@o6.objecttype(
    nodeId="i=2089",
    browseName="AuditCertificateMismatchEventType",
    displayName="AuditCertificateMismatchEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditCertificateMismatchEventType(AuditCertificateEventType):
    pass


@o6.objecttype(
    nodeId="i=2090",
    browseName="AuditNodeManagementEventType",
    displayName="AuditNodeManagementEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditNodeManagementEventType(AuditEventType):
    pass


@o6.objecttype(
    nodeId="i=2091",
    browseName="AuditAddNodesEventType",
    displayName="AuditAddNodesEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditAddNodesEventType(AuditNodeManagementEventType):
    nodesToAdd: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2092", browseName="NodesToAdd", modellingRule="Mandatory", dataType=ns0_datypes.AddNodesItem, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(
    nodeId="i=2093",
    browseName="AuditDeleteNodesEventType",
    displayName="AuditDeleteNodesEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditDeleteNodesEventType(AuditNodeManagementEventType):
    nodesToDelete: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2094", browseName="NodesToDelete", modellingRule="Mandatory", dataType=ns0_datypes.DeleteNodesItem, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(
    nodeId="i=2095",
    browseName="AuditAddReferencesEventType",
    displayName="AuditAddReferencesEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditAddReferencesEventType(AuditNodeManagementEventType):
    referencesToAdd: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=2096", browseName="ReferencesToAdd", modellingRule="Mandatory", dataType=ns0_datypes.AddReferencesItem, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(
    nodeId="i=2097",
    browseName="AuditDeleteReferencesEventType",
    displayName="AuditDeleteReferencesEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditDeleteReferencesEventType(AuditNodeManagementEventType):
    referencesToDelete: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=2098", browseName="ReferencesToDelete", modellingRule="Mandatory", dataType=ns0_datypes.DeleteReferencesItem, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(
    nodeId="i=2099",
    browseName="AuditUpdateEventType",
    displayName="AuditUpdateEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditUpdateEventType(AuditEventType):
    pass


@o6.objecttype(
    nodeId="i=2100",
    browseName="AuditWriteUpdateEventType",
    displayName="AuditWriteUpdateEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditWriteUpdateEventType(AuditUpdateEventType):
    attributeId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2750", browseName="AttributeId", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    indexRange: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2101", browseName="IndexRange", modellingRule="Mandatory", dataType=ns0_datypes.NumericRange, valueRank=-1)
    )
    newValue: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=2103", browseName="NewValue", modellingRule="Mandatory", valueRank=-1))
    oldValue: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=2102", browseName="OldValue", modellingRule="Mandatory", valueRank=-1))


@o6.objecttype(
    nodeId="i=2104",
    browseName="AuditHistoryUpdateEventType",
    displayName="AuditHistoryUpdateEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryUpdateEventType(AuditUpdateEventType):
    parameterDataTypeId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2751", browseName="ParameterDataTypeId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=2127",
    browseName="AuditUpdateMethodEventType",
    displayName="AuditUpdateMethodEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditUpdateMethodEventType(AuditEventType):
    inputArguments: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2129", browseName="InputArguments", modellingRule="Mandatory", valueRank=1, arrayDimensions=[0])
    )
    methodId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2128", browseName="MethodId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    outputArguments: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19306", browseName="OutputArguments", modellingRule="Optional", valueRank=1, arrayDimensions=[0])
    )
    statusCodeId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19305", browseName="StatusCodeId", modellingRule="Optional", dataType=o6.StatusCode, valueRank=-1)
    )


o6.reference(o6.ns["i=18666"], "i=3065", AuditUpdateMethodEventType)


@o6.objecttype(nodeId="i=2130", browseName="SystemEventType", displayName="SystemEventType", isAbstract=True)
class SystemEventType(BaseEventType):
    pass


@o6.objecttype(nodeId="i=2131", browseName="DeviceFailureEventType", displayName="DeviceFailureEventType", isAbstract=True)
class DeviceFailureEventType(SystemEventType):
    pass


@o6.objecttype(nodeId="i=2132", browseName="BaseModelChangeEventType", displayName="BaseModelChangeEventType", isAbstract=True)
class BaseModelChangeEventType(BaseEventType):
    pass


@o6.objecttype(nodeId="i=2133", browseName="GeneralModelChangeEventType", displayName="GeneralModelChangeEventType", isAbstract=True)
class GeneralModelChangeEventType(BaseModelChangeEventType):
    changes: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=2134", browseName="Changes", modellingRule="Mandatory", dataType=ns0_datypes.ModelChangeStructureDataType, valueRank=1, arrayDimensions=[0]
        )
    )


o6.reference(OrderedListType, "i=41", GeneralModelChangeEventType)


@o6.objecttype(nodeId="i=2311", browseName="TransitionEventType", displayName="TransitionEventType", isAbstract=True)
class TransitionEventType(BaseEventType):
    fromState: ns0_vartypes.StateVariableType
    toState: ns0_vartypes.StateVariableType
    transition: ns0_vartypes.TransitionVariableType


@o6.objecttype(
    nodeId="i=2315",
    browseName="AuditUpdateStateEventType",
    displayName="AuditUpdateStateEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditUpdateStateEventType(AuditUpdateMethodEventType):
    newStateId: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=2778", browseName="NewStateId", modellingRule="Mandatory", valueRank=-1))
    oldStateId: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=2777", browseName="OldStateId", modellingRule="Mandatory", valueRank=-1))


@o6.objecttype(nodeId="i=2378", browseName="ProgramTransitionEventType", displayName="ProgramTransitionEventType", isAbstract=True)
class ProgramTransitionEventType(TransitionEventType):
    intermediateResult: ns0_vartypes.BaseDataVariableType = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=2379", browseName="IntermediateResult", modellingRule="Mandatory", valueRank=-1)
    )


@o6.objecttype(nodeId="i=2738", browseName="SemanticChangeEventType", displayName="SemanticChangeEventType", isAbstract=True)
class SemanticChangeEventType(BaseEventType):
    changes: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=2739", browseName="Changes", modellingRule="Mandatory", dataType=ns0_datypes.SemanticChangeStructureDataType, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(
    nodeId="i=2748",
    browseName="AuditUrlMismatchEventType",
    displayName="AuditUrlMismatchEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditUrlMismatchEventType(AuditCreateSessionEventType):
    endpointUrl: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2749", browseName="EndpointUrl", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2787", browseName="RefreshStartEventType", displayName="RefreshStartEventType", isAbstract=True)
class RefreshStartEventType(SystemEventType):
    pass


o6.reference(o6.ns["i=3875"], "i=3065", RefreshStartEventType)
o6.reference(o6.ns["i=12912"], "i=3065", RefreshStartEventType)


@o6.objecttype(nodeId="i=2788", browseName="RefreshEndEventType", displayName="RefreshEndEventType", isAbstract=True)
class RefreshEndEventType(SystemEventType):
    pass


o6.reference(o6.ns["i=3875"], "i=3065", RefreshEndEventType)
o6.reference(o6.ns["i=12912"], "i=3065", RefreshEndEventType)


@o6.objecttype(nodeId="i=2789", browseName="RefreshRequiredEventType", displayName="RefreshRequiredEventType", isAbstract=True)
class RefreshRequiredEventType(SystemEventType):
    pass


@o6.objecttype(
    nodeId="i=2790",
    browseName="AuditConditionEventType",
    displayName="AuditConditionEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionEventType(AuditUpdateMethodEventType):
    pass


@o6.objecttype(
    nodeId="i=2803",
    browseName="AuditConditionEnableEventType",
    displayName="AuditConditionEnableEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionEnableEventType(AuditConditionEventType):
    pass


o6.reference(o6.ns["i=9027"], "i=3065", AuditConditionEnableEventType)
o6.reference(o6.ns["i=9028"], "i=3065", AuditConditionEnableEventType)


@o6.objecttype(
    nodeId="i=2829",
    browseName="AuditConditionCommentEventType",
    displayName="AuditConditionCommentEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionCommentEventType(AuditConditionEventType):
    comment: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11851", browseName="Comment", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    conditionEventId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17222", browseName="ConditionEventId", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )


o6.reference(o6.ns["i=9029"], "i=3065", AuditConditionCommentEventType)


@o6.objecttype(
    nodeId="i=2999",
    browseName="AuditHistoryEventUpdateEventType",
    displayName="AuditHistoryEventUpdateEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryEventUpdateEventType(AuditHistoryUpdateEventType):
    filter: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3003", browseName="Filter", modellingRule="Mandatory", dataType=ns0_datypes.EventFilter, valueRank=-1)
    )
    newValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3029", browseName="NewValues", modellingRule="Mandatory", dataType=ns0_datypes.HistoryEventFieldList, valueRank=1, arrayDimensions=[0])
    )
    oldValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3030", browseName="OldValues", modellingRule="Mandatory", dataType=ns0_datypes.HistoryEventFieldList, valueRank=1, arrayDimensions=[0])
    )
    performInsertReplace: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3028", browseName="PerformInsertReplace", modellingRule="Mandatory", dataType=ns0_datypes.PerformUpdateType, valueRank=-1)
    )
    updatedNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3025", browseName="UpdatedNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=3006",
    browseName="AuditHistoryValueUpdateEventType",
    displayName="AuditHistoryValueUpdateEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryValueUpdateEventType(AuditHistoryUpdateEventType):
    newValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3032", browseName="NewValues", modellingRule="Mandatory", dataType=o6.DataValue, valueRank=1, arrayDimensions=[0])
    )
    oldValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3033", browseName="OldValues", modellingRule="Mandatory", dataType=o6.DataValue, valueRank=1, arrayDimensions=[0])
    )
    performInsertReplace: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3031", browseName="PerformInsertReplace", modellingRule="Mandatory", dataType=ns0_datypes.PerformUpdateType, valueRank=-1)
    )
    updatedNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3026", browseName="UpdatedNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=3012",
    browseName="AuditHistoryDeleteEventType",
    displayName="AuditHistoryDeleteEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryDeleteEventType(AuditHistoryUpdateEventType):
    updatedNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3027", browseName="UpdatedNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=3014",
    browseName="AuditHistoryRawModifyDeleteEventType",
    displayName="AuditHistoryRawModifyDeleteEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryRawModifyDeleteEventType(AuditHistoryDeleteEventType):
    endTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3017", browseName="EndTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    isDeleteModified: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3015", browseName="IsDeleteModified", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    oldValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3034", browseName="OldValues", modellingRule="Mandatory", dataType=o6.DataValue, valueRank=1, arrayDimensions=[0])
    )
    startTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3016", browseName="StartTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=3019",
    browseName="AuditHistoryAtTimeDeleteEventType",
    displayName="AuditHistoryAtTimeDeleteEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryAtTimeDeleteEventType(AuditHistoryDeleteEventType):
    oldValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3021", browseName="OldValues", modellingRule="Mandatory", dataType=o6.DataValue, valueRank=1, arrayDimensions=[0])
    )
    reqTimes: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3020", browseName="ReqTimes", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(
    nodeId="i=3022",
    browseName="AuditHistoryEventDeleteEventType",
    displayName="AuditHistoryEventDeleteEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryEventDeleteEventType(AuditHistoryDeleteEventType):
    eventIds: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3023", browseName="EventIds", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=1, arrayDimensions=[0])
    )
    oldValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3024", browseName="OldValues", modellingRule="Mandatory", dataType=ns0_datypes.HistoryEventFieldList, valueRank=-1)
    )


@o6.objecttype(nodeId="i=3035", browseName="EventQueueOverflowEventType", displayName="EventQueueOverflowEventType", isAbstract=True)
class EventQueueOverflowEventType(BaseEventType):
    pass


@o6.objecttype(nodeId="i=3806", browseName="ProgramTransitionAuditEventType", displayName="ProgramTransitionAuditEventType")
class ProgramTransitionAuditEventType(AuditUpdateStateEventType):
    transition: ns0_vartypes.FiniteTransitionVariableType


@o6.objecttype(
    nodeId="i=8927",
    browseName="AuditConditionRespondEventType",
    displayName="AuditConditionRespondEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionRespondEventType(AuditConditionEventType):
    selectedResponse: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11852", browseName="SelectedResponse", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


o6.reference(o6.ns["i=9069"], "i=3065", AuditConditionRespondEventType)
o6.reference(o6.ns["i=24312"], "i=3065", AuditConditionRespondEventType)


@o6.objecttype(
    nodeId="i=8944",
    browseName="AuditConditionAcknowledgeEventType",
    displayName="AuditConditionAcknowledgeEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionAcknowledgeEventType(AuditConditionEventType):
    comment: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11853", browseName="Comment", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    conditionEventId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17223", browseName="ConditionEventId", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )


o6.reference(o6.ns["i=9111"], "i=3065", AuditConditionAcknowledgeEventType)


@o6.objecttype(
    nodeId="i=8961",
    browseName="AuditConditionConfirmEventType",
    displayName="AuditConditionConfirmEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionConfirmEventType(AuditConditionEventType):
    comment: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11854", browseName="Comment", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    conditionEventId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17224", browseName="ConditionEventId", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )


o6.reference(o6.ns["i=9113"], "i=3065", AuditConditionConfirmEventType)


@o6.objecttype(
    nodeId="i=11093",
    browseName="AuditConditionShelvingEventType",
    displayName="AuditConditionShelvingEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionShelvingEventType(AuditConditionEventType):
    shelvingTime: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11855", browseName="ShelvingTime", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )


o6.reference(o6.ns["i=2947"], "i=3065", AuditConditionShelvingEventType)
o6.reference(o6.ns["i=2948"], "i=3065", AuditConditionShelvingEventType)
o6.reference(o6.ns["i=2949"], "i=3065", AuditConditionShelvingEventType)
o6.reference(o6.ns["i=24756"], "i=3065", AuditConditionShelvingEventType)
o6.reference(o6.ns["i=24758"], "i=3065", AuditConditionShelvingEventType)
o6.reference(o6.ns["i=24760"], "i=3065", AuditConditionShelvingEventType)


@o6.objecttype(nodeId="i=11436", browseName="ProgressEventType", displayName="ProgressEventType", isAbstract=True)
class ProgressEventType(BaseEventType):
    context: ns0_vartypes.PropertyType = o6.hasProperty(ns0_vartypes.PropertyType(nodeId="i=12502", browseName="Context", modellingRule="Mandatory", valueRank=-1))
    progress: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12503", browseName="Progress", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )


@o6.objecttype(nodeId="i=11446", browseName="SystemStatusChangeEventType", displayName="SystemStatusChangeEventType", isAbstract=True)
class SystemStatusChangeEventType(SystemEventType):
    systemState: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11696", browseName="SystemState", modellingRule="Mandatory", dataType=ns0_datypes.ServerState, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=11856",
    browseName="AuditProgramTransitionEventType",
    displayName="AuditProgramTransitionEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditProgramTransitionEventType(AuditUpdateStateEventType):
    transitionNumber: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11875", browseName="TransitionNumber", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(nodeId="i=12620", browseName="CertificateUpdatedAuditEventType", displayName="CertificateUpdatedAuditEventType", isAbstract=True)
class CertificateUpdatedAuditEventType(AuditUpdateMethodEventType):
    certificateGroup: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=13735", browseName="CertificateGroup", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    certificateType: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=13736", browseName="CertificateType", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=15013",
    browseName="AuditConditionResetEventType",
    displayName="AuditConditionResetEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionResetEventType(AuditConditionEventType):
    pass


o6.reference(o6.ns["i=18199"], "i=3065", AuditConditionResetEventType)
o6.reference(o6.ns["i=24324"], "i=3065", AuditConditionResetEventType)


@o6.objecttype(nodeId="i=15535", browseName="PubSubStatusEventType", displayName="PubSubStatusEventType", isAbstract=True)
class PubSubStatusEventType(SystemEventType):
    connectionId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15545", browseName="ConnectionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    groupId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15546", browseName="GroupId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    state: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15547", browseName="State", modellingRule="Mandatory", dataType=ns0_datypes.PubSubState, valueRank=-1)
    )


@o6.objecttype(nodeId="i=15541", browseName="ConfigurationUpdatedAuditEventType", displayName="ConfigurationUpdatedAuditEventType", isAbstract=True)
class ConfigurationUpdatedAuditEventType(AuditEventType):
    newVersion: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15543", browseName="NewVersion", modellingRule="Mandatory", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )
    oldVersion: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15542", browseName="OldVersion", modellingRule="Mandatory", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )


@o6.objecttype(nodeId="i=15548", browseName="PubSubTransportLimitsExceedEventType", displayName="PubSubTransportLimitsExceedEventType", isAbstract=True)
class PubSubTransportLimitsExceedEventType(PubSubStatusEventType):
    actual: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15561", browseName="Actual", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maximum: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15562", browseName="Maximum", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.objecttype(nodeId="i=15563", browseName="PubSubCommunicationFailureEventType", displayName="PubSubCommunicationFailureEventType", isAbstract=True)
class PubSubCommunicationFailureEventType(PubSubStatusEventType):
    error: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=15576", browseName="Error", modellingRule="Mandatory", dataType=o6.StatusCode, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=17225",
    browseName="AuditConditionSuppressionEventType",
    displayName="AuditConditionSuppressionEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionSuppressionEventType(AuditConditionEventType):
    pass


o6.reference(o6.ns["i=16403"], "i=3065", AuditConditionSuppressionEventType)
o6.reference(o6.ns["i=17868"], "i=3065", AuditConditionSuppressionEventType)
o6.reference(o6.ns["i=24316"], "i=3065", AuditConditionSuppressionEventType)
o6.reference(o6.ns["i=24318"], "i=3065", AuditConditionSuppressionEventType)


@o6.objecttype(
    nodeId="i=17242",
    browseName="AuditConditionSilenceEventType",
    displayName="AuditConditionSilenceEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionSilenceEventType(AuditConditionEventType):
    pass


o6.reference(o6.ns["i=16402"], "i=3065", AuditConditionSilenceEventType)


@o6.objecttype(
    nodeId="i=17259",
    browseName="AuditConditionOutOfServiceEventType",
    displayName="AuditConditionOutOfServiceEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
)
class AuditConditionOutOfServiceEventType(AuditConditionEventType):
    pass


o6.reference(o6.ns["i=17869"], "i=3065", AuditConditionOutOfServiceEventType)
o6.reference(o6.ns["i=17870"], "i=3065", AuditConditionOutOfServiceEventType)
o6.reference(o6.ns["i=24320"], "i=3065", AuditConditionOutOfServiceEventType)
o6.reference(o6.ns["i=24322"], "i=3065", AuditConditionOutOfServiceEventType)


@o6.objecttype(nodeId="i=17641", browseName="RoleMappingRuleChangedAuditEventType", displayName="RoleMappingRuleChangedAuditEventType", isAbstract=True)
class RoleMappingRuleChangedAuditEventType(AuditUpdateMethodEventType):
    pass


@o6.objecttype(nodeId="i=18011", browseName="KeyCredentialAuditEventType", displayName="KeyCredentialAuditEventType", isAbstract=True)
class KeyCredentialAuditEventType(AuditUpdateMethodEventType):
    resourceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18028", browseName="ResourceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=18029", browseName="KeyCredentialUpdatedAuditEventType", displayName="KeyCredentialUpdatedAuditEventType")
class KeyCredentialUpdatedAuditEventType(KeyCredentialAuditEventType):
    pass


@o6.objecttype(nodeId="i=18047", browseName="KeyCredentialDeletedAuditEventType", displayName="KeyCredentialDeletedAuditEventType")
class KeyCredentialDeletedAuditEventType(KeyCredentialAuditEventType):
    resourceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18064", browseName="ResourceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=19095",
    browseName="AuditHistoryAnnotationUpdateEventType",
    displayName="AuditHistoryAnnotationUpdateEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryAnnotationUpdateEventType(AuditHistoryUpdateEventType):
    newValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19294", browseName="NewValues", modellingRule="Mandatory", dataType=ns0_datypes.Annotation, valueRank=1, arrayDimensions=[0])
    )
    oldValues: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19295", browseName="OldValues", modellingRule="Mandatory", dataType=ns0_datypes.Annotation, valueRank=1, arrayDimensions=[0])
    )
    performInsertReplace: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19293", browseName="PerformInsertReplace", modellingRule="Mandatory", dataType=ns0_datypes.PerformUpdateType, valueRank=-1)
    )


@o6.objecttype(nodeId="i=19362", browseName="BaseLogEventType", displayName="BaseLogEventType", isAbstract=True)
class BaseLogEventType(BaseEventType):
    conditionClassId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19363", browseName="ConditionClassId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    conditionClassName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19364", browseName="ConditionClassName", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    errorCode: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19365", browseName="ErrorCode", modellingRule="Optional", dataType=o6.StatusCode, valueRank=-1)
    )
    errorCodeNode: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19366", browseName="ErrorCodeNode", modellingRule="Optional", dataType=o6.NodeId, valueRank=-1)
    )
    traceContext: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24376", browseName="TraceContext", modellingRule="Optional", dataType=ns0_datypes.TraceContextDataType, valueRank=-1)
    )


@o6.objecttype(nodeId="i=19369", browseName="LogOverflowEventType", displayName="LogOverflowEventType", isAbstract=True)
class LogOverflowEventType(BaseEventType):
    pass


@o6.objecttype(
    nodeId="i=23606",
    browseName="AuditClientEventType",
    displayName="AuditClientEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditClientEventType(AuditEventType):
    serverUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23908", browseName="ServerUri", modellingRule="Mandatory", dataType=ns0_datypes.UriString, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=23926",
    browseName="AuditClientUpdateMethodResultEventType",
    displayName="AuditClientUpdateMethodResultEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditClientUpdateMethodResultEventType(AuditClientEventType):
    inputArguments: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23999", browseName="InputArguments", modellingRule="Mandatory", valueRank=1, arrayDimensions=[0])
    )
    methodId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23995", browseName="MethodId", modellingRule="Mandatory", dataType=o6.ExpandedNodeId, valueRank=-1)
    )
    objectId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23994", browseName="ObjectId", modellingRule="Mandatory", dataType=o6.ExpandedNodeId, valueRank=-1)
    )
    outputArguments: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25684", browseName="OutputArguments", modellingRule="Mandatory", valueRank=1, arrayDimensions=[0])
    )
    statusCodeId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23998", browseName="StatusCodeId", modellingRule="Mandatory", dataType=o6.StatusCode, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2782", browseName="ConditionType", displayName="ConditionType", isAbstract=True)
class ConditionType(BaseEventType):
    addComment: o6.node.MethodNode = o6.hasComponent(o6.ns["i=9029"])
    branchId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9010", browseName="BranchId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    clientUserId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9026", browseName="ClientUserId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    comment: ns0_vartypes.ConditionVariableType
    conditionClassId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11112", browseName="ConditionClassId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    conditionClassName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11113", browseName="ConditionClassName", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    conditionName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9009", browseName="ConditionName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    conditionRefresh: o6.node.MethodNode = o6.hasComponent(o6.ns["i=3875"])
    conditionRefresh2: o6.node.MethodNode = o6.hasComponent(o6.ns["i=12912"])
    conditionSubClassId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16363", browseName="ConditionSubClassId", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    conditionSubClassName: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16364", browseName="ConditionSubClassName", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )
    disable: o6.node.MethodNode = o6.hasComponent(o6.ns["i=9028"])
    enable: o6.node.MethodNode = o6.hasComponent(o6.ns["i=9027"])
    enabledState: ns0_vartypes.TwoStateVariableType
    lastSeverity: ns0_vartypes.ConditionVariableType
    quality: ns0_vartypes.ConditionVariableType
    retain: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=3874", browseName="Retain", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    supportsFilteredRetain: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32060", browseName="SupportsFilteredRetain", dataType=o6.Boolean, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2830", browseName="DialogConditionType", displayName="DialogConditionType")
class DialogConditionType(ConditionType):
    cancelResponse: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9067", browseName="CancelResponse", modellingRule="Mandatory", dataType=o6.Int32, valueRank=-1)
    )
    defaultResponse: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9065", browseName="DefaultResponse", modellingRule="Mandatory", dataType=o6.Int32, valueRank=-1)
    )
    dialogState: ns0_vartypes.TwoStateVariableType
    enabledState: ns0_vartypes.TwoStateVariableType
    lastResponse: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9068", browseName="LastResponse", modellingRule="Mandatory", dataType=o6.Int32, valueRank=-1)
    )
    okResponse: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9066", browseName="OkResponse", modellingRule="Mandatory", dataType=o6.Int32, valueRank=-1)
    )
    prompt: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2831", browseName="Prompt", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    respond: o6.node.MethodNode = o6.hasComponent(o6.ns["i=9069"])
    respond2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24312"])
    responseOptionSet: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9064", browseName="ResponseOptionSet", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="i=2881", browseName="AcknowledgeableConditionType", displayName="AcknowledgeableConditionType")
class AcknowledgeableConditionType(ConditionType):
    ackedState: ns0_vartypes.TwoStateVariableType
    acknowledge: o6.node.MethodNode = o6.hasComponent(o6.ns["i=9111"])
    confirm: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=9113"])
    confirmedState: ns0_vartypes.TwoStateVariableType | None
    enabledState: ns0_vartypes.TwoStateVariableType


@o6.objecttype(nodeId="i=2915", browseName="AlarmConditionType", displayName="AlarmConditionType")
class AlarmConditionType(AcknowledgeableConditionType):
    activeState: ns0_vartypes.TwoStateVariableType
    alarmGroup_: AlarmGroupType | None = o6.reference(AlarmGroupType(nodeId="i=16399", browseName="<AlarmGroup>", modellingRule="OptionalPlaceholder"), "i=16361")
    audibleEnabled: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16389", browseName="AudibleEnabled", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    audibleSound: ns0_vartypes.AudioVariableType | None = o6.hasComponent(
        ns0_vartypes.AudioVariableType(nodeId="i=16390", browseName="AudibleSound", modellingRule="Optional", dataType=ns0_datypes.AudioDataType, valueRank=-1)
    )
    enabledState: ns0_vartypes.TwoStateVariableType
    firstInGroup: AlarmGroupType | None = o6.hasComponent(AlarmGroupType(nodeId="i=16398", browseName="FirstInGroup", modellingRule="Optional"))
    firstInGroupFlag: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=16397", browseName="FirstInGroupFlag", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    getGroupMemberships: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24744"])
    inputNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11120", browseName="InputNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    latchedState: ns0_vartypes.TwoStateVariableType | None
    maxTimeShelved: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9216", browseName="MaxTimeShelved", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    offDelay: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16396", browseName="OffDelay", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    onDelay: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16395", browseName="OnDelay", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    outOfServiceState: ns0_vartypes.TwoStateVariableType | None
    placeInService: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17870"])
    placeInService2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24322"])
    reAlarmRepeatCount: ns0_vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0_vartypes.BaseDataVariableType(nodeId="i=16401", browseName="ReAlarmRepeatCount", modellingRule="Optional", dataType=o6.Int16, valueRank=-1)
    )
    reAlarmTime: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16400", browseName="ReAlarmTime", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    removeFromService: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17869"])
    removeFromService2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24320"])
    reset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=18199"])
    reset2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24324"])
    shelvingState: ShelvedStateMachineType | None
    silence: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16402"])
    silenceState: ns0_vartypes.TwoStateVariableType | None
    suppress: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16403"])
    suppress2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24316"])
    suppressedOrShelved: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9215", browseName="SuppressedOrShelved", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    suppressedState: ns0_vartypes.TwoStateVariableType | None
    unsuppress: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17868"])
    unsuppress2: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=24318"])


@o6.objecttype(nodeId="i=2955", browseName="LimitAlarmType", displayName="LimitAlarmType")
class LimitAlarmType(AlarmConditionType):
    baseHighHighLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16572", browseName="BaseHighHighLimit", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    baseHighLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16573", browseName="BaseHighLimit", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    baseLowLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16574", browseName="BaseLowLimit", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    baseLowLowLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16575", browseName="BaseLowLowLimit", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    highDeadband: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24775", browseName="HighDeadband", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    highHighDeadband: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24774", browseName="HighHighDeadband", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    highHighLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11124", browseName="HighHighLimit", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    highLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11125", browseName="HighLimit", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    lowDeadband: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24776", browseName="LowDeadband", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    lowLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11126", browseName="LowLimit", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    lowLowDeadband: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24777", browseName="LowLowDeadband", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    lowLowLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11127", browseName="LowLowLimit", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    severityHigh: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24771", browseName="SeverityHigh", modellingRule="Optional", dataType=o6.UInt16, valueRank=-1)
    )
    severityHighHigh: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24770", browseName="SeverityHighHigh", modellingRule="Optional", dataType=o6.UInt16, valueRank=-1)
    )
    severityLow: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24772", browseName="SeverityLow", modellingRule="Optional", dataType=o6.UInt16, valueRank=-1)
    )
    severityLowLow: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=24773", browseName="SeverityLowLow", modellingRule="Optional", dataType=o6.UInt16, valueRank=-1)
    )


@o6.objecttype(nodeId="i=9341", browseName="ExclusiveLimitAlarmType", displayName="ExclusiveLimitAlarmType")
class ExclusiveLimitAlarmType(LimitAlarmType):
    activeState: ns0_vartypes.TwoStateVariableType
    limitState: ExclusiveLimitStateMachineType


@o6.objecttype(nodeId="i=9482", browseName="ExclusiveLevelAlarmType", displayName="ExclusiveLevelAlarmType")
class ExclusiveLevelAlarmType(ExclusiveLimitAlarmType):
    pass


@o6.objecttype(nodeId="i=9623", browseName="ExclusiveRateOfChangeAlarmType", displayName="ExclusiveRateOfChangeAlarmType")
class ExclusiveRateOfChangeAlarmType(ExclusiveLimitAlarmType):
    engineeringUnits: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16899", browseName="EngineeringUnits", modellingRule="Optional", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )


@o6.objecttype(nodeId="i=9764", browseName="ExclusiveDeviationAlarmType", displayName="ExclusiveDeviationAlarmType")
class ExclusiveDeviationAlarmType(ExclusiveLimitAlarmType):
    baseSetpointNode: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16817", browseName="BaseSetpointNode", modellingRule="Optional", dataType=o6.NodeId, valueRank=-1)
    )
    setpointNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=9905", browseName="SetpointNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(nodeId="i=9906", browseName="NonExclusiveLimitAlarmType", displayName="NonExclusiveLimitAlarmType")
class NonExclusiveLimitAlarmType(LimitAlarmType):
    activeState: ns0_vartypes.TwoStateVariableType
    highHighState: ns0_vartypes.TwoStateVariableType | None
    highState: ns0_vartypes.TwoStateVariableType | None
    lowLowState: ns0_vartypes.TwoStateVariableType | None
    lowState: ns0_vartypes.TwoStateVariableType | None


@o6.objecttype(nodeId="i=10060", browseName="NonExclusiveLevelAlarmType", displayName="NonExclusiveLevelAlarmType")
class NonExclusiveLevelAlarmType(NonExclusiveLimitAlarmType):
    pass


@o6.objecttype(nodeId="i=10214", browseName="NonExclusiveRateOfChangeAlarmType", displayName="NonExclusiveRateOfChangeAlarmType")
class NonExclusiveRateOfChangeAlarmType(NonExclusiveLimitAlarmType):
    engineeringUnits: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16858", browseName="EngineeringUnits", modellingRule="Optional", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )


@o6.objecttype(nodeId="i=10368", browseName="NonExclusiveDeviationAlarmType", displayName="NonExclusiveDeviationAlarmType")
class NonExclusiveDeviationAlarmType(NonExclusiveLimitAlarmType):
    baseSetpointNode: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16776", browseName="BaseSetpointNode", modellingRule="Optional", dataType=o6.NodeId, valueRank=-1)
    )
    setpointNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=10522", browseName="SetpointNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(nodeId="i=10523", browseName="DiscreteAlarmType", displayName="DiscreteAlarmType")
class DiscreteAlarmType(AlarmConditionType):
    pass


@o6.objecttype(nodeId="i=10637", browseName="OffNormalAlarmType", displayName="OffNormalAlarmType")
class OffNormalAlarmType(DiscreteAlarmType):
    normalState: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11158", browseName="NormalState", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(nodeId="i=10751", browseName="TripAlarmType", displayName="TripAlarmType")
class TripAlarmType(OffNormalAlarmType):
    pass


@o6.objecttype(nodeId="i=11753", browseName="SystemOffNormalAlarmType", displayName="SystemOffNormalAlarmType")
class SystemOffNormalAlarmType(OffNormalAlarmType):
    pass


@o6.objecttype(nodeId="i=13225", browseName="CertificateExpirationAlarmType", displayName="CertificateExpirationAlarmType")
class CertificateExpirationAlarmType(SystemOffNormalAlarmType):
    certificate: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=13327", browseName="Certificate", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )
    certificateType: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=13326", browseName="CertificateType", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    expirationDate: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=13325", browseName="ExpirationDate", modellingRule="Mandatory", dataType=o6.DateTime, valueRank=-1)
    )
    expirationLimit: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=14900", browseName="ExpirationLimit", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )


o6.reference(CertificateGroupType, "i=9006", CertificateExpirationAlarmType)


@o6.objecttype(nodeId="i=17080", browseName="DiscrepancyAlarmType", displayName="DiscrepancyAlarmType")
class DiscrepancyAlarmType(AlarmConditionType):
    expectedTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17216", browseName="ExpectedTime", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    targetValueNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17215", browseName="TargetValueNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    tolerance: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17217", browseName="Tolerance", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )


@o6.objecttype(nodeId="i=18347", browseName="InstrumentDiagnosticAlarmType", displayName="InstrumentDiagnosticAlarmType")
class InstrumentDiagnosticAlarmType(OffNormalAlarmType):
    pass


@o6.objecttype(nodeId="i=18496", browseName="SystemDiagnosticAlarmType", displayName="SystemDiagnosticAlarmType")
class SystemDiagnosticAlarmType(OffNormalAlarmType):
    pass


@o6.objecttype(nodeId="i=19297", browseName="TrustListOutOfDateAlarmType", displayName="TrustListOutOfDateAlarmType")
class TrustListOutOfDateAlarmType(SystemOffNormalAlarmType):
    lastUpdateTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19447", browseName="LastUpdateTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    trustListId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19446", browseName="TrustListId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    updateFrequency: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19448", browseName="UpdateFrequency", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )


o6.reference(CertificateGroupType, "i=9006", TrustListOutOfDateAlarmType)


@o6.objecttype(nodeId="i=32064", browseName="AlarmSuppressionGroupType", displayName="AlarmSuppressionGroupType")
class AlarmSuppressionGroupType(AlarmGroupType):
    alarmCondition_: AlarmConditionType | None
    digitalVariable_: ns0_vartypes.BaseDataVariableType | None = o6.reference(
        ns0_vartypes.BaseDataVariableType(nodeId="i=32226", browseName="<DigitalVariable>", modellingRule="OptionalPlaceholder", dataType=o6.Boolean, valueRank=-1), "i=32059"
    )


@o6.objecttype(nodeId="i=12522", browseName="TrustListType", displayName="TrustListType")
class TrustListType(FileType):
    activityTimeout: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32254", browseName="ActivityTimeout", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    addCertificate: o6.node.MethodNode = o6.hasComponent(o6.ns["i=12548"])
    closeAndUpdate: o6.node.MethodNode = o6.hasComponent(o6.ns["i=12546"])
    defaultValidationOptions: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23563", browseName="DefaultValidationOptions", modellingRule="Optional", dataType=ns0_datypes.TrustListValidationOptions, valueRank=-1)
    )
    lastUpdateTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12542", browseName="LastUpdateTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    openWithMasks: o6.node.MethodNode = o6.hasComponent(o6.ns["i=12543"])
    removeCertificate: o6.node.MethodNode = o6.hasComponent(o6.ns["i=12550"])
    updateFrequency: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19296", browseName="UpdateFrequency", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32260", browseName="TrustListUpdateRequestedAuditEventType", displayName="TrustListUpdateRequestedAuditEventType", isAbstract=True)
class TrustListUpdateRequestedAuditEventType(AuditUpdateMethodEventType):
    pass


@o6.objecttype(nodeId="i=12561", browseName="TrustListUpdatedAuditEventType", displayName="TrustListUpdatedAuditEventType", isAbstract=True)
class TrustListUpdatedAuditEventType(AuditUpdateMethodEventType):
    trustListId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32281", browseName="TrustListId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32286", browseName="TransactionDiagnosticsType", displayName="TransactionDiagnosticsType")
class TransactionDiagnosticsType(BaseObjectType):
    affectedCertificateGroups: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32291", browseName="AffectedCertificateGroups", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    affectedTrustLists: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32290", browseName="AffectedTrustLists", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    endTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32288", browseName="EndTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    errors: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32292", browseName="Errors", modellingRule="Mandatory", dataType=ns0_datypes.TransactionErrorType, valueRank=1, arrayDimensions=[0])
    )
    result: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32289", browseName="Result", modellingRule="Mandatory", dataType=o6.StatusCode, valueRank=-1)
    )
    startTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32287", browseName="StartTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


ns0_vartypes.PropertyType(
    nodeId="i=32297",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="i=32296",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0_datypes.Argument(name="CertificateGroupId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[])],
)
ns0_vartypes.PropertyType(
    nodeId="i=32298",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="i=32296",
    referenceType=ns0_reftypes.HasProperty,
    dataType=ns0_datypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0_datypes.Argument(name="CertificateTypeIds", dataType=o6.NodeId("i=17"), valueRank=1, arrayDimensions=[0]),
        ns0_datypes.Argument(name="Certificates", dataType=o6.NodeId("i=15"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="i=32296", browseName="GetCertificates", modellingRule="Optional", inputArgs=o6.hasProperty(o6.ns["i=32297"]), outputArgs=o6.hasProperty(o6.ns["i=32298"]))


@o6.objecttype(nodeId="i=12581", browseName="ServerConfigurationType", displayName="ServerConfigurationType")
class ServerConfigurationType(BaseObjectType):
    applicationNames: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18660", browseName="ApplicationNames", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )
    applicationType: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25697", browseName="ApplicationType", modellingRule="Optional", dataType=ns0_datypes.ApplicationType, valueRank=-1)
    )
    applicationUri: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25696", browseName="ApplicationUri", modellingRule="Optional", dataType=ns0_datypes.UriString, valueRank=-1)
    )
    applyChanges: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="i=12734", browseName="ApplyChanges", modellingRule="Mandatory"))
    cancelChanges: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="i=25698", browseName="CancelChanges", modellingRule="Optional"))
    certificateGroups: CertificateGroupFolderType
    configurationFile: ApplicationConfigurationFileType | None
    createSelfSignedCertificate: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=19337"])
    createSigningRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["i=12731"])
    deleteCertificate: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=19340"])
    getCertificates: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=32296"])
    getRejectedList: o6.node.MethodNode = o6.hasComponent(o6.ns["i=12775"])
    hasSecureElement: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23593", browseName="HasSecureElement", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    inApplicationSetup: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19308", browseName="InApplicationSetup", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    maxTrustListSize: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12584", browseName="MaxTrustListSize", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    multicastDnsEnabled: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12585", browseName="MulticastDnsEnabled", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    productUri: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25724", browseName="ProductUri", modellingRule="Optional", dataType=ns0_datypes.UriString, valueRank=-1)
    )
    resetToServerDefaults: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="i=25699", browseName="ResetToServerDefaults", modellingRule="Optional"))
    serverCapabilities: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12708", browseName="ServerCapabilities", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    supportedPrivateKeyFormats: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=12583", browseName="SupportedPrivateKeyFormats", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    supportsTransactions: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=18661", browseName="SupportsTransactions", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    transactionDiagnostics: TransactionDiagnosticsType | None
    updateCertificate: o6.node.MethodNode = o6.hasComponent(o6.ns["i=12616"])


@o6.objecttype(nodeId="i=25731", browseName="ApplicationConfigurationType", displayName="ApplicationConfigurationType")
class ApplicationConfigurationType(ServerConfigurationType):
    applicationType: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=26852", browseName="ApplicationType", modellingRule="Mandatory", dataType=ns0_datypes.ApplicationType, valueRank=-1)
    )
    applicationUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=26850", browseName="ApplicationUri", modellingRule="Mandatory", dataType=ns0_datypes.UriString, valueRank=-1)
    )
    authorizationServices: AuthorizationServicesConfigurationFolderType | None = o6.hasComponent(
        AuthorizationServicesConfigurationFolderType(nodeId="i=19427", browseName="AuthorizationServices", modellingRule="Optional")
    )
    enabled: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=26849", browseName="Enabled", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    isNonUaApplication: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23741", browseName="IsNonUaApplication", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    keyCredentials: KeyCredentialConfigurationFolderType | None = o6.hasComponent(
        KeyCredentialConfigurationFolderType(nodeId="i=19423", browseName="KeyCredentials", modellingRule="Optional")
    )
    productUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=26851", browseName="ProductUri", modellingRule="Mandatory", dataType=ns0_datypes.UriString, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32306", browseName="CertificateUpdateRequestedAuditEventType", displayName="CertificateUpdateRequestedAuditEventType", isAbstract=True)
class CertificateUpdateRequestedAuditEventType(AuditUpdateMethodEventType):
    pass


@o6.objecttype(nodeId="i=14416", browseName="PublishSubscribeType", displayName="PublishSubscribeType")
class PublishSubscribeType(PubSubKeyServiceType):
    addConnection: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=16598"])
    configurationProperties: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=32397", browseName="ConfigurationProperties", modellingRule="Optional", dataType=ns0_datypes.KeyValuePair, valueRank=1, arrayDimensions=[0]
        )
    )
    configurationVersion: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25433", browseName="ConfigurationVersion", modellingRule="Optional", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )
    connectionName_: PubSubConnectionType | None
    dataSetClasses: FolderType | None
    defaultDatagramPublisherId: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25432", browseName="DefaultDatagramPublisherId", modellingRule="Optional", dataType=o6.UInt64, valueRank=-1)
    )
    defaultSecurityKeyServices: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=32396", browseName="DefaultSecurityKeyServices", modellingRule="Optional", dataType=ns0_datypes.EndpointDescription, valueRank=1, arrayDimensions=[0]
        )
    )
    diagnostics: PubSubDiagnosticsRootType | None
    pubSubCapablities: PubSubCapabilitiesType | None
    pubSubConfiguration: PubSubConfigurationType | None
    publishedDataSets: DataSetFolderType = o6.hasComponent(DataSetFolderType(nodeId="i=14434", browseName="PublishedDataSets", modellingRule="Mandatory"))
    removeConnection: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=14432"])
    setSecurityKeys: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=17296"])
    status: PubSubStatusType
    subscribedDataSets: SubscribedDataSetFolderType | None = o6.hasComponent(
        SubscribedDataSetFolderType(nodeId="i=23622", browseName="SubscribedDataSets", modellingRule="Optional")
    )
    supportedTransportProfiles: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=17479", browseName="SupportedTransportProfiles", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="i=2034", browseName="ServerRedundancyType", displayName="ServerRedundancyType")
class ServerRedundancyType(BaseObjectType):
    redundancySupport: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2035", browseName="RedundancySupport", modellingRule="Mandatory", dataType=ns0_datypes.RedundancySupport, valueRank=-1)
    )
    redundantServerArray: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=32410", browseName="RedundantServerArray", modellingRule="Optional", dataType=ns0_datypes.RedundantServerDataType, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(nodeId="i=2036", browseName="TransparentRedundancyType", displayName="TransparentRedundancyType")
class TransparentRedundancyType(ServerRedundancyType):
    currentServerId: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2037", browseName="CurrentServerId", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    redundantServerArray: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=2038", browseName="RedundantServerArray", modellingRule="Mandatory", dataType=ns0_datypes.RedundantServerDataType, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(nodeId="i=2039", browseName="NonTransparentRedundancyType", displayName="NonTransparentRedundancyType")
class NonTransparentRedundancyType(ServerRedundancyType):
    serverUriArray: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2040", browseName="ServerUriArray", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="i=11945", browseName="NonTransparentNetworkRedundancyType", displayName="NonTransparentNetworkRedundancyType")
class NonTransparentNetworkRedundancyType(NonTransparentRedundancyType):
    serverNetworkGroups: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=11948", browseName="ServerNetworkGroups", modellingRule="Mandatory", dataType=ns0_datypes.NetworkGroupDataType, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(nodeId="i=32411", browseName="NonTransparentBackupRedundancyType", displayName="NonTransparentBackupRedundancyType")
class NonTransparentBackupRedundancyType(NonTransparentRedundancyType):
    failover: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="i=32416", browseName="Failover", modellingRule="Mandatory"))
    mode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32415", browseName="Mode", modellingRule="Mandatory", dataType=ns0_datypes.RedundantServerMode, valueRank=-1)
    )
    redundantServerArray: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=32413", browseName="RedundantServerArray", modellingRule="Mandatory", dataType=ns0_datypes.RedundantServerDataType, valueRank=1, arrayDimensions=[0]
        )
    )


@o6.objecttype(nodeId="i=11616", browseName="NamespaceMetadataType", displayName="NamespaceMetadataType")
class NamespaceMetadataType(BaseObjectType):
    configurationVersion: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=25267", browseName="ConfigurationVersion", modellingRule="Optional", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )
    defaultAccessRestrictions: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=16139", browseName="DefaultAccessRestrictions", modellingRule="Optional", dataType=ns0_datypes.AccessRestrictionType, valueRank=-1)
    )
    defaultRolePermissions: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=16137", browseName="DefaultRolePermissions", modellingRule="Optional", dataType=ns0_datypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
        )
    )
    defaultUserRolePermissions: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=16138", browseName="DefaultUserRolePermissions", modellingRule="Optional", dataType=ns0_datypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
        )
    )
    isNamespaceSubset: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11620", browseName="IsNamespaceSubset", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    modelVersion: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32419", browseName="ModelVersion", modellingRule="Optional", dataType=ns0_datypes.SemanticVersionString, valueRank=-1)
    )
    namespaceFile: AddressSpaceFileType | None
    namespacePublicationDate: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11619", browseName="NamespacePublicationDate", modellingRule="Mandatory", dataType=o6.DateTime, valueRank=-1)
    )
    namespaceUri: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11617", browseName="NamespaceUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    namespaceVersion: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11618", browseName="NamespaceVersion", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    staticNodeIdTypes: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11621", browseName="StaticNodeIdTypes", modellingRule="Mandatory", dataType=ns0_datypes.IdType, valueRank=1, arrayDimensions=[0])
    )
    staticNumericNodeIdRange: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=11622", browseName="StaticNumericNodeIdRange", modellingRule="Mandatory", dataType=ns0_datypes.NumericRange, valueRank=1, arrayDimensions=[0]
        )
    )
    staticStringNodeIdPattern: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11623", browseName="StaticStringNodeIdPattern", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32439", browseName="SyntaxReferenceEntryType", displayName="SyntaxReferenceEntryType")
class SyntaxReferenceEntryType(DictionaryEntryType):
    commonName: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32441", browseName="CommonName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32442", browseName="UnitType", displayName="UnitType", isAbstract=True)
class UnitType(BaseObjectType):
    discipline: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32446", browseName="Discipline", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    symbol: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32443", browseName="Symbol", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    unitSystem: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32445", browseName="UnitSystem", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32447", browseName="ServerUnitType", displayName="ServerUnitType")
class ServerUnitType(UnitType):
    alternativeUnits: BaseObjectType | None
    coherentUnit: UnitType | None
    conversionLimit: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32461", browseName="ConversionLimit", modellingRule="Mandatory", dataType=ns0_datypes.ConversionLimitEnum, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32467", browseName="AlternativeUnitType", displayName="AlternativeUnitType")
class AlternativeUnitType(UnitType):
    linearConversion: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32472", browseName="LinearConversion", modellingRule="Optional", dataType=ns0_datypes.LinearConversionDataType, valueRank=-1)
    )
    mathMLConversion: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32473", browseName="MathMLConversion", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    mathMLInverseConversion: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32474", browseName="MathMLInverseConversion", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32475", browseName="QuantityType", displayName="QuantityType")
class QuantityType(BaseObjectType):
    annotation: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32478", browseName="Annotation", modellingRule="Optional", dataType=ns0_datypes.AnnotationDataType, valueRank=1, arrayDimensions=[0])
    )
    conversionService: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32479", browseName="ConversionService", modellingRule="Optional", dataType=ns0_datypes.UriString, valueRank=-1)
    )
    dimension: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32480", browseName="Dimension", modellingRule="Mandatory", dataType=ns0_datypes.QuantityDimension, valueRank=-1)
    )
    serverUnits: BaseObjectType
    symbol: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32476", browseName="Symbol", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=-1)
    )


@o6.objecttype(nodeId="i=2318", browseName="HistoricalDataConfigurationType", displayName="HistoricalDataConfigurationType")
class HistoricalDataConfigurationType(BaseObjectType):
    aggregateConfiguration: AggregateConfigurationType
    aggregateFunctions: FolderType | None = o6.hasComponent(FolderType(nodeId="i=11876", browseName="AggregateFunctions", modellingRule="Optional"))
    definition: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2324", browseName="Definition", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    exceptionDeviation: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2327", browseName="ExceptionDeviation", modellingRule="Optional", dataType=o6.Double, valueRank=-1)
    )
    exceptionDeviationFormat: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2328", browseName="ExceptionDeviationFormat", modellingRule="Optional", dataType=ns0_datypes.ExceptionDeviationFormat, valueRank=-1)
    )
    maxCountStoredValues: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32620", browseName="MaxCountStoredValues", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxTimeInterval: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2325", browseName="MaxTimeInterval", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    maxTimeStoredValues: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32619", browseName="MaxTimeStoredValues", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    minTimeInterval: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2326", browseName="MinTimeInterval", modellingRule="Optional", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    serverTimestampSupported: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=19092", browseName="ServerTimestampSupported", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    startOfArchive: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11499", browseName="StartOfArchive", modellingRule="Optional", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    startOfOnlineArchive: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=11500", browseName="StartOfOnlineArchive", modellingRule="Optional", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    stepped: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=2323", browseName="Stepped", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32621", browseName="HistoricalEventConfigurationType", displayName="HistoricalEventConfigurationType")
class HistoricalEventConfigurationType(BaseObjectType):
    eventTypes: FolderType = o6.hasComponent(FolderType(nodeId="i=32622", browseName="EventTypes", modellingRule="Mandatory"))
    sortByEventFields: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(
            nodeId="i=18644", browseName="SortByEventFields", modellingRule="Optional", dataType=ns0_datypes.SimpleAttributeOperand, valueRank=1, arrayDimensions=[0]
        )
    )
    startOfArchive: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32623", browseName="StartOfArchive", modellingRule="Optional", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    startOfOnlineArchive: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32624", browseName="StartOfOnlineArchive", modellingRule="Optional", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


@o6.objecttype(nodeId="i=32625", browseName="HistoricalExternalEventSourceType", displayName="HistoricalExternalEventSourceType")
class HistoricalExternalEventSourceType(BaseObjectType):
    endpointUrl: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32627", browseName="EndpointUrl", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    historicalEventFilter: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32632", browseName="HistoricalEventFilter", modellingRule="Mandatory", dataType=ns0_datypes.EventFilter, valueRank=-1)
    )
    identityTokenPolicy: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32630", browseName="IdentityTokenPolicy", modellingRule="Optional", dataType=ns0_datypes.UserTokenPolicy, valueRank=-1)
    )
    securityMode: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32628", browseName="SecurityMode", modellingRule="Optional", dataType=ns0_datypes.MessageSecurityMode, valueRank=-1)
    )
    securityPolicyUri: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32629", browseName="SecurityPolicyUri", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    server: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32626", browseName="Server", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )
    transportProfileUri: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32631", browseName="TransportProfileUri", modellingRule="Optional", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(
    nodeId="i=32758",
    browseName="AuditHistoryConfigurationChangeEventType",
    displayName="AuditHistoryConfigurationChangeEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryConfigurationChangeEventType(AuditEventType):
    pass


@o6.objecttype(
    nodeId="i=32803",
    browseName="AuditHistoryBulkInsertEventType",
    displayName="AuditHistoryBulkInsertEventType",
    rolePermissions={
        "i=15644": ns0_datypes.PermissionType.BROWSE | ns0_datypes.PermissionType.READ,
        "i=15704": ns0_datypes.PermissionType.BROWSE
        | ns0_datypes.PermissionType.READ_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_ATTRIBUTE
        | ns0_datypes.PermissionType.WRITE_ROLE_PERMISSIONS
        | ns0_datypes.PermissionType.WRITE_HISTORIZING
        | ns0_datypes.PermissionType.READ
        | ns0_datypes.PermissionType.WRITE
        | ns0_datypes.PermissionType.READ_HISTORY
        | ns0_datypes.PermissionType.INSERT_HISTORY
        | ns0_datypes.PermissionType.MODIFY_HISTORY
        | ns0_datypes.PermissionType.DELETE_HISTORY
        | ns0_datypes.PermissionType.RECEIVE_EVENTS
        | ns0_datypes.PermissionType.CALL
        | ns0_datypes.PermissionType.ADD_REFERENCE
        | ns0_datypes.PermissionType.REMOVE_REFERENCE
        | ns0_datypes.PermissionType.DELETE_NODE,
    },
    isAbstract=True,
)
class AuditHistoryBulkInsertEventType(AuditEventType):
    endTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32823", browseName="EndTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    startTime: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32822", browseName="StartTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    updatedNode: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32821", browseName="UpdatedNode", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )


@o6.objecttype(nodeId="i=23832", browseName="PubSubCapabilitiesType", displayName="PubSubCapabilitiesType")
class PubSubCapabilitiesType(BaseObjectType):
    maxDataSetReaders: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23837", browseName="MaxDataSetReaders", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxDataSetWriters: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23836", browseName="MaxDataSetWriters", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxDataSetWritersPerGroup: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32651", browseName="MaxDataSetWritersPerGroup", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxFieldsPerDataSet: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23838", browseName="MaxFieldsPerDataSet", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxNetworkMessageSizeBroker: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32653", browseName="MaxNetworkMessageSizeBroker", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxNetworkMessageSizeDatagram: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32652", browseName="MaxNetworkMessageSizeDatagram", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxPubSubConnections: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23833", browseName="MaxPubSubConnections", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxPublishedDataSets: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32846", browseName="MaxPublishedDataSets", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxPushTargets: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32845", browseName="MaxPushTargets", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxReaderGroups: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23835", browseName="MaxReaderGroups", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxSecurityGroups: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32844", browseName="MaxSecurityGroups", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxStandaloneSubscribedDataSets: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32847", browseName="MaxStandaloneSubscribedDataSets", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1)
    )
    maxWriterGroups: ns0_vartypes.PropertyType = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=23834", browseName="MaxWriterGroups", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    supportSecurityKeyPull: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32654", browseName="SupportSecurityKeyPull", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    supportSecurityKeyPush: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32655", browseName="SupportSecurityKeyPush", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )
    supportSecurityKeyServer: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32848", browseName="SupportSecurityKeyServer", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1)
    )


@o6.objecttype(nodeId="i=23456", browseName="AliasNameCategoryType", displayName="AliasNameCategoryType")
class AliasNameCategoryType(FolderType):
    addAliasesToCategory: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=23972"])
    alias_: AliasNameType | None = o6.organizes(AliasNameType(nodeId="i=23457", browseName="<Alias>", modellingRule="OptionalPlaceholder"))
    deleteAliasesFromCategory: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=23975"])
    findAlias: o6.node.MethodNode = o6.hasComponent(o6.ns["i=23462"])
    findAliasVerbose: o6.node.MethodNode | None = o6.hasComponent(o6.ns["i=23963"])
    lastChange: ns0_vartypes.PropertyType | None = o6.hasProperty(
        ns0_vartypes.PropertyType(nodeId="i=32850", browseName="LastChange", modellingRule="Optional", dataType=ns0_datypes.VersionTime, valueRank=-1)
    )
    subAliasNameCategories_: AliasNameCategoryType | None


del Any, TYPE_CHECKING, uuid, o6, ns0_reftypes, ns0_datypes, ns0_vartypes
