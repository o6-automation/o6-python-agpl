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

"""Generated OPC UA profinet namespace declarations."""

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


@o6.referencetype(nodeId="ns=profinet;i=4002", browseName="ns=profinet;HasPnRealModule", displayName="HasPnRealModule", inverseName="IsPnRealModuleOf")
class HasPnRealModule(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4003", browseName="ns=profinet;HasPnRealSubmodule", displayName="HasPnRealSubmodule", inverseName="IsPnRealSubmoduleOf")
class HasPnRealSubmodule(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4004", browseName="ns=profinet;HasPnExpectedModule", displayName="HasPnExpectedModule", inverseName="IsPnExpectedModuleOf")
class HasPnExpectedModule(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4005", browseName="ns=profinet;HasPnExpectedSubmodule", displayName="HasPnExpectedSubmodule", inverseName="IsPnExpectedSubmoduleOf")
class HasPnExpectedSubmodule(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4006", browseName="ns=profinet;HasPnAsset", displayName="HasPnAsset", inverseName="IsPnAssetOf")
class HasPnAsset(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4007", browseName="ns=profinet;HasPnInterface", displayName="HasPnInterface", inverseName="IsPnInterfaceOf")
class HasPnInterface(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4008", browseName="ns=profinet;HasPnPort", displayName="HasPnPort", inverseName="IsPnPortOf")
class HasPnPort(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4009", browseName="ns=profinet;IsPnRealModule", displayName="IsPnRealModule", inverseName="IsPnExpectedModule")
class IsPnRealModule(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4010", browseName="ns=profinet;IsPnRealSubmodule", displayName="IsPnRealSubmodule", inverseName="IsPnExpectedSubmodule")
class IsPnRealSubmodule(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=profinet;i=4011",
    browseName="ns=profinet;IsPnApplicationRelationDeviceInterface",
    displayName="IsPnApplicationRelationDeviceInterface",
    inverseName="UsedByPnApplicationRelation",
)
class IsPnApplicationRelationDeviceInterface(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=profinet;i=4012",
    browseName="ns=profinet;IsPnApplicationRelationControllerInterface",
    displayName="IsPnApplicationRelationControllerInterface",
    inverseName="UsedByPnApplicationRelation",
)
class IsPnApplicationRelationControllerInterface(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4013", browseName="ns=profinet;IsPnInterface", displayName="IsPnInterface", inverseName="RealizedByPnSubmodule")
class IsPnInterface(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4014", browseName="ns=profinet;IsPnPort", displayName="IsPnPort", inverseName="RealizedByPnSubmodule")
class IsPnPort(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4015", browseName="ns=profinet;CommLinkTo", displayName="CommLinkTo", inverseName="CommLinkFrom")
class CommLinkTo(ns0.reftypes.Organizes):
    pass


@o6.referencetype(nodeId="ns=profinet;i=4016", browseName="ns=profinet;HasPnApplicationRelation", displayName="HasPnApplicationRelation", inverseName="IsPnApplicationRelationOf")
class HasPnApplicationRelation(ns0.reftypes.HasComponent):
    pass


del Any, TYPE_CHECKING, uuid, o6, ns0
