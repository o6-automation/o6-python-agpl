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

"""Generated OPC UA plastics_extrusion_v1_filter namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion_v1 as plastics_extrusion_v1
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_v1_filter_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_filter;i=1002", browseName="ns=plastics_extrusion_v1_filter;Filter_InterfaceType", displayName="Filter_InterfaceType")
class Filter_InterfaceType(plastics_extrusion_v1.objtypes.ExtrusionDeviceType):
    additionalMeasuringDevices: plastics_rubber.objtypes.MeasuringDevicesType | None
    area: ns0.vartypes.AnalogUnitType | None
    backflushPressure: ns0.vartypes.AnalogUnitType | None
    drive: plastics_rubber.objtypes.DriveType | None
    filterPackage_LangleNrRangle: FilterPackageType | None
    filtrationFineness: ns0.vartypes.AnalogUnitType
    hydraulicPressure: plastics_rubber.objtypes.MeasuringDeviceType | None
    meltPressureZones: plastics_rubber.objtypes.MeasuringDevicesType | None
    meltTemperatureZones: plastics_rubber.objtypes.MeasuringDevicesType | None
    specificWasteOutput: plastics_rubber.objtypes.MonitoredParameterType | None
    temperatureZones: plastics_extrusion_v1.objtypes.ExtrusionTemperatureZonesType
    wasteOutput: plastics_rubber.objtypes.MonitoredParameterType | None


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_filter;i=1003", browseName="ns=plastics_extrusion_v1_filter;ScreenPackageType", displayName="ScreenPackageType")
class ScreenPackageType(ns0.objtypes.BaseObjectType):
    area: ns0.vartypes.AnalogUnitType | None
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6151", browseName="ns=plastics_extrusion_v1_filter;Name", dataType=o6.LocalizedText)
    )
    packageSetup: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6153", browseName="ns=plastics_extrusion_v1_filter;PackageSetup", dataType=o6.String, value="")
    )
    serialNr: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6154", browseName="ns=plastics_extrusion_v1_filter;SerialNr", dataType=o6.String, value="")
    )


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_filter;i=1004", browseName="ns=plastics_extrusion_v1_filter;FilterPackageType", displayName="FilterPackageType")
class FilterPackageType(ns0.objtypes.BaseObjectType):
    area: ns0.vartypes.AnalogUnitType | None
    backflushCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6169", browseName="ns=plastics_extrusion_v1_filter;BackflushCounter", dataType=o6.UInt32)
    )
    backflushTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_filter;i=6168",
            browseName="ns=plastics_extrusion_v1_filter;BackflushTime",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6276", browseName="ns=plastics_extrusion_v1_filter;Name", dataType=o6.LocalizedText)
    )
    screenPackage_LangleNrRangle: ScreenPackageType | None
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_filter;i=6165",
            browseName="ns=plastics_extrusion_v1_filter;Status",
            dataType=plastics_extrusion_v1_filter_datypes.FilterPackageStatusEnumeration,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_rubber, plastics_extrusion_v1_filter_datypes
