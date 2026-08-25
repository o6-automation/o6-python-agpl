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

"""Generated OPC UA pnrio namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.referencetype(nodeId="ns=pnrio;i=4004", browseName="ns=pnrio;HasRioInputChannel", displayName="HasRioInputChannel", inverseName="IsRioInputChannelOf")
class HasRioInputChannel(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=pnrio;i=4005", browseName="ns=pnrio;HasRioOutputChannel", displayName="HasRioOutputChannel", inverseName="IsRioOutputChannelOf")
class HasRioOutputChannel(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=pnrio;i=4006", browseName="ns=pnrio;HasRioProcessVariable", displayName="HasRioProcessVariable", inverseName="IsRioProcessVariableOf")
class HasRioProcessVariable(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=pnrio;i=4007", browseName="ns=pnrio;HasRioConfiguration", displayName="HasRioConfiguration", inverseName="IsRioConfigurationOf")
class HasRioConfiguration(ns0.reftypes.HasComponent):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ns0
