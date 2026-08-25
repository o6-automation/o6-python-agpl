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

"""Generated OPC UA powertrain namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_ac as fx_ac
import o6.ns.fx_data as fx_data
import o6.ns.ia as ia
import o6.ns.irdi_v1_0_0 as irdi_v1_0_0
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.referencetype(nodeId="ns=powertrain;i=4004", browseName="ns=powertrain;HasPtAttributes", displayName="HasPtAttributes", inverseName="PtAttributesOf")
class HasPtAttributes(ns0.reftypes.HasComponent):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, fx_ac, fx_data, ia, irdi_v1_0_0, machinery, ns0
