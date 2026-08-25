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

"""Generated OPC UA mt_connect namespace declarations."""

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


@o6.referencetype(nodeId="ns=mt_connect;i=2672", browseName="ns=mt_connect;HasMTReference", displayName="HasMTReference", symmetric=True)
class HasMTReference(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=mt_connect;i=2680",
    browseName="ns=mt_connect;HasMTClassType",
    displayName="HasMTClassType",
    description="A \\gls{MTDataItem} is representated in OPC UA as a sub-type of the most\n      appropriate \\uamodel{BaseDataVariableType}. The type is derived from the\n      MTConnect \\gls{type} attribute and references the corect\n      \\mtmodel{..ClassType}",
)
class HasMTClassType(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=mt_connect;i=2683",
    browseName="ns=mt_connect;HasMTSubClassType",
    displayName="HasMTSubClassType",
    description="A \\gls{MTDataItem} is representated in OPC UA as a sub-type of the most\n      appropriate \\uamodel{BaseDataVariableType}. The sub-type is derived from\n      the MTConnect \\gls{subType} attribute and references the corect\n      \\mtmodel{..ClassType}.",
)
class HasMTSubClassType(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=mt_connect;i=2687", browseName="ns=mt_connect;HasMTComposition", displayName="HasMTComposition", symmetric=True)
class HasMTComposition(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=mt_connect;i=2689",
    browseName="ns=mt_connect;HasMTSource",
    displayName="HasMTSource",
    description="The \\mtmodel{Source} relation to a \\gls{MTComponent} or \\gls{MTDataItem}.",
    symmetric=True,
)
class HasMTSource(ns0.reftypes.NonHierarchicalReferences):
    pass


del Any, TYPE_CHECKING, uuid, o6, ns0
