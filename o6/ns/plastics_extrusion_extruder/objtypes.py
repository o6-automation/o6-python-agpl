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

"""Generated OPC UA plastics_extrusion_extruder namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion as plastics_extrusion
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_extruder_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=plastics_extrusion_extruder;i=1002", browseName="ns=plastics_extrusion_extruder;FeedersType", displayName="FeedersType")
class FeedersType(ns0.objtypes.BaseObjectType):
    feeder_LangleNrRangle: FeederType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6041", browseName="NodeVersion", dataType=o6.String, value="")
    )


o6.reference(FeedersType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_extrusion_extruder;i=1003", browseName="ns=plastics_extrusion_extruder;HopperType", displayName="HopperType")
class HopperType(ns0.objtypes.BaseObjectType):
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6070", browseName="ns=plastics_extrusion_extruder;Id", dataType=o6.String)
    )
    material: plastics_rubber.objtypes.MaterialType
    materialLevel: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_extruder;i=6080", browseName="ns=plastics_extrusion_extruder;MaterialLevel", dataType=o6.Double)
    )
    materialLot: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6077", browseName="ns=plastics_extrusion_extruder;MaterialLot", dataType=o6.String)
    )
    materialTemperature: plastics_rubber.objtypes.MonitoredParameterType | None
    weight: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=plastics_extrusion_extruder;i=1063", browseName="ns=plastics_extrusion_extruder;FeederType", displayName="FeederType")
class FeederType(plastics_rubber.objtypes.DriveType):
    hopper: HopperType | None
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6083", browseName="ns=plastics_extrusion_extruder;Id", dataType=o6.String)
    )
    isControlled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6005", browseName="ns=plastics_extrusion_extruder;IsControlled", dataType=o6.Boolean)
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6004", browseName="ns=plastics_extrusion_extruder;IsPresent", dataType=o6.Boolean, value=False)
    )
    mode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_extruder;i=6040", browseName="ns=plastics_extrusion_extruder;Mode", dataType=plastics_extrusion_extruder_datypes.FeedingModeEnumeration
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_extruder;i=6002", browseName="ns=plastics_extrusion_extruder;Name", dataType=o6.LocalizedText, value=o6.LocalizedText()
        )
    )
    target: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6085", browseName="ns=plastics_extrusion_extruder;Target", dataType=o6.String)
    )
    throughput: plastics_rubber.objtypes.MonitoredParameterType | None


@o6.objecttype(nodeId="ns=plastics_extrusion_extruder;i=1015", browseName="ns=plastics_extrusion_extruder;Extruder_InterfaceType", displayName="Extruder_InterfaceType")
class Extruder_InterfaceType(plastics_extrusion.objtypes.ExtrusionDeviceType):
    additionalDrives: plastics_rubber.objtypes.DrivesType | None
    barrelId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6521", browseName="ns=plastics_extrusion_extruder;BarrelId", dataType=o6.String, value="")
    )
    feeders: FeedersType | None
    mainDrive: plastics_rubber.objtypes.DriveType | None
    meltPressureZones: plastics_rubber.objtypes.MeasuringDevicesType | None
    meltTemperatureZones: plastics_rubber.objtypes.MeasuringDevicesType | None
    screwId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_extruder;i=6001", browseName="ns=plastics_extrusion_extruder;ScrewId", dataType=o6.String)
    )
    screwTemperatures: plastics_extrusion.objtypes.ExtrusionTemperatureZonesType | None
    specificOutput: ns0.vartypes.AnalogUnitType | None
    temperatureZones: plastics_extrusion.objtypes.ExtrusionTemperatureZonesType
    throughput: plastics_rubber.objtypes.MonitoredParameterType | None
    users: plastics_rubber.objtypes.UsersType
    vacuumZones: plastics_rubber.objtypes.MeasuringDevicesType | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_extrusion, plastics_rubber, plastics_extrusion_extruder_datypes
