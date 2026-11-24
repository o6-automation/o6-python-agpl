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

"""Generated OPC UA surface_technology_mss namespace declarations."""

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
from . import objtypes as surface_technology_mss_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

surface_technology_mss_objtypes.STSysVesselType(
    nodeId="ns=surface_technology_mss;i=5012",
    browseName="ns=surface_technology_mss;<Vessel>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_mss;i=5002", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory"))],
)
surface_technology_mss_objtypes.STCompHeaterType(
    nodeId="ns=surface_technology_mss;i=5010",
    browseName="ns=surface_technology_mss;<Heater>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_mss;i=5016", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory"))],
)
machinery.objtypes.MachineryLifetimeCounterType(nodeId="ns=surface_technology_mss;i=5024", browseName="ns=surface_technology_mss;LifetimeCounters", modellingRule="Optional")
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5014",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5024"])],
)
o6.reference(surface_technology_mss_objtypes.STSysMaterialTransportLineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5014"])
surface_technology_mss_objtypes.STCompRamType(
    nodeId="ns=surface_technology_mss;i=5011",
    browseName="ns=surface_technology_mss;<Ram>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_mss;i=5035", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory"))],
)
surface_technology_mss_objtypes.STCompHeaterType(
    nodeId="ns=surface_technology_mss;i=5041",
    browseName="ns=surface_technology_mss;<Heater>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_mss;i=5038", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory"))],
)
surface_technology_mss_objtypes.STCompStirrerType(
    nodeId="ns=surface_technology_mss;i=5009",
    browseName="ns=surface_technology_mss;<Stirrer>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_mss;i=5061", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory"))],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_mss;i=5007",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5009"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5010"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5011"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5012"]),
    ],
)
o6.reference(surface_technology_mss_objtypes.STSysRamType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_mss;i=5007"])
surface_technology_mss_objtypes.STCompStirrerType(
    nodeId="ns=surface_technology_mss;i=5040",
    browseName="ns=surface_technology_mss;<Stirrer>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology_mss;i=5062", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory"))],
)
machinery.objtypes.MachineryLifetimeCounterType(nodeId="ns=surface_technology_mss;i=5071", browseName="ns=surface_technology_mss;LifetimeCounters", modellingRule="Optional")
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5070",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            machinery.objtypes.MachineryLifetimeCounterType(
                nodeId="ns=surface_technology_mss;i=5072", browseName="ns=surface_technology_mss;LifetimeCounters", modellingRule="Optional"
            )
        )
    ],
)
surface_technology_mss_objtypes.STCompProcessValveType(
    nodeId="ns=surface_technology_mss;i=5042",
    browseName="ns=surface_technology_mss;<Valve>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5070"])],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_mss;i=5036",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5040"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5041"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5042"]),
    ],
)
o6.reference(surface_technology_mss_objtypes.STSysVesselType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_mss;i=5036"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=surface_technology_mss;i=6001",
    browseName="ns=surface_technology_mss;RemainingDurationOfUse",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6002",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6003",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6004", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=surface_technology_mss;i=5024"], "i=47", o6.ns["ns=surface_technology_mss;i=6001"])
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5005",
    browseName="ns=machinery;Health",
    description="Entry point of health information of the MachineryItem.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6001"])],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_mss;i=6005",
    browseName="ns=surface_technology_mss;FillState",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6006",
                browseName="EnumValues",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[0],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0, displayName=o6.LocalizedText("Empty"), description=o6.LocalizedText("The transport line is not filled with any material.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("MaterialFilled"), description=o6.LocalizedText("The transport line is filled with application material.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("ReactingMaterialFilled"),
                        description=o6.LocalizedText("The transport line is filled with reactive application material. It has a limited time of usage."),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3,
                        displayName=o6.LocalizedText("FlushingAgentFilled"),
                        description=o6.LocalizedText("The transport line is filled with flushing agent to clean the transport line."),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4,
                        displayName=o6.LocalizedText("Transitioning"),
                        description=o6.LocalizedText("The transport line is currently changing from one fill state to another."),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6007", browseName="ValueAsText", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6008",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6009", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6010", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5008",
    browseName="ns=surface_technology_mss;AverageFlowVelocity",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6011",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6008"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5004",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5008"]), o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6005"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_mss;i=5003",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5004"]), o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5005"])],
)
o6.reference(surface_technology_mss_objtypes.STSysMaterialTransportLineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5003"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=surface_technology_mss;i=6012",
    browseName="ns=surface_technology_mss;VesselVibration",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6013", browseName="FalseState", modellingRule="Mandatory", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6014", browseName="TrueState", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5026",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6012"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_mss;i=5025",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5026"])],
)
o6.reference(surface_technology_mss_objtypes.STCompPowderVibrationType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5025"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6017",
    browseName="ns=surface_technology_mss;FlowResistanceCoefficient",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6018", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6019",
    browseName="ns=surface_technology_mss;PressureLossCoefficient",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6020", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6021",
    browseName="ns=surface_technology_mss;CompressiveStrength",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6022", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6023",
    browseName="ns=surface_technology_mss;Length",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6024", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6025",
    browseName="ns=surface_technology_mss;CrossSection",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6026", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5001",
    browseName="ns=surface_technology;Description",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6016",
                browseName="ns=surface_technology_mss;ContactMaterial",
                modellingRule="Optional",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6017"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6019"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6021"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6023"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6025"]),
    ],
)
o6.reference(surface_technology_mss_objtypes.STSysMaterialTransportLineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5001"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=surface_technology_mss;i=6027",
    browseName="ns=surface_technology_mss;DrumPresent",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6028", browseName="FalseState", modellingRule="Mandatory", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6029", browseName="TrueState", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_mss;i=6030",
    browseName="ns=surface_technology_mss;DiscreteFillingLevel",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6031",
                browseName="EnumValues",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[0],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("empty"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("almost empty"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("full"), description=o6.LocalizedText()),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6032", browseName="ValueAsText", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=surface_technology_mss;i=6033",
    browseName="ns=surface_technology_mss;CirculationActive",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6034", browseName="FalseState", modellingRule="Mandatory", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6035", browseName="TrueState", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=surface_technology_mss;i=6036",
    browseName="ns=surface_technology_mss;RamUnitReady",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6037", browseName="FalseState", modellingRule="Mandatory", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6038", browseName="TrueState", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5018",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6027"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6030"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6033"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6036"]),
    ],
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=surface_technology_mss;i=6039",
    browseName="ns=surface_technology_mss;RemainingCycles",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6040",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6041",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6042", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=surface_technology_mss;i=6043",
    browseName="ns=surface_technology_mss;RemainingMaterialTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6044",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6045",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6046", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6047",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6048", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6049", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5019",
    browseName="ns=surface_technology_mss;MeasuredFillingLevel",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6050",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6047"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6051",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6052", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6053", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5020",
    browseName="ns=surface_technology_mss;DownwardPressureRam",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6054",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6051"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6055",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6056", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6057", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5021",
    browseName="ns=surface_technology_mss;InputCurrentRam",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6058",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6055"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6059",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6060", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6061", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5022",
    browseName="ns=surface_technology_mss;InputPressureRam",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6062",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6059"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6063",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6064", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6065", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5023",
    browseName="ns=surface_technology_mss;MaterialTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6066",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6063"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5017",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5019"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5020"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5021"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5022"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5023"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6039"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6043"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_mss;i=5015",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5017"]), o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5018"])],
)
o6.reference(surface_technology_mss_objtypes.STCompRamType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5015"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_mss;i=6071",
    browseName="ns=surface_technology_mss;TypeOfRam",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6072",
                browseName="EnumValues",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[0],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("SinglePostRam"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DualPostRam"), description=o6.LocalizedText()),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6073", browseName="ValueAsText", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_mss;i=6074",
    browseName="ns=surface_technology_mss;DrumVolumeClass",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6075",
                browseName="EnumValues",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[0],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("20 liters"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("200 liters"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("208 liters"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("210 liters"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("216.5 liters"), description=o6.LocalizedText()),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6076", browseName="ValueAsText", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6077",
    browseName="ns=surface_technology_mss;DrumInnerDiameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6078", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5013",
    browseName="ns=surface_technology;Description",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6071"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6074"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6077"]),
    ],
)
o6.reference(surface_technology_mss_objtypes.STCompRamType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5013"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6082",
    browseName="ns=surface_technology_mss;PowderSieveMeshSize",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6083", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5027",
    browseName="ns=surface_technology;Description",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6082"])],
)
o6.reference(surface_technology_mss_objtypes.STCompPowderSieveType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5027"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6084",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6085", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6086", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5032",
    browseName="ns=surface_technology_mss;OpeningDegree",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6087",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6084"]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=surface_technology_mss;i=6088", browseName="ns=di;OperationCycleCounter", modellingRule="Optional", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1
)
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=surface_technology_mss;i=5006",
    browseName="ns=surface_technology_mss;OperationCounters",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=surface_technology_mss;i=6088"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5069",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[o6.hasAddIn(o6.ns["ns=surface_technology_mss;i=5006"]), o6.hasAddIn(o6.ns["ns=surface_technology_mss;i=5071"])],
)
o6.reference(surface_technology_mss_objtypes.STCompProcessValveType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5069"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6091",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6092", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6093", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5033",
    browseName="ns=surface_technology_mss;DutyCycle",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6094",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6091"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6095",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6096", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6097", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5034",
    browseName="ns=surface_technology_mss;SwitchingFrequency",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6098",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6095"]),
    ],
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=surface_technology_mss;i=6099",
    browseName="ns=surface_technology_mss;RemainingCycles",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6100",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6101",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6102", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=surface_technology_mss;i=5071"], "i=47", o6.ns["ns=surface_technology_mss;i=6099"])
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5031",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6089",
                browseName="ns=surface_technology_mss;OpenTime",
                modellingRule="Optional",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6090",
                browseName="ns=surface_technology_mss;CloseTime",
                modellingRule="Optional",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5032"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5033"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5034"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6099"]),
    ],
)
o6.reference(o6.ns["ns=surface_technology_mss;i=5031"], "i=46", o6.ns["ns=surface_technology_mss;i=6088"])
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_mss;i=5030",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5031"])],
)
o6.reference(surface_technology_mss_objtypes.STCompProcessValveType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5030"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=surface_technology_mss;i=6103",
    browseName="ns=machinery;LifetimeVariable",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6104", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6105",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6106",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machinery.objtypes.MachineryLifetimeCounterType(
    nodeId="ns=surface_technology_mss;i=5067",
    browseName="ns=surface_technology_mss;LifetimeCounters",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6103"])],
)
o6.reference(o6.ns["ns=surface_technology_mss;i=5067"], "i=47", o6.ns["ns=surface_technology_mss;i=6039"])
o6.reference(o6.ns["ns=surface_technology_mss;i=5067"], "i=47", o6.ns["ns=surface_technology_mss;i=6043"])
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5029",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[o6.hasAddIn(o6.ns["ns=surface_technology_mss;i=5067"])],
)
o6.reference(surface_technology_mss_objtypes.STCompRamType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5029"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6107",
    browseName="ns=surface_technology_mss;FlowCrossSection",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6108", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6109",
    browseName="ns=surface_technology_mss;Travel",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6110", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6116",
    browseName="ns=surface_technology_mss;MaterialPressureMax",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6117", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6118",
    browseName="ns=surface_technology_mss;FlowVolumeMax",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6119", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_mss;i=6120",
    browseName="ns=surface_technology_mss;TypeOfActuationEnergy",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6121",
                browseName="EnumValues",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[0],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("pneumatic"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("electric"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("hydraulic"), description=o6.LocalizedText()),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6122", browseName="ValueAsText", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5028",
    browseName="ns=surface_technology;Description",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6111",
                browseName="ns=surface_technology_mss;LifetimeCycles",
                modellingRule="Optional",
                dataType=o6.UInt16,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6112",
                browseName="ns=surface_technology_mss;MinimumPulseOpenTime",
                modellingRule="Optional",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6113",
                browseName="ns=surface_technology_mss;MinimumPulseCloseTime",
                modellingRule="Optional",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6114",
                browseName="ns=surface_technology_mss;OpeningTime",
                modellingRule="Optional",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6115",
                browseName="ns=surface_technology_mss;ClosingTime",
                modellingRule="Optional",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6107"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6109"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6116"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6118"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6120"]),
    ],
)
o6.reference(surface_technology_mss_objtypes.STCompProcessValveType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5028"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6123",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6124", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6125", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5044",
    browseName="ns=surface_technology_mss;RelativePressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6126",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6123"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6127",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6128", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6129", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5045",
    browseName="ns=surface_technology_mss;Temperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6130",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6127"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6131",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6132", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6133", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5046",
    browseName="ns=surface_technology_mss;FillVolume",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6134",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6131"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5043",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5044"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5045"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5046"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_mss;i=5039",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5043"])],
)
o6.reference(surface_technology_mss_objtypes.STSysVesselType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5039"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_mss;i=6135",
    browseName="ns=surface_technology_mss;VesselVolume",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6136", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5037",
    browseName="ns=surface_technology;Description",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6135"])],
)
o6.reference(surface_technology_mss_objtypes.STSysVesselType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5037"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6137",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6138", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6139", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5049",
    browseName="ns=surface_technology_mss;StirrerSpeed",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6140",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6137"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6141",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6142", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6143", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5050",
    browseName="ns=surface_technology_mss;StirrerTorque",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6144",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6141"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5048",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5049"]), o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5050"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_mss;i=5047",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5048"])],
)
o6.reference(surface_technology_mss_objtypes.STCompStirrerType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5047"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_mss;i=6145",
    browseName="ns=surface_technology_mss;TypeOfHeating",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6146",
                browseName="EnumValues",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[0],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("indirect fluid"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("electrical"), description=o6.LocalizedText()),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6147", browseName="ValueAsText", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5054",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6145"])],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6148",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6149", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6150", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5055",
    browseName="ns=surface_technology_mss;Temperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6151",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6148"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6152",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6153", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6154", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5056",
    browseName="ns=surface_technology_mss;StandbyTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6155",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6152"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6156",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6157", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6158", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5057",
    browseName="ns=surface_technology_mss;HeatingPower",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6159",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6156"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6161",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6162", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6163", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5058",
    browseName="ns=surface_technology_mss;HeatUpTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6164",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6161"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6165",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6166", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6167", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5059",
    browseName="ns=surface_technology_mss;HeatThroughTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6168",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6165"]),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=surface_technology_mss;i=6169",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6170", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6171", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=surface_technology_mss;i=5060",
    browseName="ns=surface_technology_mss;StandbyTimeout",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6172",
                browseName="ns=padim;SignalTag",
                displayName="Tag",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6169"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5053",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6160",
                browseName="ns=surface_technology_mss;HeatingPowerRelative",
                modellingRule="Optional",
                dataType=ns0.datatypes.Number,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5055"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5056"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5057"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5058"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5059"]),
        o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5060"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_mss;i=5052",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5053"]), o6.hasComponent(o6.ns["ns=surface_technology_mss;i=5054"])],
)
o6.reference(surface_technology_mss_objtypes.STCompHeaterType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5052"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_mss;i=6173",
    browseName="ns=surface_technology_mss;TypeOfDevice",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6174",
                browseName="EnumValues",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[0],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("drum floor heater"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("heating band"), description=o6.LocalizedText()),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("heated follow plate"), description=o6.LocalizedText()),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6175", browseName="ValueAsText", modellingRule="Mandatory", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_mss;i=5051",
    browseName="ns=surface_technology;Description",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_mss;i=6173"])],
)
o6.reference(surface_technology_mss_objtypes.STCompHeaterType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_mss;i=5051"])
http_opcfoundation_org_UA_SurfaceTechnology_OCT_MSS_ = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=surface_technology_mss;i=5068",
    browseName="ns=surface_technology_mss;http://opcfoundation.org/UA/SurfaceTechnology/OCT-MSS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6176", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6177", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-08-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6178", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/SurfaceTechnology/OCT-MSS/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6179", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6180",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[0],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_mss;i=6181", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_mss;i=6182", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


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
    surface_technology_mss_objtypes,
)
