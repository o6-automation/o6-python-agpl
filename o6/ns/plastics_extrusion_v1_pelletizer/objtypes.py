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

"""Generated OPC UA plastics_extrusion_v1_pelletizer namespace declarations."""

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


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_pelletizer;i=1002", browseName="ns=plastics_extrusion_v1_pelletizer;DiePlateType", displayName="DiePlateType")
class DiePlateType(ns0.objtypes.BaseObjectType):
    activeTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_pelletizer;i=6006", browseName="ns=plastics_extrusion_v1_pelletizer;ActiveTime", dataType=ns0.datatypes.Duration)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_pelletizer;i=6001", browseName="ns=plastics_extrusion_v1_pelletizer;Name", dataType=o6.LocalizedText)
    )


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_pelletizer;i=1003", browseName="ns=plastics_extrusion_v1_pelletizer;KnifePackageType", displayName="KnifePackageType")
class KnifePackageType(ns0.objtypes.BaseObjectType):
    activeTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_pelletizer;i=6010", browseName="ns=plastics_extrusion_v1_pelletizer;ActiveTime", dataType=ns0.datatypes.Duration)
    )
    amount: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_pelletizer;i=6009", browseName="ns=plastics_extrusion_v1_pelletizer;Amount", dataType=o6.UInt16)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_pelletizer;i=6008", browseName="ns=plastics_extrusion_v1_pelletizer;Name", dataType=o6.LocalizedText)
    )


@o6.objecttype(
    nodeId="ns=plastics_extrusion_v1_pelletizer;i=1004", browseName="ns=plastics_extrusion_v1_pelletizer;Pelletizer_InterfaceType", displayName="Pelletizer_InterfaceType"
)
class Pelletizer_InterfaceType(plastics_extrusion_v1.objtypes.ExtrusionDeviceType):
    cutGap: ns0.vartypes.AnalogUnitType | None
    diePlate_LangleNrRangle: DiePlateType | None
    drive: plastics_rubber.objtypes.DriveType
    knifePackage_LangleNrRangle: KnifePackageType | None
    pelletizerClosed: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_pelletizer;i=6108", browseName="ns=plastics_extrusion_v1_pelletizer;PelletizerClosed", dataType=o6.Boolean)
    )
    pressureZones: plastics_rubber.objtypes.MeasuringDevicesType | None
    temperatureZones: plastics_extrusion_v1.objtypes.ExtrusionTemperatureZonesType | None
    waterFlowActive: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_pelletizer;i=6109", browseName="ns=plastics_extrusion_v1_pelletizer;WaterFlowActive", dataType=o6.Boolean)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_rubber
