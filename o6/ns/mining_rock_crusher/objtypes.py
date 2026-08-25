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

"""Generated OPC UA mining_rock_crusher namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=mining_rock_crusher;i=1003", browseName="ns=mining_rock_crusher;RockCrusherControlType", displayName="RockCrusherControlType")
class RockCrusherControlType(mining.objtypes.MiningEquipmentType):
    methodSet: ns0.objtypes.BaseObjectType
    miningEquipmentIdentification: mining.objtypes.MiningEquipmentIdentificationType
    parameterSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=mining_rock_crusher;i=1002", browseName="ns=mining_rock_crusher;RockCrusherType", displayName="RockCrusherType")
class RockCrusherType(mining.objtypes.MiningEquipmentType):
    components: machinery.objtypes.MachineComponentsType = o6.hasAddIn(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=mining_rock_crusher;i=5001",
            browseName="ns=mining;Components",
            description="The components add-in contains placeholders for sub-components of an equipment asset",
        )
    )
    miningEquipmentIdentification: mining.objtypes.MiningEquipmentIdentificationType


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0
