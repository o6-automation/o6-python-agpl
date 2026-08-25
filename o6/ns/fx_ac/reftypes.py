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

"""Generated OPC UA fx_ac namespace declarations."""

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


@o6.referencetype(nodeId="ns=fx_ac;i=34", browseName="ns=fx_ac;HasBuiltInAsset", displayName="HasBuiltInAsset", inverseName="BuiltInAssetOf")
class HasBuiltInAsset(ns0.reftypes.HasContainedComponent):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=35", browseName="ns=fx_ac;HasPart", displayName="HasPart", inverseName="PartOf")
class HasPart(ns0.reftypes.HasContainedComponent):
    pass


@o6.referencetype(
    nodeId="ns=fx_ac;i=37",
    browseName="ns=fx_ac;ConnectedTo",
    displayName="ConnectedTo",
    description="This Reference indicates that the asset the reference points to is a part connected to the asset which is the starting point of the Reference by means of an electrical cable.",
    symmetric=True,
)
class ConnectedTo(ns0.reftypes.IsPhysicallyConnectedTo):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=41", browseName="ns=fx_ac;HasConnectionEndpoint", displayName="HasConnectionEndpoint", inverseName="ConnectionEndpointOf")
class HasConnectionEndpoint(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=42", browseName="ns=fx_ac;ToDataSetReader", displayName="ToDataSetReader", inverseName="FromDataSetReader")
class ToDataSetReader(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=43", browseName="ns=fx_ac;HasSubFunctionalEntity", displayName="HasSubFunctionalEntity", inverseName="SubFunctionalEntityOf")
class HasSubFunctionalEntity(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=44", browseName="ns=fx_ac;HasControlGroup", displayName="HasControlGroup", inverseName="ControlGroupOf")
class HasControlGroup(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=46", browseName="ns=fx_ac;ToDataSetWriter", displayName="ToDataSetWriter", inverseName="FromDataSetWriter")
class ToDataSetWriter(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=1056", browseName="ns=fx_ac;HasInputGroup", displayName="HasInputGroup", inverseName="InputGroupOf")
class HasInputGroup(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=1058", browseName="ns=fx_ac;HasOutputGroup", displayName="HasOutputGroup", inverseName="OutputGroupOf")
class HasOutputGroup(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=4002", browseName="ns=fx_ac;HasCapability", displayName="HasCapability", inverseName="CapabilityOf")
class HasCapability(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=4004", browseName="ns=fx_ac;IsPartOfRedundantAssetSet", displayName="IsPartOfRedundantAssetSet", symmetric=True)
class IsPartOfRedundantAssetSet(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="ns=fx_ac;i=4005", browseName="ns=fx_ac;DescribedInDescriptor", displayName="DescribedInDescriptor", inverseName="DescriptorDescribes")
class DescribedInDescriptor(ns0.reftypes.NonHierarchicalReferences):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0
