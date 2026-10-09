# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA surface_technology_cleaning namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
import o6.ns.surface_technology as surface_technology
from . import objtypes as surface_technology_cleaning_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

surface_technology_cleaning_objtypes.STCompCondenserType(
    nodeId="ns=surface_technology_cleaning;i=5069",
    browseName="ns=surface_technology_cleaning;<Condenser>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5070", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompCoolerType(
    nodeId="ns=surface_technology_cleaning;i=5071",
    browseName="ns=surface_technology_cleaning;<Cooler>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5072", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompHeaterType(
    nodeId="ns=surface_technology_cleaning;i=5073",
    browseName="ns=surface_technology_cleaning;<Heater>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5074", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPressurizedAirType(
    nodeId="ns=surface_technology_cleaning;i=5075",
    browseName="ns=surface_technology_cleaning;<PressurizedAir>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5076", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPumpType(
    nodeId="ns=surface_technology_cleaning;i=5077",
    browseName="ns=surface_technology_cleaning;<Pump>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5078", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompValveType(
    nodeId="ns=surface_technology_cleaning;i=5079",
    browseName="ns=surface_technology_cleaning;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5080", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompVesselType(
    nodeId="ns=surface_technology_cleaning;i=5081",
    browseName="ns=surface_technology_cleaning;<Vessel>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5082", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_cleaning;i=5065",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5069"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5071"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5073"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5075"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5077"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5079"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5081"]),
    ],
)
o6.reference(surface_technology_cleaning_objtypes.STSysAuxiliaryType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_cleaning;i=5065"])
surface_technology_cleaning_objtypes.STCompCoolerType(
    nodeId="ns=surface_technology_cleaning;i=5084",
    browseName="ns=surface_technology_cleaning;<Cooler>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5085", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompHeaterType(
    nodeId="ns=surface_technology_cleaning;i=5086",
    browseName="ns=surface_technology_cleaning;<Heater>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5087", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPumpType(
    nodeId="ns=surface_technology_cleaning;i=5088",
    browseName="ns=surface_technology_cleaning;<Pump>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5089", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompUltrasonicEmitterType(
    nodeId="ns=surface_technology_cleaning;i=5090",
    browseName="ns=surface_technology_cleaning;<UltrasonicEmitter>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5091", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompValveType(
    nodeId="ns=surface_technology_cleaning;i=5092",
    browseName="ns=surface_technology_cleaning;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5093", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompVesselType(
    nodeId="ns=surface_technology_cleaning;i=5094",
    browseName="ns=surface_technology_cleaning;<Vessel>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5095", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_cleaning;i=5083",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5084"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5086"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5088"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5090"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5092"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5094"]),
    ],
)
o6.reference(surface_technology_cleaning_objtypes.STSysCleaningType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_cleaning;i=5083"])
surface_technology_cleaning_objtypes.STCompCoolerType(
    nodeId="ns=surface_technology_cleaning;i=5100",
    browseName="ns=surface_technology_cleaning;<Cooler>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5101", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompDryerType(
    nodeId="ns=surface_technology_cleaning;i=5102",
    browseName="ns=surface_technology_cleaning;<Dryer>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5103", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPressurizedAirType(
    nodeId="ns=surface_technology_cleaning;i=5104",
    browseName="ns=surface_technology_cleaning;<PressurizedAir>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5105", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompValveType(
    nodeId="ns=surface_technology_cleaning;i=5106",
    browseName="ns=surface_technology_cleaning;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5107", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_cleaning;i=5096",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5100"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5102"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5104"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5106"]),
    ],
)
o6.reference(surface_technology_cleaning_objtypes.STSysConveyorType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_cleaning;i=5096"])
surface_technology_cleaning_objtypes.STCompCoolerType(
    nodeId="ns=surface_technology_cleaning;i=5113",
    browseName="ns=surface_technology_cleaning;<Cooler>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5114", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompDryerType(
    nodeId="ns=surface_technology_cleaning;i=5115",
    browseName="ns=surface_technology_cleaning;<Dryer>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5116", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompHeaterType(
    nodeId="ns=surface_technology_cleaning;i=5117",
    browseName="ns=surface_technology_cleaning;<Heater>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5118", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPressurizedAirType(
    nodeId="ns=surface_technology_cleaning;i=5119",
    browseName="ns=surface_technology_cleaning;<PressurizedAir>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5120", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPumpType(
    nodeId="ns=surface_technology_cleaning;i=5121",
    browseName="ns=surface_technology_cleaning;<Pump>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5122", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompValveType(
    nodeId="ns=surface_technology_cleaning;i=5123",
    browseName="ns=surface_technology_cleaning;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5124", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompVesselType(
    nodeId="ns=surface_technology_cleaning;i=5125",
    browseName="ns=surface_technology_cleaning;<Vessel>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5126", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_cleaning;i=5108",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5113"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5115"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5117"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5119"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5121"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5123"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5125"]),
    ],
)
o6.reference(surface_technology_cleaning_objtypes.STSysDryingType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_cleaning;i=5108"])
surface_technology_cleaning_objtypes.STCompDryerType(
    nodeId="ns=surface_technology_cleaning;i=5131",
    browseName="ns=surface_technology_cleaning;<Dryer>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5132", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPressurizedAirType(
    nodeId="ns=surface_technology_cleaning;i=5133",
    browseName="ns=surface_technology_cleaning;<PressurizedAir>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5134", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompValveType(
    nodeId="ns=surface_technology_cleaning;i=5135",
    browseName="ns=surface_technology_cleaning;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5136", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_cleaning;i=5127",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5131"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5133"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5135"]),
    ],
)
o6.reference(surface_technology_cleaning_objtypes.STSysHandlingType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_cleaning;i=5127"])
surface_technology_cleaning_objtypes.STCompPumpType(
    nodeId="ns=surface_technology_cleaning;i=5138",
    browseName="ns=surface_technology_cleaning;<Pump>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5139", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompStirrerType(
    nodeId="ns=surface_technology_cleaning;i=5140",
    browseName="ns=surface_technology_cleaning;<Stirrer>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5141", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompValveType(
    nodeId="ns=surface_technology_cleaning;i=5142",
    browseName="ns=surface_technology_cleaning;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5143", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompVesselType(
    nodeId="ns=surface_technology_cleaning;i=5144",
    browseName="ns=surface_technology_cleaning;<Vessel>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5145", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_cleaning;i=5137",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5138"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5140"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5142"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5144"]),
    ],
)
o6.reference(surface_technology_cleaning_objtypes.STSysMaterialSupplyType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_cleaning;i=5137"])
surface_technology_cleaning_objtypes.STCompCoolerType(
    nodeId="ns=surface_technology_cleaning;i=5158",
    browseName="ns=surface_technology_cleaning;<Cooler>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5159", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompHeaterType(
    nodeId="ns=surface_technology_cleaning;i=5160",
    browseName="ns=surface_technology_cleaning;<Heater>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5161", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPumpType(
    nodeId="ns=surface_technology_cleaning;i=5162",
    browseName="ns=surface_technology_cleaning;<Pump>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5163", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompUltrasonicEmitterType(
    nodeId="ns=surface_technology_cleaning;i=5164",
    browseName="ns=surface_technology_cleaning;<UltrasonicEmitter>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5165", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompValveType(
    nodeId="ns=surface_technology_cleaning;i=5166",
    browseName="ns=surface_technology_cleaning;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5167", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompVesselType(
    nodeId="ns=surface_technology_cleaning;i=5168",
    browseName="ns=surface_technology_cleaning;<Vessel>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5169", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_cleaning;i=5157",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5158"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5160"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5162"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5164"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5166"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5168"]),
    ],
)
o6.reference(surface_technology_cleaning_objtypes.STSysRinsingType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_cleaning;i=5157"])
surface_technology_cleaning_objtypes.STCompHeaterType(
    nodeId="ns=surface_technology_cleaning;i=5171",
    browseName="ns=surface_technology_cleaning;<Heater>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5172", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompPumpType(
    nodeId="ns=surface_technology_cleaning;i=5173",
    browseName="ns=surface_technology_cleaning;<Pump>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5174", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompValveType(
    nodeId="ns=surface_technology_cleaning;i=5175",
    browseName="ns=surface_technology_cleaning;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5176", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
surface_technology_cleaning_objtypes.STCompVesselType(
    nodeId="ns=surface_technology_cleaning;i=5177",
    browseName="ns=surface_technology_cleaning;<Vessel>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_cleaning;i=5178", browseName="ns=surface_technology;MachineryBuildingBlocks"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_cleaning;i=5170",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5171"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5173"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5175"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5177"]),
    ],
)
o6.reference(surface_technology_cleaning_objtypes.STSysTreatmentType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_cleaning;i=5170"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashSurfaceTechnologySlashCleaningPretreatmentSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=surface_technology_cleaning;i=5001",
    browseName="ns=surface_technology_cleaning;http://opcfoundation.org/UA/SurfaceTechnology/CleaningPretreatment/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-10-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6003",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/SurfaceTechnology/CleaningPretreatment/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6005",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6008",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6009", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6010", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5004",
    browseName="ns=surface_technology_cleaning;<CoolingPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6011", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6008"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6012",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6013", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6014", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5005",
    browseName="ns=surface_technology_cleaning;<Temperature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6015", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6012"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5003",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5004"]), o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5005"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5002",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5003"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompCoolerType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5002"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6016",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6017", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6018", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5008",
    browseName="ns=surface_technology_cleaning;<Temperature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6019", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6016"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5007",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5008"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5006",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5007"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompCondenserType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5006"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6020",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6022", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5011",
    browseName="ns=surface_technology_cleaning;<DryerPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6023", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6020"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6024",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6025", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6026", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5012",
    browseName="ns=surface_technology_cleaning;<Humidity>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6027", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6024"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6028",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6029", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6030", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5013",
    browseName="ns=surface_technology_cleaning;<Temperature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6031", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6028"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5010",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5011"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5012"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5013"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5009",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5010"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompDryerType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5009"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6032",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6033", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6034", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5016",
    browseName="ns=surface_technology_cleaning;<EmissionControl>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6035", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6032"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6036",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6037", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6038", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5017",
    browseName="ns=surface_technology_cleaning;<HeatingPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6039", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6036"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6040",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6041", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6042", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5018",
    browseName="ns=surface_technology_cleaning;<Temperature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6043", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6040"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5015",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5016"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5017"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5018"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5014",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5015"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompHeaterType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5014"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6044",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6045", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6046", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5021",
    browseName="ns=surface_technology_cleaning;<PressurizedAirPressure>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6047", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6044"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6048",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6049", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6050", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5022",
    browseName="ns=surface_technology_cleaning;<PressurizedAirVolumeflow>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6051", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6048"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6052",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6053", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6054", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5023",
    browseName="ns=surface_technology_cleaning;<Temperature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6055", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6052"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5020",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5021"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5022"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5023"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5019",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5020"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompPressurizedAirType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5019"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6056",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6057", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6058", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5026",
    browseName="ns=surface_technology_cleaning;<EmissionControl>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6059", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6056"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6060",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6061", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6062", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5027",
    browseName="ns=surface_technology_cleaning;<InverterFrequency>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6063", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6060"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6064",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6065", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5028",
    browseName="ns=surface_technology_cleaning;<InverterPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6067", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6064"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6068",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5029",
    browseName="ns=surface_technology_cleaning;<MediaPressure>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6071", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6068"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6072",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6073", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6074", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5030",
    browseName="ns=surface_technology_cleaning;<MediaVolumeflow>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6075", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6072"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6076",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6077", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6078", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5031",
    browseName="ns=surface_technology_cleaning;<PumpVibration>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6079", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6076"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6080",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6082", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5032",
    browseName="ns=surface_technology_cleaning;<Temperature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6083", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6080"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5025",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5026"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5027"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5028"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5029"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5030"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5031"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5032"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5024",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5025"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompPumpType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5024"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6084",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6085", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6086", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5035",
    browseName="ns=surface_technology_cleaning;<StirrerSpeed>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6087", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6084"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5034",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5035"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5033",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5034"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompStirrerType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5033"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6088",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6089", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6090", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5038",
    browseName="ns=surface_technology_cleaning;<UltrasonicFrequency>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6091", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6088"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6092",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6093", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6094", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5039",
    browseName="ns=surface_technology_cleaning;<UltrasonicPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6095", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6092"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5037",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5038"]), o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5039"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5036",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5037"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompUltrasonicEmitterType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5036"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6096",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6097", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6098", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5042",
    browseName="ns=surface_technology_cleaning;<ValveOpeningAngle>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6099", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6096"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6100",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6102", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5043",
    browseName="ns=surface_technology_cleaning;<ValveOpeningTime>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6103", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6100"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5041",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5042"]), o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5043"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5040",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5041"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompValveType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5040"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6104",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6105", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6106", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5046",
    browseName="ns=surface_technology_cleaning;<CoolingPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6107", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6104"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6108",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6109", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6110", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5047",
    browseName="ns=surface_technology_cleaning;<CorrosionProtectionConcentration>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6111", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6108"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6112",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6114", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5048",
    browseName="ns=surface_technology_cleaning;<DryerPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6115", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6112"]),
    ],
)
padim.vartypes.MultiStateDiscreteSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6116",
    browseName="ns=padim;MultiStateDiscreteSignal",
    displayName="Multistate I/O value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6117", browseName="EnumDictionaryEntries", dataType=o6.NodeId, valueRank=2, arrayDimensions=[0, 0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6118",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Empty", "en"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Low", "en"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Medium", "en"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("High", "en"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Full", "en"), description=o6.LocalizedText()),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6119", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Empty"))
        ),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
padim.objtypes.MultiStateDiscreteSignalType(
    nodeId="ns=surface_technology_cleaning;i=5049",
    browseName="ns=surface_technology_cleaning;<FillLevelDiscrete>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6120", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6116"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6121",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6122", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6123", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5186",
    browseName="ns=surface_technology_cleaning;<ChamberPressure>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6124", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6121"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6126",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6127", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6128", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5050",
    browseName="ns=surface_technology_cleaning;<FluorescenceLiquid>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6129", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6126"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6130",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6131", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6132", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5051",
    browseName="ns=surface_technology_cleaning;<HeatingPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6133", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6130"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6134",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6135", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6136", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5052",
    browseName="ns=surface_technology_cleaning;<LevelCavitationNoise>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6137", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6134"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6138",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6139", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6140", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5053",
    browseName="ns=surface_technology_cleaning;<NonVolatileResidualsLiquid>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6141", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6138"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6142",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6143", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6144", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5054",
    browseName="ns=surface_technology_cleaning;<OilContaminantConcentration>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6145", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6142"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6146",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6147", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6148", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5055",
    browseName="ns=surface_technology_cleaning;<ParticleCountClassXLiquid>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6149", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6146"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6150",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6151", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6152", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5056",
    browseName="ns=surface_technology_cleaning;<ParticleWeightLiquid>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6153", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6150"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6154",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6156", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5057",
    browseName="ns=surface_technology_cleaning;<phValue>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6157", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6154"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6158",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6159", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6160", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5058",
    browseName="ns=surface_technology_cleaning;<QualityIndexLiquid>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6161", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6158"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6162",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6163", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6164", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5059",
    browseName="ns=surface_technology_cleaning;<SurfactantConcentration>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6165", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6162"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6166",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6167", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6168", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5060",
    browseName="ns=surface_technology_cleaning;<Temperature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6169", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6166"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6170",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6171", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6172", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5061",
    browseName="ns=surface_technology_cleaning;<TotalOrganicCarbon>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6173", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6170"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6174",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6175", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6176", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5062",
    browseName="ns=surface_technology_cleaning;<UltrasonicFrequency>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6177", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6174"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6178",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6179", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6180", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5063",
    browseName="ns=surface_technology_cleaning;<UltrasonicPower>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6181", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6178"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6182",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6184", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5064",
    browseName="ns=surface_technology_cleaning;<VolatileResidualsLiquid>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6185", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6182"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6186",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6187", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6188", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5068",
    browseName="ns=surface_technology_cleaning;<ParticleCountClassXLiquid>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6189", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6186"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5067",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5068"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5066",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5067"])],
)
o6.reference(surface_technology_cleaning_objtypes.STSysAuxiliaryType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5066"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6190",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6191", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6192", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5099",
    browseName="ns=surface_technology_cleaning;<MovementSpeed>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6193", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6190"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5098",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5099"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5097",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5098"])],
)
o6.reference(surface_technology_cleaning_objtypes.STSysConveyorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5097"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6194",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6195", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6196", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5111",
    browseName="ns=surface_technology_cleaning;<EmissionControl>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6197", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6194"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6198",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6199", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6200", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5112",
    browseName="ns=surface_technology_cleaning;<Humidity>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6201", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6198"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5110",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5111"]), o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5112"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5109",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5110"])],
)
o6.reference(surface_technology_cleaning_objtypes.STSysDryingType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5109"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6202",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6203", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6204", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5130",
    browseName="ns=surface_technology_cleaning;<MovementSpeed>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6205", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6202"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5129",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5130"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5128",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5129"])],
)
o6.reference(surface_technology_cleaning_objtypes.STSysHandlingType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5128"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6206",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6207", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6208", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5148",
    browseName="ns=surface_technology_cleaning;<FluorescencePart>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6209", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6206"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6210",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6212", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5149",
    browseName="ns=surface_technology_cleaning;<NonVolatileResidualsPart>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6213", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6210"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6214",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6215", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6216", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5150",
    browseName="ns=surface_technology_cleaning;<ParticleCountClassXLiquid>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6217", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6214"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6218",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6219", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6220", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5151",
    browseName="ns=surface_technology_cleaning;<ParticleCountClassXPart>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6221", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6218"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6222",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6223", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6224", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5152",
    browseName="ns=surface_technology_cleaning;<ParticleWeightPart>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6225", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6222"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6226",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6227", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6228", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5153",
    browseName="ns=surface_technology_cleaning;<QualityIndexPart>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6229", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6226"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6230",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6231", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6232", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5154",
    browseName="ns=surface_technology_cleaning;<ResidualGasAnalysisHeavyHydrocarbons>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6233", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6230"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6234",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6235", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6236", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5155",
    browseName="ns=surface_technology_cleaning;<ResidualGasAnalysisLightHydrocarbons>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6237", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6234"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6238",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6239", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6240", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5156",
    browseName="ns=surface_technology_cleaning;<ResidualGasAnalysisWater>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6241", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6238"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5147",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5148"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5149"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5150"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5151"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5152"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5153"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5154"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5155"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5156"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5146",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5147"])],
)
o6.reference(surface_technology_cleaning_objtypes.STSysQualityControlType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5146"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6242",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6243", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6244", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5179",
    browseName="ns=surface_technology_cleaning;<AlkalinityFree>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6245", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6242"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6246",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6247", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6248", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5180",
    browseName="ns=surface_technology_cleaning;<AlkalinityTotal>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6249", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6246"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6250",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6251", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6252", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5181",
    browseName="ns=surface_technology_cleaning;<AcidityFree>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6253", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6250"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6254",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6255", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6256", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5182",
    browseName="ns=surface_technology_cleaning;<AcidityTotal>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6257", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6254"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6258",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6259", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6260", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5183",
    browseName="ns=surface_technology_cleaning;<Conductivity>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6261", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6258"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6262",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6263", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5184",
    browseName="ns=surface_technology_cleaning;<CleaningAgentConcentration>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6265", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6262"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6266",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6267", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6268", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5185",
    browseName="ns=surface_technology_cleaning;<BuilderConcentration>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6269", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6266"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6125",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6270", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6271", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=5187",
    browseName="ns=surface_technology_cleaning;<CavitationIntensity>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6272", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6125"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_cleaning;i=6274",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6275", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_cleaning;i=6276", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_cleaning;i=6273",
    browseName="ns=surface_technology_cleaning;<FillLevel>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_cleaning;i=6277", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6274"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_cleaning;i=5045",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5046"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5047"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5048"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5049"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5050"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5051"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5052"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5053"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5054"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5055"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5056"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5057"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5058"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5059"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5060"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5061"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5062"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5063"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5064"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5179"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5180"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5181"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5182"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5183"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5184"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5185"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5186"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5187"]),
        o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=6273"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_cleaning;i=5044",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_cleaning;i=5045"])],
)
o6.reference(surface_technology_cleaning_objtypes.STCompVesselType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_cleaning;i=5044"])


del (
    Any,
    TYPE_CHECKING,
    uuid,
    o6,
    di,
    ia,
    irdi,
    isa95_jobcontrol_v2,
    machinery,
    machinery_jobs,
    machinery_processvalues,
    ns0,
    padim,
    surface_technology,
    surface_technology_cleaning_objtypes,
)
