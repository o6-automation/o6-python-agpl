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

"""Generated OPC UA machinery_energy namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ecm as ecm
import o6.ns.ia as ia
import o6.ns.ns0 as ns0
from . import reftypes as machinery_energy_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=machinery_energy;i=1003", browseName="ns=machinery_energy;INonElectricalEnergyType", displayName="INonElectricalEnergyType", isAbstract=True)
class INonElectricalEnergyType(ns0.objtypes.BaseInterfaceType):
    neEnergyExportHp: ecm.vartypes.EnergyMeasurementValueType
    neEnergyImportHp: ecm.vartypes.EnergyMeasurementValueType


@o6.objecttype(nodeId="ns=machinery_energy;i=1006", browseName="ns=machinery_energy;IBaseFlowType", displayName="IBaseFlowType", isAbstract=True)
class IBaseFlowType(ns0.objtypes.BaseInterfaceType):
    pressure: ecm.vartypes.EnergyMeasurementValueType | None
    temperature: ecm.vartypes.EnergyMeasurementValueType | None


@o6.objecttype(nodeId="ns=machinery_energy;i=1004", browseName="ns=machinery_energy;IVolumeFlowType", displayName="IVolumeFlowType", isAbstract=True)
class IVolumeFlowType(IBaseFlowType):
    volume: ecm.vartypes.EnergyMeasurementValueType | None
    volumeFlowRate: ecm.vartypes.EnergyMeasurementValueType | None


@o6.objecttype(nodeId="ns=machinery_energy;i=1008", browseName="ns=machinery_energy;IMassFlowType", displayName="IMassFlowType", isAbstract=True)
class IMassFlowType(IBaseFlowType):
    mass: ecm.vartypes.EnergyMeasurementValueType | None
    massFlowRate: ecm.vartypes.EnergyMeasurementValueType | None


del Any, TYPE_CHECKING, uuid, o6, di, ecm, ia, ns0, machinery_energy_reftypes
