# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA additive_manufacturing namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
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


@o6.enumtype(
    nodeId="ns=additive_manufacturing;i=3000",
    browseName="ns=additive_manufacturing;FeedstockFunction",
    description="This enumeration indicates the function of a specific feedstock.",
)
class FeedstockFunction(ns0.datatypes.Enumeration):
    UNDEFINED = o6.enumfield(0, name="Undefined")
    MAIN = o6.enumfield(1, name="Main")
    ANCILLARY = o6.enumfield(2, name="Ancillary")
    CONSUMABLE = o6.enumfield(3, name="Consumable")


@o6.datatype(nodeId="ns=additive_manufacturing;i=3001", browseName="ns=additive_manufacturing;RunInfoDataType", defaultEncodingId="ns=additive_manufacturing;i=5036")
class RunInfoDataType(ns0.datatypes.Structure):
    currentLayer: o6.UInt32 | None = o6.field(name="CurrentLayer")
    identifier: o6.String = o6.field(name="Identifier")
    state: isa95_jobcontrol_v2.datatypes.ISA95StateDataType = o6.field(name="State")
    remainingTime: o6.Double | None = o6.field(name="RemainingTime")


@o6.enumtype(
    nodeId="ns=additive_manufacturing;i=3002", browseName="ns=additive_manufacturing;SensorSeverity", description="This enumeration indicates the severity of a specific sensor."
)
class SensorSeverity(ns0.datatypes.Enumeration):
    INFO = o6.enumfield(0, name="Info")
    CRITICAL = o6.enumfield(1, name="Critical")


@o6.enumtype(
    nodeId="ns=additive_manufacturing;i=3003", browseName="ns=additive_manufacturing;SensorCategory", description="This enumeration indicates the severity of a specific sensor."
)
class SensorCategory(ns0.datatypes.Enumeration):
    MACHINE_HEALTH = o6.enumfield(0, name="MachineHealth")
    MAINTENANCE_TRACKING = o6.enumfield(1, name="MaintenanceTracking")
    PROCESS_MONITORING = o6.enumfield(2, name="ProcessMonitoring")


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_processvalues, ns0, padim
