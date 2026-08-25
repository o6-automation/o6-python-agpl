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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=machine_vision_amcm;i=3002", browseName="SEMI_E10SystemStateDataType", defaultEncodingId="ns=machine_vision_amcm;i=5215")
class SEMI_E10SystemStateDataType(ns0.datatypes.Structure):
    id: o6.UInt32
    priority: o6.UInt32


@o6.datatype(nodeId="ns=machine_vision_amcm;i=3003", browseName="SEMI_E10SystemStateInfoDataType", defaultEncodingId="ns=machine_vision_amcm;i=5218")
class SEMI_E10SystemStateInfoDataType(ns0.datatypes.Structure):
    id: o6.UInt32
    name: o6.LocalizedText
    parentStateId: o6.UInt32
    description: o6.LocalizedText


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, machine_vision_amcm_reftypes
