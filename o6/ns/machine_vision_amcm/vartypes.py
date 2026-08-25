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

"""Generated OPC UA machine_vision_amcm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import reftypes as machine_vision_amcm_reftypes
from . import datatypes as machine_vision_amcm_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=machine_vision_amcm;i=2002",
    browseName="ns=machine_vision_amcm;SEMI_E10SystemStateType",
    displayName="SEMI_E10SystemStateType",
    description="It is used to denote a single level with one or multiple SEMI E10 states that might be active in an item",
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=o6.ValueRank.SCALAR_OR_1D,
)
class SEMI_E10SystemStateType(ns0.vartypes.BaseDataVariableType):
    causePath: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6196",
            browseName="ns=machine_vision_amcm;CausePath",
            description="is a path information string based on the SEMI E10 scheme. Instantiated SEMI_E10SystemStateTypes using the SubStates component do not need to provide this property",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    statesInfo: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6195",
            browseName="ns=machine_vision_amcm;StatesInfo",
            description="mandatory property of all the states that can be assigned to the level of variable",
            dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    subStates: SEMI_E10SystemStateType | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, machine_vision_amcm_reftypes, machine_vision_amcm_datypes
