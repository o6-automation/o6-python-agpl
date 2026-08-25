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

"""Generated OPC UA ecm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=ecm;i=3002", browseName="StandbyModeTransitionDataType", defaultEncodingId="ns=ecm;i=5001")
class StandbyModeTransitionDataType(ns0.datatypes.Structure):
    iDDestination: o6.Byte
    currentTimeToDestination: o6.Double
    currentTimeToOperate: o6.Double
    energyConsumptionToDestination: o6.Float


@o6.datatype(nodeId="ns=ecm;i=3003", browseName="EnergyStateInformationDataType", defaultEncodingId="ns=ecm;i=5004")
class EnergyStateInformationDataType(ns0.datatypes.Structure):
    iDSource: o6.Byte
    iDDestination: o6.Byte
    regularTimeToOperate: o6.Double
    modePowerConsumption: o6.Float


@o6.datatype(nodeId="ns=ecm;i=3005", browseName="AcPeDataType", defaultEncodingId="ns=ecm;i=5010")
class AcPeDataType(ns0.datatypes.Structure):
    l1: o6.Float
    l2: o6.Float
    l3: o6.Float


@o6.datatype(nodeId="ns=ecm;i=3006", browseName="AcPpDataType", defaultEncodingId="ns=ecm;i=5013")
class AcPpDataType(ns0.datatypes.Structure):
    l1L2: o6.Float
    l2L3: o6.Float
    l3L1: o6.Float


@o6.enumtype(nodeId="ns=ecm;i=3010", browseName="MeasurementPeriodEnum")
class MeasurementPeriodEnum(ns0.datatypes.Enumeration):
    SLIDING_DEMAND = o6.enumfield(0, name="SlidingDemand")
    FIXED_BLOCK_COMPLETED = o6.enumfield(1, name="FixedBlockCompleted")
    FIXED_BLOCK_INSTANTANEOUS = o6.enumfield(2, name="FixedBlockInstantaneous")
    FIXED_BLOCK_PREDICTED = o6.enumfield(3, name="FixedBlockPredicted")


@o6.datatype(nodeId="ns=ecm;i=3007", browseName="MeasurementPeriodDataType", defaultEncodingId="ns=ecm;i=5008")
class MeasurementPeriodDataType(ns0.datatypes.Structure):
    duration: o6.Double
    definition: MeasurementPeriodEnum


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0
