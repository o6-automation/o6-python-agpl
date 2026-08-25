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

"""Generated OPC UA pngsdgm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.referencetype(nodeId="ns=pngsdgm;i=4002", browseName="ns=pngsdgm;HasInputData", displayName="HasInputData", inverseName="HasInputApplication")
class HasInputData(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(nodeId="ns=pngsdgm;i=4003", browseName="ns=pngsdgm;HasOutputData", displayName="HasOutputData", inverseName="HasOutputApplication")
class HasOutputData(ns0.reftypes.HasComponent):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ns0
