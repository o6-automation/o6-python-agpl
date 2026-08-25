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

"""Generated OPC UA mining_armoured_face_conveyor namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import datatypes as mining_armoured_face_conveyor_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=mining_armoured_face_conveyor;i=2001",
    browseName="ns=mining_armoured_face_conveyor;AFCStateType",
    displayName="AFCStateType",
    description="Current State of operation of the AFC",
    dataType=mining_armoured_face_conveyor_datypes.AFCStateEnum,
    value=mining_armoured_face_conveyor_datypes.AFCStateEnum.UNDEFINED,
)
class AFCStateType(ns0.vartypes.BaseDataVariableType):
    aFCNormalRunningDirection: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mining_armoured_face_conveyor;i=6021",
            browseName="ns=mining_armoured_face_conveyor;AFCNormalRunningDirection",
            description="Direction of the normal AFC operation",
            dataType=mining_armoured_face_conveyor_datypes.AFCNormalRunningDirectionEnum,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0, mining_armoured_face_conveyor_datypes
