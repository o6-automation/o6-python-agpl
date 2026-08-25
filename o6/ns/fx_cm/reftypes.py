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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.referencetype(nodeId="ns=fx_cm;i=1053", browseName="ns=fx_cm;HasServerAddress", displayName="HasServerAddress", inverseName="ServerAddressOf")
class HasServerAddress(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_cm;i=1057", browseName="ns=fx_cm;HasConnectionConfiguration", displayName="HasConnectionConfiguration", inverseName="ConnectionConfigurationOf")
class HasConnectionConfiguration(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(
    nodeId="ns=fx_cm;i=1060",
    browseName="ns=fx_cm;HasCommunicationFlowConfiguration",
    displayName="HasCommunicationFlowConfiguration",
    inverseName="CommunicationFlowConfigurationOf",
)
class HasCommunicationFlowConfiguration(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(
    nodeId="ns=fx_cm;i=1062",
    browseName="ns=fx_cm;HasAutomationComponentConfiguration",
    displayName="HasAutomationComponentConfiguration",
    inverseName="AutomationComponentConfigurationOf",
)
class HasAutomationComponentConfiguration(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(
    nodeId="ns=fx_cm;i=1063",
    browseName="ns=fx_cm;ToAutomationComponentConfiguration",
    displayName="ToAutomationComponentConfiguration",
    inverseName="FromAutomationComponentConfiguration",
)
class ToAutomationComponentConfiguration(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=fx_cm;i=4001",
    browseName="ns=fx_cm;ToConnectionEndpointConfiguration",
    displayName="ToConnectionEndpointConfiguration",
    inverseName="FromConnectionEndpointConfiguration",
)
class ToConnectionEndpointConfiguration(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=fx_cm;i=4003", browseName="ns=fx_cm;HasCharacteristic", displayName="HasCharacteristic", inverseName="CharacteristicOf")
class HasCharacteristic(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_cm;i=4004", browseName="ns=fx_cm;ToFlow", displayName="ToFlow", inverseName="FromFlow")
class ToFlow(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=fx_cm;i=4005", browseName="ns=fx_cm;HasAssetToVerify", displayName="HasAssetToVerify", inverseName="AssetToVerifyOf")
class HasAssetToVerify(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_cm;i=4006", browseName="ns=fx_cm;ToInboundFlow", displayName="ToInboundFlow", inverseName="FromInboundFlow")
class ToInboundFlow(ToFlow):
    pass


@o6.referencetype(nodeId="ns=fx_cm;i=4007", browseName="ns=fx_cm;ToOutboundFlow", displayName="ToOutboundFlow", inverseName="FromOutboundFlow")
class ToOutboundFlow(ToFlow):
    pass


@o6.referencetype(nodeId="ns=fx_cm;i=4008", browseName="ns=fx_cm;HasCMCapability", displayName="HasCMCapability", inverseName="CMCapabilityOf")
class HasCMCapability(ns0.reftypes.HasComponent):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0
