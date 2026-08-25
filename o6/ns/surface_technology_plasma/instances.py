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

"""Generated OPC UA surface_technology_plasma namespace declarations."""

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
from . import objtypes as surface_technology_plasma_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_plasma;i=5036",
    browseName="ns=machinery;Components",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            surface_technology_plasma_objtypes.RegulatorType(
                nodeId="ns=surface_technology_plasma;i=5040", browseName="ns=surface_technology_plasma;<PrecursorRegulator>", modellingRule="OptionalPlaceholder"
            )
        )
    ],
)
o6.reference(surface_technology_plasma_objtypes.PrecursorSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5036"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5038"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5036"])
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_plasma;i=5042",
    browseName="ns=machinery;Components",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            surface_technology_plasma_objtypes.RegulatorType(
                nodeId="ns=surface_technology_plasma;i=5046", browseName="ns=surface_technology_plasma;<GasRegulator>", modellingRule="OptionalPlaceholder"
            )
        )
    ],
)
o6.reference(surface_technology_plasma_objtypes.GasSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5042"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5044"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5042"])
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_plasma;i=5048",
    browseName="ns=machinery;Components",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            surface_technology_plasma_objtypes.CirculationSystemType(
                nodeId="ns=surface_technology_plasma;i=5051", browseName="ns=surface_technology_plasma;<CirculationSystem>", modellingRule="OptionalPlaceholder"
            )
        )
    ],
)
o6.reference(surface_technology_plasma_objtypes.PlantCoolingSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5048"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5050"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5048"])
machinery.objtypes.MachineComponentsType(nodeId="ns=surface_technology_plasma;i=5073", browseName="ns=machinery;Components")
ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5074", browseName="ns=machinery;MachineryBuildingBlocks")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5074"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5073"])
machinery.objtypes.MonitoringType(nodeId="ns=surface_technology_plasma;i=5075", browseName="ns=machinery;Monitoring")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5074"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5075"])
surface_technology_plasma_objtypes.GasSystemType(
    nodeId="ns=surface_technology_plasma;i=5013",
    browseName="ns=surface_technology_plasma;<GasSystem>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5074"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5075"]),
        o6.hasAddIn(o6.ns["ns=surface_technology_plasma;i=5073"]),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5077", browseName="ns=machinery;MachineryBuildingBlocks")
machinery.objtypes.MonitoringType(nodeId="ns=surface_technology_plasma;i=5078", browseName="ns=machinery;Monitoring")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5077"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5078"])
ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5079", browseName="ns=machinery;MachineryBuildingBlocks")
machinery.objtypes.MonitoringType(nodeId="ns=surface_technology_plasma;i=5080", browseName="ns=machinery;Monitoring")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5079"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5080"])
surface_technology_plasma_objtypes.PlasmaGeneratorType(
    nodeId="ns=surface_technology_plasma;i=5011",
    browseName="ns=surface_technology_plasma;<PlasmaGenerator>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5079"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5080"])],
)
machinery.objtypes.MachineComponentsType(nodeId="ns=surface_technology_plasma;i=5081", browseName="ns=machinery;Components")
ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5082", browseName="ns=machinery;MachineryBuildingBlocks")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5082"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5081"])
machinery.objtypes.MonitoringType(nodeId="ns=surface_technology_plasma;i=5083", browseName="ns=machinery;Monitoring")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5082"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5083"])
surface_technology_plasma_objtypes.PrecursorSystemType(
    nodeId="ns=surface_technology_plasma;i=5012",
    browseName="ns=surface_technology_plasma;<PrecursorSystem>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5082"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5083"]),
        o6.hasAddIn(o6.ns["ns=surface_technology_plasma;i=5081"]),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5084", browseName="ns=machinery;MachineryBuildingBlocks")
machinery.objtypes.MonitoringType(nodeId="ns=surface_technology_plasma;i=5085", browseName="ns=machinery;Monitoring")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5084"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5085"])
surface_technology_plasma_objtypes.HeatingSystemType(
    nodeId="ns=surface_technology_plasma;i=5022",
    browseName="ns=surface_technology_plasma;<HeatingSystem>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5084"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5085"])],
)
ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5086", browseName="ns=machinery;MachineryBuildingBlocks")
machinery.objtypes.MonitoringType(nodeId="ns=surface_technology_plasma;i=5087", browseName="ns=machinery;Monitoring")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5086"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5087"])
surface_technology_plasma_objtypes.ProcessingChamberType(
    nodeId="ns=surface_technology_plasma;i=5021",
    browseName="ns=surface_technology_plasma;<ProcessingChamber>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5086"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5087"])],
)
ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5088", browseName="ns=machinery;MachineryBuildingBlocks")
machinery.objtypes.MonitoringType(nodeId="ns=surface_technology_plasma;i=5089", browseName="ns=machinery;Monitoring")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5088"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5089"])
surface_technology_plasma_objtypes.WorkpieceMotionDeviceType(
    nodeId="ns=surface_technology_plasma;i=5023",
    browseName="ns=surface_technology_plasma;<WorkpieceMotionDevice>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5088"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5089"])],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_plasma;i=5018",
    browseName="ns=machinery;Components",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5021"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5022"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5023"]),
    ],
)
o6.reference(surface_technology_plasma_objtypes.LowPressurePlasmaSurfaceMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5018"])
ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5095", browseName="ns=machinery;MachineryBuildingBlocks")
machinery.objtypes.MonitoringType(nodeId="ns=surface_technology_plasma;i=5096", browseName="ns=machinery;Monitoring")
o6.reference(o6.ns["ns=surface_technology_plasma;i=5095"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5096"])
surface_technology_plasma_objtypes.PlasmaJetType(
    nodeId="ns=surface_technology_plasma;i=5019",
    browseName="ns=surface_technology_plasma;<PlasmaJet>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5095"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5096"])],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_plasma;i=5026",
    browseName="ns=machinery;Components",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5019"])],
)
o6.reference(surface_technology_plasma_objtypes.AtmosphericPressurePlasmaSurfaceMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5026"])
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_plasma;i=5076",
    browseName="ns=machinery;Components",
    references=[
        o6.hasComponent(
            surface_technology_plasma_objtypes.CirculationSystemType(
                nodeId="ns=surface_technology_plasma;i=5104", browseName="ns=surface_technology_plasma;<CirculationSystem>", modellingRule="OptionalPlaceholder"
            )
        )
    ],
)
o6.reference(o6.ns["ns=surface_technology_plasma;i=5077"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5076"])
surface_technology_plasma_objtypes.PlantCoolingSystemType(
    nodeId="ns=surface_technology_plasma;i=5014",
    browseName="ns=surface_technology_plasma;<PlantCoolingSystem>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5077"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5078"]),
        o6.hasAddIn(o6.ns["ns=surface_technology_plasma;i=5076"]),
    ],
)
machinery.objtypes.MachineComponentsType(
    nodeId="ns=surface_technology_plasma;i=5003",
    browseName="ns=machinery;Components",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5011"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5012"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5013"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5014"]),
    ],
)
o6.reference(surface_technology_plasma_objtypes.PlasmaSurfaceMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5003"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5010"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5003"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashSurfaceTechnologySlashPlasmaSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=surface_technology_plasma;i=5001",
    browseName="ns=surface_technology_plasma;http://opcfoundation.org/UA/SurfaceTechnology/Plasma/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-01-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/SurfaceTechnology/Plasma/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6005",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6010", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5002",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6008",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6009",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6011",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.PlasmaSurfaceMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5002"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5010"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5002"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6012",
    browseName="ns=surface_technology_plasma;BiasArcCounter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6013", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology_plasma;i=6016",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6017", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=surface_technology_plasma;i=5008",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6022", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6016"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=surface_technology_plasma;i=6018",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=surface_technology_plasma;i=6019",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=surface_technology_plasma;i=6020",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=surface_technology_plasma;i=6021",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=surface_technology_plasma;i=6023",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=surface_technology_plasma;i=6024",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=surface_technology_plasma;i=6025",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6030",
    browseName="ns=surface_technology_plasma;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6031", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5015",
    browseName="ns=machinery;Consumption",
    description="Entry point for consumption information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6030"])],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6032",
    browseName="ns=surface_technology_plasma;SubstrateTemperature",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6033", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5016",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6032"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5017",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6034", browseName="ns=surface_technology_plasma;MainSwitchOn", dataType=o6.Boolean))
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5004",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5015"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5016"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5017"]),
    ],
)
o6.reference(surface_technology_plasma_objtypes.PlasmaSurfaceMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5004"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5010"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5004"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5030",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6035",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6036",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.PlasmaGeneratorType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5030"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5032"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5030"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6037",
    browseName="ns=surface_technology_plasma;EvaporatorCurrent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6038", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6039",
    browseName="ns=surface_technology_plasma;EvaporatorVoltage",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6040", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6041",
    browseName="ns=surface_technology_plasma;EvaporatorPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6042", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6044",
    browseName="ns=surface_technology_plasma;BiasDutyCycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6045", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6015",
    browseName="ns=surface_technology_plasma;BiasPulseFrequency",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6043", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6046", browseName="ns=surface_technology_plasma;BiasPolarity", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6044"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6049",
    browseName="ns=surface_technology_plasma;BiasCurrent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6050", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6051",
    browseName="ns=surface_technology_plasma;BiasVoltage",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6052", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6053",
    browseName="ns=surface_technology_plasma;BiasPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6054", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5034",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6014", browseName="ns=surface_technology_plasma;EvaporatorGeneratorSwitchOn", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6055", browseName="ns=surface_technology_plasma;BiasGeneratorSwitchOn", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6056", browseName="ns=surface_technology_plasma;PlasmaReadyToStart", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6057", browseName="ns=surface_technology_plasma;PlasmaActive", dataType=o6.Boolean)),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6060",
    browseName="ns=surface_technology_plasma;EvaporatorDutyCycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6061", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6058",
    browseName="ns=surface_technology_plasma;EvaporatorPulseFrequency",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6047", browseName="ns=surface_technology_plasma;EvaporatorPolarity", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6059", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6060"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6048",
    browseName="ns=surface_technology_plasma;EvaporatorReversePower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6062", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6063",
    browseName="ns=surface_technology_plasma;BiasReversePower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6064", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5033",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6012"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6015"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6037"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6039"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6041"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6048"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6049"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6051"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6053"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6058"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6063"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5031",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5033"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5034"])],
)
o6.reference(surface_technology_plasma_objtypes.PlasmaGeneratorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5031"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5032"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5031"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5035",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6065",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6066",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.PrecursorSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5035"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5038"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5035"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6067",
    browseName="ns=surface_technology_plasma;PrimaryPressureControl",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6068", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5039",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6067"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5037",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5039"])],
)
o6.reference(surface_technology_plasma_objtypes.PrecursorSystemType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5037"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5038"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5037"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5041",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6069",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6070",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.GasSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5041"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5044"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5041"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6071",
    browseName="ns=surface_technology_plasma;PrimaryPressureControl",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5045",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6071"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5043",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5045"])],
)
o6.reference(surface_technology_plasma_objtypes.GasSystemType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5043"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5044"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5043"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6073",
    browseName="ns=surface_technology_plasma;GasFlow",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6074", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6073"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6075",
    browseName="ns=surface_technology_plasma;GasConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6076", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6075"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6077",
    browseName="ns=surface_technology_plasma;PrecursorMassFlow",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6078", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6077"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6079",
    browseName="ns=surface_technology_plasma;PrecursorVolumeFlow",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6080", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6079"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6081",
    browseName="ns=surface_technology_plasma;TFittingTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6082", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6081"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6083",
    browseName="ns=surface_technology_plasma;HeaterTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6084", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6083"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6085",
    browseName="ns=surface_technology_plasma;JetHeadTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6086", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6085"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_plasma;i=6088",
    browseName="ns=surface_technology_plasma;TypeOfGas",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6089",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Ar")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("N2")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CH4")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("C2H2")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("O2")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("H2")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6090", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6088"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=surface_technology_plasma;i=6091",
    browseName="ns=surface_technology_plasma;TypeOfPrecursorFluid",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6092",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Ar")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("N2")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CH4")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("C2H2")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("O2")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("H2")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6093", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(surface_technology_plasma_objtypes.RegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6091"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5047",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6094",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6095",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.PlantCoolingSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5047"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5050"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5047"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6096",
    browseName="ns=surface_technology_plasma;FlowRate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6097", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6098",
    browseName="ns=surface_technology_plasma;CoolingSystemTemperatureOutlet",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6099", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6100",
    browseName="ns=surface_technology_plasma;CoolingSystemTemperatureInlet",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6102",
    browseName="ns=surface_technology_plasma;CoolingSystemPressureInlet",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6103", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6104",
    browseName="ns=surface_technology_plasma;CoolingSystemPressureOutlet",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6105", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5052",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6096"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6098"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6100"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6102"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6104"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5049",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5052"])],
)
o6.reference(surface_technology_plasma_objtypes.PlantCoolingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5049"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5050"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5049"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6106",
    browseName="ns=surface_technology_plasma;CoolingCircuitTemperatureOutlet",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6107", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.CirculationSystemType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6106"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6108",
    browseName="ns=surface_technology_plasma;CoolingCircuitFlowRate",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6109", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(surface_technology_plasma_objtypes.CirculationSystemType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=6108"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5053",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6110",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6111",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.ProcessingChamberType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5053"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5056"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5053"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6112",
    browseName="ns=surface_technology_plasma;ChamberPrePressure",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6114",
    browseName="ns=surface_technology_plasma;ChamberPressure",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6115", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6116",
    browseName="ns=surface_technology_plasma;ChamberTemperature",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6117", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6118",
    browseName="ns=surface_technology_plasma;LeakRate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6119", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5057",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6120", browseName="ns=surface_technology_plasma;PumpDownTime", dataType=ns0.datatypes.DurationString)
        ),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6112"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6114"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6116"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6118"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5054",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5057"])],
)
o6.reference(surface_technology_plasma_objtypes.ProcessingChamberType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5054"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5056"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5054"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5058",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6121",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6122",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.HeatingSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5058"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5060"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5058"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6123",
    browseName="ns=surface_technology_plasma;HeaterCurrent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6124", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6125",
    browseName="ns=surface_technology_plasma;HeaterVoltage",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6126", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6127",
    browseName="ns=surface_technology_plasma;HeaterPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6128", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6129",
    browseName="ns=surface_technology_plasma;HeaterTemperature",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6130", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5061",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6123"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6125"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6127"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6129"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5059",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5061"])],
)
o6.reference(surface_technology_plasma_objtypes.HeatingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5059"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5060"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5059"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5062",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6131",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6132",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.WorkpieceMotionDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5062"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5064"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5062"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6133",
    browseName="ns=surface_technology_plasma;RotationSpeed",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6134", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6135", browseName="ns=surface_technology_plasma;RotationDirection", dataType=o6.Boolean)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6136",
    browseName="ns=surface_technology_plasma;RotationPosition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6137", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Int16,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6139",
    browseName="ns=surface_technology_plasma;ZMotionSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6140", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6141",
    browseName="ns=surface_technology_plasma;ZMotionPosition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6142", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Int16,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=surface_technology_plasma;i=6138",
    browseName="ns=surface_technology_plasma;ZMotion",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6139"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6141"])],
    dataType=o6.Boolean,
    value=False,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5065",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6133"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6136"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6138"]),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5063",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5065"])],
)
o6.reference(surface_technology_plasma_objtypes.WorkpieceMotionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5063"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5064"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5063"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology_plasma;i=5066",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6143",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology_plasma;i=6144",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_plasma_objtypes.PlasmaJetType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5066"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5070"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5066"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6149",
    browseName="ns=surface_technology_plasma;PlasmaVoltage",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6150", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6151",
    browseName="ns=surface_technology_plasma;PlasmaCurrent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6152", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6153",
    browseName="ns=surface_technology_plasma;PlasmaJetPressure",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6154", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6155",
    browseName="ns=surface_technology_plasma;PlasmaJetRotation",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6156", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6157",
    browseName="ns=surface_technology_plasma;PlasmaJetFlow",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6158", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6159",
    browseName="ns=surface_technology_plasma;PlasmaJetPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6160", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6161",
    browseName="ns=surface_technology_plasma;PlasmaFrequency",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6162", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=surface_technology_plasma;i=6163",
    browseName="ns=surface_technology_plasma;PlasmaCycleTime",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6164", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt16,
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5071",
    browseName="ns=machinery;Process",
    description="Entry point for process information of the MachineryItem.",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6149"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6151"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6153"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6155"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6157"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6159"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6161"]),
        o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6163"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5072",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6165", browseName="ns=surface_technology_plasma;TransformatorInformation", dataType=o6.String)
        )
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5067",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5071"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5072"])],
)
o6.reference(surface_technology_plasma_objtypes.PlasmaJetType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5067"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5070"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5067"])
ns0.objtypes.StateType(
    nodeId="ns=surface_technology_plasma;i=5091",
    browseName="ns=surface_technology_plasma;Vented",
    description="The machine is being prepared for the next run",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6167", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(surface_technology_plasma_objtypes.LowPressurePlasmaNotExecutingSubState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5091"])
ns0.objtypes.StateType(
    nodeId="ns=surface_technology_plasma;i=5092",
    browseName="ns=surface_technology_plasma;Standby",
    description="The vacuum chamber is evacuated and the system is ready to start",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6168", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(surface_technology_plasma_objtypes.LowPressurePlasmaNotExecutingSubState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5092"])
ns0.objtypes.TransitionType(
    nodeId="ns=surface_technology_plasma;i=5093",
    browseName="ns=surface_technology_plasma;FromStandbyToVented",
    description="Transition from state Standby to state Vented",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6169", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(surface_technology_plasma_objtypes.LowPressurePlasmaNotExecutingSubState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5093"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5093"], "i=51", o6.ns["ns=surface_technology_plasma;i=5092"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5093"], "i=52", o6.ns["ns=surface_technology_plasma;i=5091"])
ns0.objtypes.TransitionType(
    nodeId="ns=surface_technology_plasma;i=5094",
    browseName="ns=surface_technology_plasma;FromVentedToStandby",
    description="Transition from state Vented to state Standby",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6170", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(surface_technology_plasma_objtypes.LowPressurePlasmaNotExecutingSubState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5094"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5094"], "i=51", o6.ns["ns=surface_technology_plasma;i=5091"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5094"], "i=52", o6.ns["ns=surface_technology_plasma;i=5092"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology_plasma;i=6171",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6172", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
surface_technology_plasma_objtypes.LowPressurePlasmaNotExecutingSubState_StateMachineType(
    nodeId="ns=surface_technology_plasma;i=5090",
    browseName="ns=surface_technology_plasma;LowPressurePlasmaNotExecutingSubState",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6171"])],
)
o6.reference(surface_technology_plasma_objtypes.LowPressurePlasmaMachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5090"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5090"], "i=117", "ns=machinery;i=5007", inverse=True)
ns0.objtypes.StateType(
    nodeId="ns=surface_technology_plasma;i=5097",
    browseName="ns=surface_technology_plasma;Idle",
    description="The machine is being prepared for the next run",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6174", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(
    surface_technology_plasma_objtypes.AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5097"]
)
ns0.objtypes.StateType(
    nodeId="ns=surface_technology_plasma;i=5098",
    browseName="ns=surface_technology_plasma;Standby",
    description="The system is ready to start",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6175", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(
    surface_technology_plasma_objtypes.AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5098"]
)
ns0.objtypes.TransitionType(
    nodeId="ns=surface_technology_plasma;i=5099",
    browseName="ns=surface_technology_plasma;FromStandbyToIdle",
    description="Transition from state Standby to state Idle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6176", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(
    surface_technology_plasma_objtypes.AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5099"]
)
o6.reference(o6.ns["ns=surface_technology_plasma;i=5099"], "i=51", o6.ns["ns=surface_technology_plasma;i=5098"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5099"], "i=52", o6.ns["ns=surface_technology_plasma;i=5097"])
ns0.objtypes.TransitionType(
    nodeId="ns=surface_technology_plasma;i=5100",
    browseName="ns=surface_technology_plasma;FromIdleToStandby",
    description="Transition from state Idle to state Standby",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6177", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(
    surface_technology_plasma_objtypes.AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5100"]
)
o6.reference(o6.ns["ns=surface_technology_plasma;i=5100"], "i=51", o6.ns["ns=surface_technology_plasma;i=5097"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5100"], "i=52", o6.ns["ns=surface_technology_plasma;i=5098"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology_plasma;i=6178",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6179", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
surface_technology_plasma_objtypes.AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType(
    nodeId="ns=surface_technology_plasma;i=5101",
    browseName="ns=surface_technology_plasma;AtmosphericPressurePlasmaNotExecutingSubState",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6178"])],
)
o6.reference(
    surface_technology_plasma_objtypes.AtmosphericPressurePlasmaMachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5101"]
)
o6.reference(o6.ns["ns=surface_technology_plasma;i=5101"], "i=117", "ns=machinery;i=5007", inverse=True)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology_plasma;i=6180",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6181", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
surface_technology_plasma_objtypes.AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType(
    nodeId="ns=surface_technology_plasma;i=5102",
    browseName="ns=surface_technology_plasma;AtmosphericPressurePlasmaNotExecutingSubState",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6180"])],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology_plasma;i=6182",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6183", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
surface_technology_plasma_objtypes.AtmosphericPressurePlasmaMachineryItemState_StateMachineType(
    nodeId="ns=surface_technology_plasma;i=5029",
    browseName="ns=machinery;MachineryItemState",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5102"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6182"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5028",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    references=[o6.hasAddIn(o6.ns["ns=surface_technology_plasma;i=5029"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5027",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5028"])],
)
o6.reference(surface_technology_plasma_objtypes.AtmosphericPressurePlasmaSurfaceMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5027"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology_plasma;i=6184",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6185", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
surface_technology_plasma_objtypes.LowPressurePlasmaNotExecutingSubState_StateMachineType(
    nodeId="ns=surface_technology_plasma;i=5103",
    browseName="ns=surface_technology_plasma;LowPressurePlasmaNotExecutingSubState",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6184"])],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology_plasma;i=6186",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology_plasma;i=6187", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
surface_technology_plasma_objtypes.LowPressurePlasmaMachineryItemState_StateMachineType(
    nodeId="ns=surface_technology_plasma;i=5025",
    browseName="ns=machinery;MachineryItemState",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5103"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=6186"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology_plasma;i=5024",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    references=[o6.hasAddIn(o6.ns["ns=surface_technology_plasma;i=5025"])],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology_plasma;i=5020",
    browseName="ns=machinery;Monitoring",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5024"])],
)
o6.reference(surface_technology_plasma_objtypes.LowPressurePlasmaSurfaceMachineType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology_plasma;i=5020"])


ns0.vartypes.PropertyType(
    nodeId="ns=surface_technology_plasma;i=6026",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology_plasma;i=7001",
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
    nodeId="ns=surface_technology_plasma;i=6027",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology_plasma;i=7001",
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
    nodeId="ns=surface_technology_plasma;i=7001",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=surface_technology_plasma;i=6026"]),
    outputArgs=o6.hasProperty(o6.ns["ns=surface_technology_plasma;i=6027"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=surface_technology_plasma;i=6028",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology_plasma;i=7002",
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
    nodeId="ns=surface_technology_plasma;i=6029",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology_plasma;i=7002",
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
    nodeId="ns=surface_technology_plasma;i=7002",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=surface_technology_plasma;i=6028"]),
    outputArgs=o6.hasProperty(o6.ns["ns=surface_technology_plasma;i=6029"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=surface_technology_plasma;i=5009",
    browseName="ns=machinery_jobs;JobOrderResults",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=7001"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=7002"])],
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=surface_technology_plasma;i=5007",
    browseName="ns=machinery_jobs;JobManagement",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5008"]), o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5009"])],
)
o6.reference(surface_technology_plasma_objtypes.PlasmaSurfaceMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology_plasma;i=5007"])
o6.reference(o6.ns["ns=surface_technology_plasma;i=5010"], "i=17604", o6.ns["ns=surface_technology_plasma;i=5007"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, surface_technology_plasma_objtypes
