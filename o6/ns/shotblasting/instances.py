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

"""Generated OPC UA shotblasting namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0
from . import objtypes as shotblasting_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5014", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5032", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5035", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5040", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5044", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5047", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=shotblasting;i=6001",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6002", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=shotblasting;i=5001", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6001"])]
)
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5026", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory", references=[o6.hasAddIn(o6.ns["ns=shotblasting;i=5001"])]
)
o6.reference(shotblasting_objtypes.FiltrationType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5026"])
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=shotblasting;i=5006",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6004",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6005",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6006",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(shotblasting_objtypes.ShotBlastChamberType, ns0.reftypes.HasAddIn, o6.ns["ns=shotblasting;i=5006"])
o6.reference(o6.ns["ns=shotblasting;i=5008"], "i=17604", o6.ns["ns=shotblasting;i=5006"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=shotblasting;i=6011",
    browseName="ns=shotblasting;ShotBlastMediaHardnessUnit",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6012",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("HRC")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("HV")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("MOHS")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("HB")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6013", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=shotblasting;i=6010",
    browseName="ns=shotblasting;ShotBlastMediaHardnessAverage",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6011"])],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(shotblasting_objtypes.ShotBlastMediaType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=6010"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5009",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6015",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6016",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(shotblasting_objtypes.BlasterType, ns0.reftypes.HasAddIn, o6.ns["ns=shotblasting;i=5009"])
o6.reference(o6.ns["ns=shotblasting;i=5011"], "i=17604", o6.ns["ns=shotblasting;i=5009"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6017",
    browseName="ns=shotblasting;ShotBlastMediaThroughput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6018", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6019",
    browseName="ns=shotblasting;ShotBlastMediaThroughputPercent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6020", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6021",
    browseName="ns=shotblasting;ShotBlastPressure",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6022", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6023",
    browseName="ns=shotblasting;WheelRotationSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6024", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Int32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5010",
    browseName="ns=shotblasting;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6025", browseName="ns=shotblasting;ShotBlastTime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6017"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6019"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6021"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6023"]),
    ],
)
o6.reference(shotblasting_objtypes.BlasterType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5010"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5013",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6026",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6027",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=shotblasting;i=5014"], "i=17604", o6.ns["ns=shotblasting;i=5013"])
shotblasting_objtypes.BlasterType(
    nodeId="ns=shotblasting;i=5012",
    browseName="ns=shotblasting;<Blaster>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=shotblasting;i=5014"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5015", browseName="ns=shotblasting;Monitoring")),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5013"]),
    ],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=shotblasting;i=5007", browseName="ns=machinery;Components", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=shotblasting;i=5012"])]
)
o6.reference(shotblasting_objtypes.ShotBlastChamberType, ns0.reftypes.HasAddIn, o6.ns["ns=shotblasting;i=5007"])
o6.reference(o6.ns["ns=shotblasting;i=5008"], "i=17604", o6.ns["ns=shotblasting;i=5007"])
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5016",
    browseName="ns=shotblasting;Monitoring",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6028", browseName="ns=shotblasting;HopperLevelMax", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6029", browseName="ns=shotblasting;HopperLevelMin", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(shotblasting_objtypes.HopperType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5016"])
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5017",
    browseName="ns=shotblasting;Monitoring",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6030", browseName="ns=shotblasting;RefillSiloLevelMax", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6031", browseName="ns=shotblasting;RefillSiloLevelMin", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(shotblasting_objtypes.RefillSiloType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5017"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5018",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6032",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6033",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(shotblasting_objtypes.PressurisedBoilerType, ns0.reftypes.HasAddIn, o6.ns["ns=shotblasting;i=5018"])
o6.reference(o6.ns["ns=shotblasting;i=5020"], "i=17604", o6.ns["ns=shotblasting;i=5018"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6036",
    browseName="ns=shotblasting;StoragePressure",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6037", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5019",
    browseName="ns=shotblasting;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6034", browseName="ns=shotblasting;PressurisedBoilerLevelMax", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6035", browseName="ns=shotblasting;PressurisedBoilerLevelMin", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6036"]),
    ],
)
o6.reference(shotblasting_objtypes.PressurisedBoilerType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5019"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5021",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6038",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6039",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(shotblasting_objtypes.ConveyorType, ns0.reftypes.HasAddIn, o6.ns["ns=shotblasting;i=5021"])
o6.reference(o6.ns["ns=shotblasting;i=5023"], "i=17604", o6.ns["ns=shotblasting;i=5021"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6040",
    browseName="ns=shotblasting;ConveyorTransportSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6041", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6042",
    browseName="ns=shotblasting;WorkpieceRotationSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6043", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5022",
    browseName="ns=shotblasting;Monitoring",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6040"]), o6.hasComponent(o6.ns["ns=shotblasting;i=6042"])],
)
o6.reference(shotblasting_objtypes.ConveyorType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5022"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=shotblasting;i=6044",
    browseName="ns=shotblasting;ConsumedMedia",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6045",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Shotblast Media")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Water")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Pressurised Air")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6046", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(shotblasting_objtypes.DeploymentType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=6044"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6047",
    browseName="ns=shotblasting;ActualConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6048", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(shotblasting_objtypes.DeploymentType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=6047"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5024",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6051",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6052",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(shotblasting_objtypes.FiltrationType, ns0.reftypes.HasAddIn, o6.ns["ns=shotblasting;i=5024"])
o6.reference(o6.ns["ns=shotblasting;i=5026"], "i=17604", o6.ns["ns=shotblasting;i=5024"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6060",
    browseName="ns=shotblasting;DifferentialPressure",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6061", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6062",
    browseName="ns=shotblasting;TemperatureFilterUnit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6064",
    browseName="ns=shotblasting;FillLevel<n>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6065", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6066",
    browseName="ns=shotblasting;FlowRate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6067", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6068",
    browseName="ns=shotblasting;ResidualDust",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5025",
    browseName="ns=shotblasting;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6053", browseName="ns=shotblasting;FilterRunning", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6054", browseName="ns=shotblasting;FlowRateOK", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6055", browseName="ns=shotblasting;FilterCleaningRunning", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6056", browseName="ns=shotblasting;DifferentialPressureMax", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6057", browseName="ns=shotblasting;DifferentialPressureMin", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6058", browseName="ns=shotblasting;DischargeSystemRunning", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6059", browseName="ns=shotblasting;ResidualDustOK", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6060"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6062"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6064"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6066"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6068"]),
    ],
)
o6.reference(shotblasting_objtypes.FiltrationType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5025"])
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=shotblasting;i=5027",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6003",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6070",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6071",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(shotblasting_objtypes.ShotBlastMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=shotblasting;i=5027"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5031",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6072",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6073",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=shotblasting;i=5032"], "i=17604", o6.ns["ns=shotblasting;i=5031"])
shotblasting_objtypes.BlasterType(
    nodeId="ns=shotblasting;i=5030",
    browseName="ns=shotblasting;<Blaster>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=shotblasting;i=5032"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5033", browseName="ns=shotblasting;Monitoring")),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5031"]),
    ],
)
machinery.objtypes.MachineComponentsType(nodeId="ns=shotblasting;i=5029", browseName="ns=machinery;Components", references=[o6.hasComponent(o6.ns["ns=shotblasting;i=5030"])])
o6.reference(o6.ns["ns=shotblasting;i=5035"], "i=17604", o6.ns["ns=shotblasting;i=5029"])
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=shotblasting;i=5034",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6074",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6075",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6076",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=shotblasting;i=5035"], "i=17604", o6.ns["ns=shotblasting;i=5034"])
shotblasting_objtypes.ShotBlastChamberType(
    nodeId="ns=shotblasting;i=5028",
    browseName="ns=shotblasting;<ShotBlastChamber>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6077", browseName="ns=shotblasting;LoadingState", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=shotblasting;i=5035"]),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5029"]),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5034"]),
    ],
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5039",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6078",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6079",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=shotblasting;i=5040"], "i=17604", o6.ns["ns=shotblasting;i=5039"])
shotblasting_objtypes.PressurisedBoilerType(
    nodeId="ns=shotblasting;i=5038",
    browseName="ns=shotblasting;<PressurisedBoiler>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=shotblasting;i=5040"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5041", browseName="ns=shotblasting;Monitoring")),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5039"]),
    ],
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5043",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6080",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6081",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=shotblasting;i=5044"], "i=17604", o6.ns["ns=shotblasting;i=5043"])
shotblasting_objtypes.ConveyorType(
    nodeId="ns=shotblasting;i=5042",
    browseName="ns=shotblasting;<Conveyor>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=5044"]), o6.hasAddIn(o6.ns["ns=shotblasting;i=5043"])],
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=shotblasting;i=5046",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6082",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6083",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=shotblasting;i=5047"], "i=17604", o6.ns["ns=shotblasting;i=5046"])
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5048",
    browseName="ns=shotblasting;Monitoring",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6084", browseName="ns=shotblasting;FilterRunning", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        )
    ],
)
shotblasting_objtypes.FiltrationType(
    nodeId="ns=shotblasting;i=5045",
    browseName="ns=shotblasting;<FiltrationSystem>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=5047"]), o6.hasComponent(o6.ns["ns=shotblasting;i=5048"]), o6.hasAddIn(o6.ns["ns=shotblasting;i=5046"])],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=shotblasting;i=5002",
    browseName="ns=machinery;Components",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=shotblasting;i=5028"]),
        o6.hasComponent(shotblasting_objtypes.HopperType(nodeId="ns=shotblasting;i=5036", browseName="ns=shotblasting;<Hopper>", modellingRule="MandatoryPlaceholder")),
        o6.hasComponent(shotblasting_objtypes.RefillSiloType(nodeId="ns=shotblasting;i=5037", browseName="ns=shotblasting;<RefillSilo>", modellingRule="OptionalPlaceholder")),
        o6.hasComponent(o6.ns["ns=shotblasting;i=5038"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=5042"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=5045"]),
    ],
)
o6.reference(shotblasting_objtypes.ShotBlastMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=shotblasting;i=5002"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=shotblasting;i=6085",
    browseName="ns=shotblasting;ConsumedMedia",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6086",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Shotblast Media")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Water")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Pressurised Air")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6087", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
shotblasting_objtypes.DeploymentType(
    nodeId="ns=shotblasting;i=5049", browseName="ns=shotblasting;<Water>", modellingRule="OptionalPlaceholder", references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6085"])]
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=shotblasting;i=6088",
    browseName="ns=shotblasting;ConsumedMedia",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6089",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Shotblast Media")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Water")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Pressurised Air")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6090", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
shotblasting_objtypes.DeploymentType(
    nodeId="ns=shotblasting;i=5050", browseName="ns=shotblasting;<Electricity>", modellingRule="OptionalPlaceholder", references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6088"])]
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=shotblasting;i=6091",
    browseName="ns=shotblasting;ConsumedMedia",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6092",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Shotblast Media")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Water")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Pressurised Air")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6093", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
shotblasting_objtypes.DeploymentType(
    nodeId="ns=shotblasting;i=5051",
    browseName="ns=shotblasting;<PressurisedAir>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6091"])],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=shotblasting;i=6049",
    browseName="ns=shotblasting;TotalConsumption",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6050", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6094", browseName="ns=shotblasting;ConsumingPeriod", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(shotblasting_objtypes.DeploymentType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=6049"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=shotblasting;i=6097",
    browseName="ns=machinery;LifetimeVariable",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6098", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6099",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6100",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machinery.objtypes.MachineryLifetimeCounterType(
    nodeId="ns=shotblasting;i=5054", browseName="ns=machinery;LifetimeCounter", references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6097"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=shotblasting;i=6101",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6102", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=shotblasting;i=5055", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6101"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=shotblasting;i=6103",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6104", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=shotblasting;i=5056", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6103"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=shotblasting;i=6105",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6106", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=shotblasting;i=5058",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6111", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=shotblasting;i=6105"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=shotblasting;i=6107",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=shotblasting;i=6108",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=shotblasting;i=6109",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=shotblasting;i=6110",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=shotblasting;i=6112",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=shotblasting;i=6113",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=shotblasting;i=6114",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashSurfaceTechnologySlashShotBlastingSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=shotblasting;i=5060",
    browseName="ns=shotblasting;http://opcfoundation.org/UA/SurfaceTechnology/ShotBlasting/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6119", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6120", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-04-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6121", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/SurfaceTechnology/ShotBlasting/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6122", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6123",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6124", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6125", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=shotblasting;i=6130",
    browseName="ns=shotblasting;ConsumedMedia",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6131",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Shotblast Media")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Water")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Pressurised Air")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6132", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
shotblasting_objtypes.DeploymentType(
    nodeId="ns=shotblasting;i=5063",
    browseName="ns=shotblasting;<ShotBlastMediaSupply>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6130"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5004",
    browseName="ns=shotblasting;Monitoring",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=shotblasting;i=5049"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=5050"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=5051"]),
        o6.hasComponent(o6.ns["ns=shotblasting;i=5063"]),
    ],
)
o6.reference(shotblasting_objtypes.ShotBlastMachineType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5004"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=shotblasting;i=6135",
    browseName="ns=shotblasting;ShotBlastMediaHardnessUnit",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=shotblasting;i=6136",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("HRC")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("HV")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("MOHS")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("HB")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6137", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=shotblasting;i=6133",
    browseName="ns=shotblasting;ShotBlastMediaHardnessRange",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=6135"])],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(shotblasting_objtypes.ShotBlastMediaType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=6133"])


ns0.vartypes.PropertyType(
    nodeId="ns=shotblasting;i=6115",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=shotblasting;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Contains an ID of the job order, as specified by the method caller.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=shotblasting;i=6116",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=shotblasting;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=bacnet;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=shotblasting;i=7001",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=shotblasting;i=6115"]),
    outputArgs=o6.hasProperty(o6.ns["ns=shotblasting;i=6116"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=shotblasting;i=6117",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=shotblasting;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=bacnet;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=shotblasting;i=6118",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=shotblasting;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=bacnet;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a list of information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data. "
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=shotblasting;i=7002",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=shotblasting;i=6117"]),
    outputArgs=o6.hasProperty(o6.ns["ns=shotblasting;i=6118"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=shotblasting;i=5059",
    browseName="ns=machinery_jobs;JobOrderResults",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=7001"]), o6.hasComponent(o6.ns["ns=shotblasting;i=7002"])],
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=shotblasting;i=5057",
    browseName="ns=machinery_jobs;JobManagement",
    references=[o6.hasComponent(o6.ns["ns=shotblasting;i=5058"]), o6.hasComponent(o6.ns["ns=shotblasting;i=5059"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=shotblasting;i=5005",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=shotblasting;i=5053", browseName="ns=machinery;OperationCounter")),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5054"]),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5055"]),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5056"]),
        o6.hasAddIn(o6.ns["ns=shotblasting;i=5057"]),
    ],
)
o6.reference(shotblasting_objtypes.ShotBlastMachineType, ns0.reftypes.HasComponent, o6.ns["ns=shotblasting;i=5005"])
o6.reference(o6.ns["ns=shotblasting;i=5005"], "i=17604", o6.ns["ns=shotblasting;i=5002"])
o6.reference(o6.ns["ns=shotblasting;i=5005"], "i=17604", o6.ns["ns=shotblasting;i=5027"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, shotblasting_objtypes
