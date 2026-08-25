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

"""Generated OPC UA plastics_extrusion_v1 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_v1_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1016", browseName="ns=plastics_extrusion_v1;ExtrusionTemperatureZoneType", displayName="ExtrusionTemperatureZoneType")
class ExtrusionTemperatureZoneType(plastics_rubber.objtypes.MeasuringDeviceType):
    controllerOutput: ns0.vartypes.AnalogUnitType | None
    electricalCurrent: plastics_rubber.objtypes.MonitoredParameterType | None
    nominalCoolingPower: ns0.vartypes.AnalogUnitType | None
    nominalHeatingPower: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1002", browseName="ns=plastics_extrusion_v1;ExtrusionDeviceType", displayName="ExtrusionDeviceType", isAbstract=True)
class ExtrusionDeviceType(ns0.objtypes.BaseObjectType):
    additionalMeasuringDevices: plastics_rubber.objtypes.MeasuringDevicesType | None
    electricalEnergy: plastics_rubber.objtypes.EnergyType | None
    fluidEnergy: plastics_rubber.objtypes.EnergyType | None
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6035", browseName="ns=plastics_extrusion_v1;IsPresent", dataType=o6.Boolean)
    )
    lineId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6020", browseName="ns=plastics_extrusion_v1;LineId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    machineConfiguration: plastics_rubber.objtypes.MachineConfigurationType | None
    machineInformation: plastics_rubber.objtypes.MachineInformationType
    maintenance: plastics_rubber.objtypes.MaintenanceType | None
    pressureAir: plastics_rubber.objtypes.EnergyType | None
    productionDatasetManagement: plastics_rubber.objtypes.ProductionDatasetManagementType | None
    startDevice: plastics_rubber.objtypes.StartDeviceType | None
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1;i=6038", browseName="ns=plastics_extrusion_v1;Status", dataType=plastics_extrusion_v1_datypes.ComponentStatusEnumeration
        )
    )
    strand: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6037", browseName="ns=plastics_extrusion_v1;Strand", dataType=o6.UInt32)
    )
    target: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6036", browseName="ns=plastics_extrusion_v1;Target", dataType=o6.String, valueRank=-3)
    )


o6.reference(ExtrusionDeviceType, "i=41", "ns=plastics_rubber;i=1004")
o6.reference(ExtrusionDeviceType, "i=41", "ns=plastics_rubber;i=1011")


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1007", browseName="ns=plastics_extrusion_v1;RollBendingType", displayName="RollBendingType")
class RollBendingType(ns0.objtypes.BaseObjectType):
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6305", browseName="NodeVersion", dataType=o6.String))
    referencePoint_LangleNrRangle: plastics_rubber.objtypes.MeasuringDeviceType | None


o6.reference(RollBendingType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1003", browseName="ns=plastics_extrusion_v1;GapType", displayName="GapType")
class GapType(ns0.objtypes.BaseObjectType):
    contactForce: plastics_rubber.objtypes.MonitoredParameterType | None
    distanceLeft: plastics_rubber.objtypes.MonitoredParameterType | None
    distanceRight: plastics_rubber.objtypes.MonitoredParameterType | None
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6344", browseName="ns=plastics_extrusion_v1;Id", dataType=o6.String)
    )
    isClosed: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1;i=6345", browseName="ns=plastics_extrusion_v1;IsClosed", dataType=o6.Boolean)
    )
    rollId1: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6346", browseName="ns=plastics_extrusion_v1;RollId1", dataType=o6.String)
    )
    rollId2: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6347", browseName="ns=plastics_extrusion_v1;RollId2", dataType=o6.String)
    )
    stockingGuideIsPresent: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6348", browseName="ns=plastics_extrusion_v1;StockingGuideIsPresent", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1004", browseName="ns=plastics_extrusion_v1;GapsType", displayName="GapsType")
class GapsType(ns0.objtypes.BaseObjectType):
    gap_LangleNrRangle: GapType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6467", browseName="NodeVersion", dataType=o6.String))


o6.reference(GapsType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1005", browseName="ns=plastics_extrusion_v1;RollType", displayName="RollType")
class RollType(ns0.objtypes.BaseObjectType):
    crossAxisLeft: plastics_rubber.objtypes.MonitoredParameterType | None
    crossAxisRight: plastics_rubber.objtypes.MonitoredParameterType | None
    drive: plastics_rubber.objtypes.DriveType
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6638", browseName="ns=plastics_extrusion_v1;Id", dataType=o6.String)
    )
    masterRollId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6641", browseName="ns=plastics_extrusion_v1;MasterRollId", dataType=o6.String)
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6642", browseName="ns=plastics_extrusion_v1;Name", dataType=o6.LocalizedText)
    )
    peripheralDevices: RollPeripheralDevicesType | None
    rollBending: RollBendingType | None
    temperature: ExtrusionTemperatureZoneType


ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6772", browseName="NodeVersion", dataType=o6.String)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=6772"], "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1008", browseName="ns=plastics_extrusion_v1;RollPeripheralDevicesType", displayName="RollPeripheralDevicesType")
class RollPeripheralDevicesType(ns0.objtypes.BaseObjectType):
    cleaningSystem_LangleNrRangle: plastics_rubber.objtypes.StartDeviceType | None
    infraredHeatingSystem_LangleNrRangle: plastics_rubber.objtypes.StartDeviceType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6772"])


o6.reference(RollPeripheralDevicesType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1006", browseName="ns=plastics_extrusion_v1;RollsType", displayName="RollsType")
class RollsType(ns0.objtypes.BaseObjectType):
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6803", browseName="NodeVersion", dataType=o6.String))
    roll_LangleNrRangle: RollType | None


o6.reference(RollsType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_extrusion_v1;i=1017", browseName="ns=plastics_extrusion_v1;ExtrusionTemperatureZonesType", displayName="ExtrusionTemperatureZonesType")
class ExtrusionTemperatureZonesType(ns0.objtypes.BaseObjectType):
    maintenance: plastics_rubber.objtypes.MaintenanceType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6987", browseName="NodeVersion", dataType=o6.String, value="0")
    )
    startTempering: plastics_rubber.objtypes.StartDeviceType | None
    temperatureZone_LangleNrRangle: ExtrusionTemperatureZoneType | None


o6.reference(ExtrusionTemperatureZonesType, "i=41", "i=2133")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_extrusion_v1_datypes
