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

"""Generated OPC UA plastics_imm2mes namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_imm2mes_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_imm2mes;i=1007",
    browseName="ns=plastics_imm2mes;IMM_MES_InterfaceType",
    displayName="IMM_MES_InterfaceType",
    description="Root ObjectType representing an injection moulding machine with all its subcomponents for data exchange with an MES",
)
class IMM_MES_InterfaceType(ns0.objtypes.BaseObjectType):
    injectionUnits: InjectionUnitsType
    jobs: plastics_rubber.objtypes.JobsType | None
    machineConfiguration: plastics_rubber.objtypes.MachineConfigurationType
    machineInformation: plastics_rubber.objtypes.MachineInformationType
    machineMESConfiguration: plastics_rubber.objtypes.MachineMESConfigurationType
    machineMESStatus: plastics_rubber.objtypes.MachineMESStatusType
    machineStatus: plastics_rubber.objtypes.MachineStatusType
    moulds: plastics_rubber.objtypes.MouldsType
    powerUnits: plastics_rubber.objtypes.PowerUnitsType
    productionDatasetManagement: plastics_rubber.objtypes.ProductionDatasetManagementType | None


o6.reference(IMM_MES_InterfaceType, "i=41", "ns=plastics_rubber;i=1011")
o6.reference(IMM_MES_InterfaceType, "i=41", "ns=plastics_rubber;i=1038")


@o6.objecttype(
    nodeId="ns=plastics_imm2mes;i=1016",
    browseName="ns=plastics_imm2mes;InjectionUnitsType",
    displayName="InjectionUnitsType",
    description="Container for objects of InjectionUnitType",
)
class InjectionUnitsType(ns0.objtypes.BaseObjectType):
    injectionUnit_LangleNrRangle: InjectionUnitType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6006", browseName="NodeVersion", dataType=o6.String, value="\n      ")
    )


o6.reference(InjectionUnitsType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=plastics_imm2mes;i=1039", browseName="ns=plastics_imm2mes;InjectionUnitCycleParametersType", displayName="InjectionUnitCycleParametersType", isAbstract=True
)
class InjectionUnitCycleParametersType(ns0.objtypes.BaseObjectType):
    backPressure: ns0.vartypes.AnalogItemType | None
    cavityPressureMaximum: ns0.vartypes.AnalogItemType | None
    cushionStroke: ns0.vartypes.AnalogItemType | None
    cushionVolume: ns0.vartypes.AnalogItemType
    decompressionVolumeAfterPlastification: ns0.vartypes.AnalogItemType | None
    decompressionVolumeBeforePlastification: ns0.vartypes.AnalogItemType | None
    dosingTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_imm2mes;i=6059",
            browseName="ns=plastics_imm2mes;DosingTime",
            description="Time to melt-up the plastic granulates and feed the melt for the next injection shot to the front of the screw",
            dataType=ns0.datatypes.Duration,
            value=0.0,
        )
    )
    flowIndex: ns0.vartypes.AnalogItemType | None
    holdHydraulicPressureAverage: ns0.vartypes.AnalogItemType | None
    holdHydraulicPressureMaximum: ns0.vartypes.AnalogItemType | None
    holdSpecificPressureAverage: ns0.vartypes.AnalogItemType | None
    holdSpecificPressureMaximum: ns0.vartypes.AnalogItemType | None
    hydraulicPressureMaximum: ns0.vartypes.AnalogItemType | None
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_imm2mes;i=6107", browseName="ns=plastics_imm2mes;Index", description="Index of the injection unit", dataType=o6.UInt32, value=0
        )
    )
    injectionSpeedAverage: ns0.vartypes.AnalogItemType | None
    injectionSpeedMaximum: ns0.vartypes.AnalogItemType | None
    injectionStartPosition: ns0.vartypes.AnalogItemType | None
    injectionTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_imm2mes;i=6060",
            browseName="ns=plastics_imm2mes;InjectionTime",
            description="Time required to fill the cavity or mould",
            dataType=ns0.datatypes.Duration,
            value=0.0,
        )
    )
    plastificationCircumferentialSpeedAverage: ns0.vartypes.AnalogItemType | None
    plastificationCircumferentialSpeedMaximum: ns0.vartypes.AnalogItemType | None
    plastificationHydraulicPressureAverage: ns0.vartypes.AnalogItemType | None
    plastificationHydraulicPressureMaximum: ns0.vartypes.AnalogItemType | None
    plastificationRotationalSpeedAverage: ns0.vartypes.AnalogItemType | None
    plastificationRotationalSpeedMaximum: ns0.vartypes.AnalogItemType | None
    plastificationSpecificPressureAverage: ns0.vartypes.AnalogItemType | None
    plastificationSpecificPressureMaximum: ns0.vartypes.AnalogItemType | None
    plastificationVolume: ns0.vartypes.AnalogItemType
    specificPressureMaximum: ns0.vartypes.AnalogItemType
    transferCavityPressure: ns0.vartypes.AnalogItemType | None
    transferHydraulicPressure: ns0.vartypes.AnalogItemType | None
    transferSpecificPressure: ns0.vartypes.AnalogItemType | None
    transferStroke: ns0.vartypes.AnalogItemType | None
    transferVolume: ns0.vartypes.AnalogItemType | None
    vPChangeOverPosition: ns0.vartypes.AnalogItemType | None


@o6.objecttype(
    nodeId="ns=plastics_imm2mes;i=1028",
    browseName="ns=plastics_imm2mes;InjectionUnitType",
    displayName="InjectionUnitType",
    description="Description and status of an injection unit",
)
class InjectionUnitType(ns0.objtypes.BaseObjectType):
    barrelId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_imm2mes;i=6097",
            browseName="ns=plastics_imm2mes;BarrelId",
            description="Id (e.g. serial number) of the barrel",
            dataType=o6.String,
            value="\n      ",
        )
    )
    inProduction: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_imm2mes;i=6099",
            browseName="ns=plastics_imm2mes;InProduction",
            description="information if the injection unit is used in the current running production",
            dataType=o6.Boolean,
            value=True,
        )
    )
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_imm2mes;i=6724", browseName="ns=plastics_imm2mes;Index", description="Number of the injection unit", dataType=o6.UInt32, value=0
        )
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_imm2mes;i=6098",
            browseName="ns=plastics_imm2mes;IsPresent",
            description="Information if the injection unit is physically installed on the injection machines",
            dataType=o6.Boolean,
            value=True,
        )
    )
    maxScrewStroke: ns0.vartypes.AnalogItemType | None
    screwDiameter: ns0.vartypes.AnalogItemType | None
    screwId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_imm2mes;i=6106",
            browseName="ns=plastics_imm2mes;ScrewId",
            description="Id of the screw installed in the injection unit",
            dataType=o6.String,
            value="\n      ",
        )
    )
    screwVolume: ns0.vartypes.AnalogItemType | None
    temperatureZones: plastics_rubber.objtypes.TemperatureZonesType


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_imm2mes_datypes
