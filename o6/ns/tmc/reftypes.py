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

"""Generated OPC UA tmc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.referencetype(
    nodeId="ns=tmc;i=4006",
    browseName="ns=tmc;FlowsTo",
    displayName="FlowsTo",
    description="The semantic of this ReferenceType is to link TMC objects according to the material flow, within \na machine module and between machine modules.",
    inverseName="FlowsFrom",
)
class FlowsTo(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=tmc;i=4007",
    browseName="ns=tmc;Precedes",
    displayName="Precedes",
    description="The semantic of this ReferenceType is to link upstream process values to downstream process \nvalues.",
    inverseName="Follows",
)
class Precedes(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=tmc;i=4009",
    browseName="ns=tmc;HasUIShapeSelector",
    displayName="HasUIShapeSelector",
    description="The semantic of this ReferenceType is to link a UI resource to the conditions that will identify \nhow it is displayed.",
    inverseName="SelectsUIShape",
)
class HasUIShapeSelector(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=tmc;i=4010",
    browseName="ns=tmc;IsDisplayedBy",
    displayName="IsDisplayedBy",
    description="The semantic of this ReferenceType is to link an OPC UA construct to its UI representation.",
    inverseName="Displays",
)
class IsDisplayedBy(ns0.reftypes.NonHierarchicalReferences):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pack_ml
