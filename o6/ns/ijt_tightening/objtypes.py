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

"""Generated OPC UA ijt_tightening namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.amb as amb
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ijt_base as ijt_base
import o6.ns.machinery as machinery
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=ijt_tightening;i=1003",
    browseName="ns=ijt_tightening;ITighteningToolParametersType",
    displayName="ITighteningToolParametersType",
    description="This interface is inherited from 0:BaseInterfaceType to add additional parameters of a tool in a tightening system. It shall be added to 2:Parameters object of the tool instance.",
    isAbstract=True,
)
class ITighteningToolParametersType(ns0.objtypes.BaseInterfaceType):
    designType: ns0.vartypes.MultiStateDiscreteType
    driveMethod: ns0.vartypes.MultiStateDiscreteType
    driveType: ns0.vartypes.MultiStateDiscreteType
    maxSpeed: ijt_base.vartypes.JoiningDataVariableType | None
    maxTorque: ijt_base.vartypes.JoiningDataVariableType | None
    minTorque: ijt_base.vartypes.JoiningDataVariableType | None
    motorType: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ijt_tightening;i=6023", browseName="ns=ijt_tightening;MotorType", description="MotorType is the type of motor in the tool.", dataType=o6.String, value=""
        )
    )
    shutOffMethod: ns0.vartypes.MultiStateDiscreteType | None


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, ijt_base, machinery, machinery_result, ns0
