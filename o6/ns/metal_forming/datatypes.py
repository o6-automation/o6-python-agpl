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

"""Generated OPC UA metal_forming namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi_v1_00 as irdi_v1_00
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=metal_forming;i=3003", browseName="CyclicProcessValueDataType", defaultEncodingId="ns=metal_forming;i=5001")
class CyclicProcessValueDataType(ns0.datatypes.Structure):
    analogSignal: o6.ExtensionObject
    setpoint: o6.ExtensionObject
    cycleCount: o6.UInt32
    isActive: o6.Boolean


@o6.datatype(nodeId="ns=metal_forming;i=3004", browseName="CyclicPartInformationDataType", defaultEncodingId="ns=metal_forming;i=5006")
class CyclicPartInformationDataType(ns0.datatypes.Structure):
    cycleCount: o6.UInt32
    partId: o6.String | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi_v1_00, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_processvalues, ns0, padim
