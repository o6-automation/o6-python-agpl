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

"""Generated OPC UA robotics namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.referencetype(
    nodeId="ns=robotics;i=4002",
    browseName="ns=robotics;Controls",
    displayName="Controls",
    description="Reference: Describe dependencies between objects which have a controlling character.",
    inverseName="IsControlledBy",
)
class Controls(ns0.reftypes.HierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=robotics;i=18178",
    browseName="ns=robotics;Moves",
    displayName="Moves",
    description="Reference: Describe the coupling between a powertrain and the axes from the powertrain point of view.",
    inverseName="IsMovedBy",
)
class Moves(ns0.reftypes.HierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=robotics;i=18179",
    browseName="ns=robotics;Requires",
    displayName="Requires",
    description="Reference: Describe the coupling between a powertrain and axes from the axis point of view. An axis has a Requires reference to all powertrains that need to move such that only this single axis moves.",
    inverseName="IsRequiredBy",
)
class Requires(ns0.reftypes.HierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=robotics;i=18180",
    browseName="ns=robotics;IsDrivenBy",
    displayName="IsDrivenBy",
    description="Reference: Describe dependencies between objects which have a driving or powering character. The BrowseName IsDrivenBy and the InverseName Drives describe semantically the hierarchical dependency.",
    inverseName="Drives",
)
class IsDrivenBy(ns0.reftypes.HierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=robotics;i=18181",
    browseName="ns=robotics;IsConnectedTo",
    displayName="IsConnectedTo",
    description="Reference: Describe dependencies between objects which are mounted or mechanically linked or connected to each other. The IsConnectedTo reference is symmetric and has no InverseName.",
    inverseName="IsConnectedTo",
    symmetric=True,
)
class IsConnectedTo(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=robotics;i=18182",
    browseName="ns=robotics;HasSafetyStates",
    displayName="HasSafetyStates",
    description="Reference: Describe dependencies between objects to show which (controller) object is responsible for the execution of the safety-functionality. The BrowseName HasSafetyStates and the InverseName SafetyStatesOf describe semantically the hierarchical dependency.",
    inverseName="SafetyStatesOf",
)
class HasSafetyStates(ns0.reftypes.HierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=robotics;i=18183",
    browseName="ns=robotics;HasSlave",
    displayName="HasSlave",
    description="Reference: Provide the master-slave relationship of powertrains which provide torque for a common axis. The InverseName is IsSlaveOf.",
    inverseName="IsSlaveOf",
)
class HasSlave(ns0.reftypes.HierarchicalReferences):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0
