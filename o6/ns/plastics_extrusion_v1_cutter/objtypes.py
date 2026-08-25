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

"""Generated OPC UA plastics_extrusion_v1_cutter namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion_v1 as plastics_extrusion_v1
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_v1_cutter_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_cutter;i=1002", browseName="ns=plastics_extrusion_v1_cutter;CutEventType", displayName="CutEventType", isAbstract=True)
class CutEventType(ns0.objtypes.BaseEventType):
    actualOutput: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_cutter;i=6002", browseName="ns=plastics_extrusion_v1_cutter;ActualOutput", dataType=o6.UInt64)
    )
    cuttingProductId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_cutter;i=6001", browseName="ns=plastics_extrusion_v1_cutter;CuttingProductId", dataType=o6.String)
    )
    totalOutput: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_cutter;i=6003", browseName="ns=plastics_extrusion_v1_cutter;TotalOutput", dataType=o6.UInt64)
    )


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_cutter;i=1004", browseName="ns=plastics_extrusion_v1_cutter;CuttingProductsType", displayName="CuttingProductsType")
class CuttingProductsType(ns0.objtypes.BaseObjectType):
    actualCuttingProductId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_extrusion_v1_cutter;i=6029",
            browseName="ns=plastics_extrusion_v1_cutter;ActualCuttingProductId",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    cuttingProduct_LangleNrRangle: CuttingProductType


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_cutter;i=1003", browseName="ns=plastics_extrusion_v1_cutter;CuttingProductType", displayName="CuttingProductType")
class CuttingProductType(ns0.objtypes.BaseObjectType):
    actualOutput: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_cutter;i=6021", browseName="ns=plastics_extrusion_v1_cutter;ActualOutput", dataType=o6.UInt64)
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_cutter;i=6009", browseName="ns=plastics_extrusion_v1_cutter;Id", dataType=o6.String)
    )
    length: ns0.vartypes.AnalogUnitType
    lengthCorrection: ns0.vartypes.AnalogUnitType | None
    resetOutput: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_cutter;i=7001", browseName="ns=plastics_extrusion_v1_cutter;ResetOutput"))
    setOutput: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_extrusion_v1_cutter;i=6020", browseName="ns=plastics_extrusion_v1_cutter;SetOutput", dataType=o6.UInt64, accessLevel=3, userAccessLevel=1
        )
    )
    totalOutput: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_cutter;i=6022", browseName="ns=plastics_extrusion_v1_cutter;TotalOutput", dataType=o6.UInt64)
    )
    wallThickeningLength: ns0.vartypes.AnalogUnitType | None
    wallThickeningPosition: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_cutter;i=6019",
            browseName="ns=plastics_extrusion_v1_cutter;WallThickeningPosition",
            dataType=plastics_extrusion_v1_cutter_datypes.WallThickeningEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_cutter;i=1005", browseName="ns=plastics_extrusion_v1_cutter;Cutter_InterfaceType", displayName="Cutter_InterfaceType")
class Cutter_InterfaceType(plastics_extrusion_v1.objtypes.ExtrusionDeviceType):
    cuttingProducts: CuttingProductsType
    cuttingProgram: plastics_rubber.objtypes.StartDeviceType | None
    manualCut: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_cutter;i=7002", browseName="ns=plastics_extrusion_v1_cutter;ManualCut"))
    productSpeed: plastics_rubber.objtypes.MonitoredParameterType | None
    sampleCut: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_cutter;i=7003", browseName="ns=plastics_extrusion_v1_cutter;SampleCut"))
    sampleCuttingLength: ns0.vartypes.AnalogUnitType | None
    sideClampClosed: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_cutter;i=6039", browseName="ns=plastics_extrusion_v1_cutter;SideClampClosed", dataType=o6.Boolean)
    )
    totalWasteLength: ns0.vartypes.AnalogUnitType | None
    wasteCuttingLength: ns0.vartypes.AnalogUnitType | None
    wasteIndicator: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_extrusion_v1_cutter;i=6044", browseName="ns=plastics_extrusion_v1_cutter;WasteIndicator", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )


o6.reference(Cutter_InterfaceType, "i=41", CutEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_rubber, plastics_extrusion_v1_cutter_datypes
