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

"""Generated OPC UA mining_dozer namespace declarations."""

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


@o6.enumtype(nodeId="ns=mining_dozer;i=3002", browseName="DozerJobMissionEnum")
class DozerJobMissionEnum(ns0.datatypes.Enumeration):
    CLEANUP_OPERATIONS = o6.enumfield(0, name="CleanupOperations")
    RIPPING_OPERATIONS = o6.enumfield(1, name="RippingOperations")
    TOPSOIL_REMOVAL = o6.enumfield(2, name="TopsoilRemoval")
    OVERBURDEN_REMOVAL = o6.enumfield(3, name="OverburdenRemoval")
    CONSTRUCTION_OF_ROADS = o6.enumfield(4, name="ConstructionOfRoads")
    CONSTRUCTION_OF_BERMS = o6.enumfield(5, name="ConstructionOfBerms")
    BENCH_PREPARATION = o6.enumfield(6, name="BenchPreparation")
    BLAST_CLEANUP = o6.enumfield(7, name="BlastCleanup")
    DOZER_PUSH_INTO_VOIDS = o6.enumfield(8, name="DozerPushIntoVoids")
    DOZER_PUSH_INTO_TRAPS = o6.enumfield(9, name="DozerPushIntoTraps")
    STOCKPILES = o6.enumfield(10, name="Stockpiles")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0
