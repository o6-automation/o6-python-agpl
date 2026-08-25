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

"""Generated OPC UA plastics_extrusion_v1_calibrator namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion_v1 as plastics_extrusion_v1
import o6.ns.plastics_rubber as plastics_rubber

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_extrusion_v1_calibrator;i=1004", browseName="ns=plastics_extrusion_v1_calibrator;Calibrator_InterfaceType", displayName="Calibrator_InterfaceType"
)
class Calibrator_InterfaceType(plastics_extrusion_v1.objtypes.ExtrusionDeviceType):
    calibrationZones: CalibrationZonesType
    positionZ: plastics_rubber.objtypes.MeasuringDeviceType | None
    positionsPipeSupport: plastics_rubber.objtypes.MeasuringDevicesType | None
    positionsX: plastics_rubber.objtypes.MeasuringDevicesType | None
    positionsY: plastics_rubber.objtypes.MeasuringDevicesType | None


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_calibrator;i=1003", browseName="ns=plastics_extrusion_v1_calibrator;CalibrationZonesType", displayName="CalibrationZonesType")
class CalibrationZonesType(ns0.objtypes.BaseObjectType):
    calibrationZone_LangleNrRangle: CalibrationZoneType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calibrator;i=6155", browseName="NodeVersion", dataType=o6.String)
    )
    waterFlowIn: plastics_rubber.objtypes.MeasuringDeviceType | None
    waterFlowOut: plastics_rubber.objtypes.MeasuringDeviceType | None
    waterTemperatureIn: plastics_rubber.objtypes.MeasuringDeviceType | None
    waterTemperatureOut: plastics_rubber.objtypes.MeasuringDeviceType | None


o6.reference(CalibrationZonesType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_calibrator;i=1002", browseName="ns=plastics_extrusion_v1_calibrator;CalibrationZoneType", displayName="CalibrationZoneType")
class CalibrationZoneType(ns0.objtypes.BaseObjectType):
    additionalMeasuringDevices: plastics_rubber.objtypes.MeasuringDevicesType | None
    airShowerPressure: plastics_rubber.objtypes.MeasuringDeviceType | None
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calibrator;i=6002", browseName="ns=plastics_extrusion_v1_calibrator;IsPresent", dataType=o6.Boolean)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_calibrator;i=6001", browseName="ns=plastics_extrusion_v1_calibrator;Name", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1
        )
    )
    position: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calibrator;i=6324", browseName="ns=plastics_extrusion_v1_calibrator;Position", dataType=o6.String)
    )
    vacuum: plastics_rubber.objtypes.MeasuringDeviceType | None
    vacuumPumps: plastics_rubber.objtypes.DrivesType | None
    waterFlow: plastics_rubber.objtypes.MeasuringDeviceType | None
    waterLevel: plastics_rubber.objtypes.MeasuringDeviceType | None
    waterPumps: plastics_rubber.objtypes.DrivesType | None
    waterTemperature: plastics_rubber.objtypes.MeasuringDeviceType | None


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_rubber
