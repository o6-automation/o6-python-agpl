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

"""Generated OPC UA cas namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as cas_datypes
from . import objtypes as cas_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=cas;i=5042", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=cas;i=5043", browseName="Default XML")
o6.hasEncoding(cas_datypes.FilterClassDataType, o6.ns["ns=cas;i=5043"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=cas;i=5044", browseName="Default JSON")
o6.hasEncoding(cas_datypes.FilterClassDataType, o6.ns["ns=cas;i=5044"])
compressors = ns0.objtypes.FolderType(nodeId="ns=cas;i=5117", browseName="ns=cas;Compressors")
cas_objtypes.AirnetComponentsType(
    nodeId="ns=cas;i=5047",
    browseName="ns=machinery;Components",
    description="Organizes components assigned to the airnet.",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=cas;i=5069", browseName="ns=cas;ChargingSystems", description="Organizes all charging systems connected to the airnet.")
        ),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5095", browseName="ns=cas;Compressors", description="Organizes all compressors connected to the airnet.")),
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=cas;i=5105", browseName="ns=cas;CondensateDrains", description="Organizes all condensate drains connected to the airnet.")
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=cas;i=5106", browseName="ns=cas;CondensateSeparators", description="Organizes all condensate separators connected to the airnet.")
        ),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5107", browseName="ns=cas;Converters", description="Organizes all converters connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5111", browseName="ns=cas;CoolingSystems", description="Organizes all cooling systems connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5113", browseName="ns=cas;Dryers", description="Organizes all dryers connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5114", browseName="ns=cas;Filters", description="Organizes all filters connected to the airnet.")),
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=cas;i=5118", browseName="ns=cas;HeatRecoverySystems", description="Organizes all heat recovery systems connected to the airnet.")
        ),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5119", browseName="ns=cas;Receivers", description="Organizes all receivers connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5122", browseName="ns=cas;Sensors", description="Organizes all sensors connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5128", browseName="ns=cas;Valves", description="Organizes all valves connected to the airnet.")),
    ],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=cas;i=5175", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=cas;i=5176", browseName="Default XML")
o6.hasEncoding(cas_datypes.SensorTechnologyOptionSet, o6.ns["ns=cas;i=5176"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=cas;i=5177", browseName="Default JSON")
o6.hasEncoding(cas_datypes.SensorTechnologyOptionSet, o6.ns["ns=cas;i=5177"])
cas_objtypes.ComponentsGroupType(
    nodeId="ns=cas;i=5013",
    browseName="ns=machinery;Components",
    description="All components in a compressed air system as browsable objects.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5197", browseName="ns=cas;ChargingSystems", description="Organizes all charging systems connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5198", browseName="ns=cas;Compressors", description="Organizes all compressors connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5199", browseName="ns=cas;CondensateDrains", description="Organizes all condensate drains connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5200", browseName="ns=cas;CondensateSeparators", description="Organizes all condensate separators connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5203", browseName="ns=cas;Converters", description="Organizes all converters connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5204", browseName="ns=cas;CoolingSystems", description="Organizes all cooling systems connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(nodeId="ns=cas;i=5205", browseName="ns=cas;Dryers", description="Organizes all dryers connected to the compressed air system.")
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5207", browseName="ns=cas;Filters", description="Organizes all filters connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5208", browseName="ns=cas;HeatRecoverySystems", description="Organizes all heat recovery systems connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5209", browseName="ns=cas;Receivers", description="Organizes all receivers connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(
                nodeId="ns=cas;i=5210", browseName="ns=cas;Sensors", description="Organizes all sensors connected to the compressed air system."
            )
        ),
        o6.hasComponent(
            machinery.objtypes.MachineComponentsType(nodeId="ns=cas;i=5211", browseName="ns=cas;Valves", description="Organizes all valves connected to the compressed air system.")
        ),
    ],
)
o6.reference(cas_objtypes.CASType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5013"])
cas_objtypes.AirnetComponentsType(
    nodeId="ns=cas;i=5001",
    browseName="ns=machinery;Components",
    description="Organizes components assigned to the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=cas;i=5223", browseName="ns=cas;ChargingSystems", description="Organizes all charging systems connected to the airnet.")
        ),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5224", browseName="ns=cas;Compressors", description="Organizes all compressors connected to the airnet.")),
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=cas;i=5225", browseName="ns=cas;CondensateDrains", description="Organizes all condensate drains connected to the airnet.")
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=cas;i=5226", browseName="ns=cas;CondensateSeparators", description="Organizes all condensate separators connected to the airnet.")
        ),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5227", browseName="ns=cas;Converters", description="Organizes all converters connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5228", browseName="ns=cas;CoolingSystems", description="Organizes all cooling systems connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5229", browseName="ns=cas;Dryers", description="Organizes all dryers connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5230", browseName="ns=cas;Filters", description="Organizes all filters connected to the airnet.")),
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=cas;i=5231", browseName="ns=cas;HeatRecoverySystems", description="Organizes all heat recovery systems connected to the airnet.")
        ),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5232", browseName="ns=cas;Receivers", description="Organizes all receivers connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5233", browseName="ns=cas;Sensors", description="Organizes all sensors connected to the airnet.")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=cas;i=5234", browseName="ns=cas;Valves", description="Organizes all valves connected to the airnet.")),
    ],
)
o6.reference(cas_objtypes.AirnetType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5001"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6009",
    browseName="ns=cas;FluidType",
    description="Enumeration of possible process fluid types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6013", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FluidTypeEnum,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6002",
    browseName="ns=cas;RealTime",
    description="Real time passed since last counter reset.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6018", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6020", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6028", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6030", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.StatisticsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6002"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6017",
    browseName="ns=cas;CompressorsIntegrated",
    description="Number of integrated compressors in the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6033", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6034", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6037", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6038", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6039", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6017"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6073",
    browseName="ns=cas;CompressorsIntegrated",
    description="Number of integrated compressors in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6035", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6036", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6040", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6041", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6074", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6006",
    browseName="ns=cas;RunningTime",
    description="Time spent running since last counter reset.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6032", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6050", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6077", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6081", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.StatisticsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6006"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6071",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible compressor types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6092", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.CompressorTypeEnum,
)
o6.reference(cas_objtypes.CompressorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6071"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6027",
    browseName="ns=cas;CompressorsNotAvailable",
    description="Number of unavailable compressors in the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6076", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6079", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6095", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6096", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6097", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6027"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6078",
    browseName="ns=cas;CompressorsNotAvailable",
    description="Number of unavailable compressors in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6100", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6102", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6103", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6104", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6086",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible dryer types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6116", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.DryerTypeEnum,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6083",
    browseName="ns=cas;LoadedTime",
    description="Time spent in loaded state since last counter reset.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6123", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6124", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6125", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6126", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6127", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.CompressorStatisticsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6083"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6064",
    browseName="ns=cas;HealthState",
    description="Actual health state of the part.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6130", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6131", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Enumeration,
)
o6.reference(cas_objtypes.OperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6064"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6121",
    browseName="ns=cas;LowestAmbientTemperature",
    description="Lowest allowable ambient temperature for the dryer to work as intended.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6135", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6138", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6139", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
cas_objtypes.DryerDesignType(
    nodeId="ns=cas;i=5057",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6086"]), o6.hasComponent(o6.ns["ns=cas;i=6121"])],
)
o6.reference(cas_objtypes.DryerType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5057"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6093",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6143", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6144", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6145", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6146", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6147", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6148", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.ElectricalQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6093"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6094",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6150", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6151", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6152", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6153", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6154", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.ElectricalQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6094"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6099",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6155", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6156", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6157", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6158", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6162", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6163", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.ElectricalQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6099"])
cas_objtypes.DesignType(
    nodeId="ns=cas;i=5073",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cas;i=6172",
                browseName="ns=cas;ComponentClass",
                description="Enumeration of possible types of the component’s device class.",
                dataType=ns0.datatypes.Enumeration,
            )
        )
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6112",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6164", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6165", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6166", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6167", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6168", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6173", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.ElectricalQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6112"])
cas_objtypes.CASIdentificationType(
    nodeId="ns=cas;i=5009",
    browseName="ns=di;Identification",
    description="Identification properties of the topology element.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6180", browseName="ns=cas;AssetId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6181", browseName="ns=cas;ComponentName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6182", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
o6.reference(cas_objtypes.AirnetType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5009"])
cas_objtypes.CASIdentificationType(
    nodeId="ns=cas;i=5030",
    browseName="ns=di;Identification",
    description="Identification properties of the topology element.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6190", browseName="ns=cas;AssetId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6191", browseName="ns=cas;ComponentName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6192", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6161",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6196", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6197", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6198", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6199", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6200", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6201", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6161"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=cas;i=6193",
    browseName="ns=cas;OperatingProfiles",
    description="Configured operating profile for an airnet in a compressed air system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6202",
                browseName="EnumStrings",
                description="Available operating profiles for an airnet in a compressed air system.",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[3],
                value=[o6.LocalizedText("Profile0", "0"), o6.LocalizedText("Profile1", "1"), o6.LocalizedText("Profile2")],
            )
        )
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6170",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6205", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6206", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6207", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6208", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6209", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6210", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6170"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6067",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the compressor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6068", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6217", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.CompressorOperatingStateEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6061",
    browseName="ns=cas;ActivePressureBand",
    description="Indicates the actual active pressure band.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6218", browseName="Definition", dataType=o6.String))],
    dataType=o6.UInt16,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6065",
    browseName="ns=cas;IntegratedState",
    description="Actual integrated state of the part.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6132", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6222", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Enumeration,
)
o6.reference(cas_objtypes.OperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6065"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6122",
    browseName="ns=cas;UnloadedTime",
    description="Time spent in unloaded state since last counter reset.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6136", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6226", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6227", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6228", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6229", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.CompressorStatisticsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6122"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6174",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6184", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6185", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6186", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6215", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6236", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6237", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6175",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6238", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6239", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6240", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6241", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6242", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6243", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6176",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6244", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6245", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6248", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6249", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6252", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=cas;i=6255",
    browseName="ns=cas;OperatingModes",
    description="Configured operating mode for an airnet in a compressed air system.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6257",
                browseName="EnumStrings",
                description="Available operating modes for an airnet in a compressed air system.",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.LocalizedText("stopped", "0")],
            )
        )
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(cas_objtypes.AirnetConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6255"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=cas;i=6260",
    browseName="ns=cas;OperatingProfiles",
    description="Configured operating profile for an airnet in a compressed air system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6261",
                browseName="EnumStrings",
                description="Available operating profiles for an airnet in a compressed air system.",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[0],
            )
        )
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(cas_objtypes.AirnetConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6260"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6005",
    browseName="ns=cas;RealTimeToNextService",
    description="Real time left until the real time of the next service level is exceeded.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6007", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6008", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6262", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6263", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6264", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.StatisticsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6005"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=cas;i=6265",
    browseName="ns=cas;OperatingModes",
    description="Configured operating mode for an airnet in a compressed air system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6266",
                browseName="EnumStrings",
                description="Available operating modes for an airnet in a compressed air system.",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.LocalizedText("Stopped", "0")],
            )
        )
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=cas;i=6267",
    browseName="ns=cas;OperatingProfiles",
    description="Configured operating profile for an airnet in a compressed air system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6268",
                browseName="EnumStrings",
                description="Available operating profiles for an airnet in a compressed air system.",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[3],
                value=[o6.LocalizedText("Profile0", "0"), o6.LocalizedText("Profile1", "1"), o6.LocalizedText("Profile2")],
            )
        )
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
cas_objtypes.AirnetConfigurationType(
    nodeId="ns=cas;i=5015",
    browseName="ns=di;Configuration",
    description="Configure the behavior of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6232", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.ns["ns=cas;i=6265"]),
        o6.hasComponent(o6.ns["ns=cas;i=6267"]),
    ],
)
o6.reference(cas_objtypes.AirnetType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5015"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6022",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible types of the component’s device class.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6269", browseName="Definition", dataType=o6.String))],
    dataType=ns0.datatypes.Enumeration,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6171",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6211", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6212", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6254", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6256", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6258", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6270", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6171"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6177",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6253", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6275", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6276", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6277", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6278", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6279", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6273",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible types of the component’s device class.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6282", browseName="Definition", dataType=o6.String))],
    dataType=ns0.datatypes.Enumeration,
)
o6.reference(cas_objtypes.DesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6273"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6274",
    browseName="ns=cas;FluidType",
    description="Enumeration of possible fluid types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6284", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FluidTypeEnum,
)
o6.reference(cas_objtypes.FluidCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6274"])
di.vartypes.UIElementType(nodeId="ns=cas;i=6295", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
cas_objtypes.CASIdentificationType(
    nodeId="ns=cas;i=5003",
    browseName="ns=di;Identification",
    description="Identification properties of the compressed air system.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6234", browseName="ns=cas;AssetId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6235", browseName="ns=cas;ComponentName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=cas;i=6295"]),
    ],
)
o6.reference(cas_objtypes.CASType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5003"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6293",
    browseName="ns=cas;LastCalibrationDate",
    description="Date when the sensor was last calibrated.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6296", browseName="Definition", dataType=o6.String))],
    dataType=o6.DateTime,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6178",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6271", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6272", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6281", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6283", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6308", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6309", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6178"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6328",
    browseName="OptionSetValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        o6.LocalizedText("CapacitiveSensor"),
        o6.LocalizedText("ElectronTube"),
        o6.LocalizedText("InductiveSensor"),
        o6.LocalizedText("IonizationSensor"),
        o6.LocalizedText("Magnetometer"),
        o6.LocalizedText("OpticalSensor"),
        o6.LocalizedText("PiezoelectricSensor"),
        o6.LocalizedText("ResistiveSensor"),
        o6.LocalizedText("ResonantSensor"),
        o6.LocalizedText("TemperatureSensor"),
        o6.LocalizedText("ThermalSensor"),
        o6.LocalizedText("UltrasoundSensor"),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6053",
    browseName="ns=cas;RealTime",
    description="Real time passed since last counter reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6321", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6322", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6331", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6333", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6052",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible compressor types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6335", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.CompressorTypeEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6316",
    browseName="ns=cas;DisplacementType",
    description="Enumeration of possible displacement types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6336", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.DisplacementTypeEnum,
)
o6.reference(cas_objtypes.CompressorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6316"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6317",
    browseName="ns=cas;LubricationType",
    description="Enumeration of possible lubrication types for the compression process of a compressor.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6337", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.LubricationTypeEnum,
)
o6.reference(cas_objtypes.CompressorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6317"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6318",
    browseName="ns=cas;NumberOfStages",
    description="Number of stages the compressor has available.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6338", browseName="Definition", dataType=o6.String))],
    dataType=o6.UInt16,
)
o6.reference(cas_objtypes.CompressorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6318"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=6319",
    browseName="ns=cas;VariableFlow",
    description="Indicates if a compressor has a variable or fixed flow.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6320",
                browseName="FalseState",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("'Fixed flow' means the product offers no control for changing the volume flow independent of pressure."),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6329",
                browseName="TrueState",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(
                    "'Variable flow' means the compressor package allows an intentional change in volume flow rate, most obviously by VSD but also by adjustable guide vanes in turbo compressors or by valve controls in piston compressors or other means."
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6339", browseName="Definition", dataType=o6.String)),
    ],
    dataType=o6.Boolean,
)
o6.reference(cas_objtypes.CompressorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6319"])
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6291",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6342", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6340",
    browseName="ns=cas;DisplacementType",
    description="Enumeration of possible displacement types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6372", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.DisplacementTypeEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6341",
    browseName="ns=cas;LubricationType",
    description="Enumeration of possible lubrication types for the compression process of a compressor.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6373", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.LubricationTypeEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6362",
    browseName="ns=cas;NumberOfStages",
    description="Number of stages the compressor has available.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6374", browseName="Definition", dataType=o6.String))],
    dataType=o6.UInt16,
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=6363",
    browseName="ns=cas;VariableFlow",
    description="Indicates if a compressor has a variable or fixed flow.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6364",
                browseName="FalseState",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("'Fixed flow' means the product offers no control for changing the volume flow independent of pressure."),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6371",
                browseName="TrueState",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(
                    "‘Variable flow' means the compressor package allows an intentional change in volume flow rate, most obviously by VSD but also by adjustable guide vanes in turbo compressors or by valve controls in piston compressors or other means."
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6375", browseName="Definition", dataType=o6.String)),
    ],
    dataType=o6.Boolean,
    value=True,
)
cas_objtypes.CompressorDesignType(
    nodeId="ns=cas;i=5058",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=6052"]),
        o6.hasComponent(o6.ns["ns=cas;i=6340"]),
        o6.hasComponent(o6.ns["ns=cas;i=6341"]),
        o6.hasComponent(o6.ns["ns=cas;i=6362"]),
        o6.hasComponent(o6.ns["ns=cas;i=6363"]),
    ],
)
o6.reference(cas_objtypes.CompressorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5058"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6358",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6359", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6377", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6378", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6379", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6393", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6394", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6369",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6370", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6406", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6407", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6408", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6409", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6410", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6187",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6310", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6311", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6312", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6313", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6392", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6420", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6187"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6188",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6422", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6423", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6424", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6425", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6426", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6427", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6188"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6439",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[13],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Ammeter"), description=o6.LocalizedText("Ammeter")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("DewPointSensor"), description=o6.LocalizedText("Dew point sensor")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("FlowRateSensor"), description=o6.LocalizedText("Flow rate sensor")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("FlowSpeedSensor"), description=o6.LocalizedText("Flow speed sensor")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("HumiditySensor"), description=o6.LocalizedText("Humidity sensor")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("OilConcentrationSensor"), description=o6.LocalizedText("Oil concentration sensor")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ParticleCounter"), description=o6.LocalizedText("Particle counter")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("PressureSensor"), description=o6.LocalizedText("Pressure sensor")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("TemperatureSensor"), description=o6.LocalizedText("Temperature sensor")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Voltmeter"), description=o6.LocalizedText("Voltmeter")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("VolumeSensor"), description=o6.LocalizedText("Volume sensor")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Wattmeter"), description=o6.LocalizedText("Wattmeter")),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6440",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6114", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6115", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6140", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6141", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6142", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6149", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.ElectricalQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6440"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6441",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DryReceiver"), description=o6.LocalizedText("Dry Receiver")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("WetReceiver"), description=o6.LocalizedText("Wet Receiver")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=cas;i=6445", browseName="ns=cas;FilterClassDataType", dataType=o6.String, value="FilterClassDataType")
o6.reference(o6.ns["ns=cas;i=5042"], "i=39", o6.ns["ns=cas;i=6445"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=cas;i=6446", browseName="ns=cas;FilterClassDataType", dataType=o6.String, value="//xs:element[@name='FilterClassDataType']")
o6.reference(o6.ns["ns=cas;i=5043"], "i=39", o6.ns["ns=cas;i=6446"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6447",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ActivatedCarbonFilter"), description=o6.LocalizedText("Activated carbon filter")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("AdsorptionFilter"), description=o6.LocalizedText("Adsorption filter")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CoalescingFilter"), description=o6.LocalizedText("Coalescing filter")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ParticulateFilter"), description=o6.LocalizedText("Particulate filter")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("FabricFilter"), description=o6.LocalizedText("Fabric filter")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("SterileFilter"), description=o6.LocalizedText("Sterile filter")),
    ],
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=cas;i=6448",
    browseName="ns=cas;OperatingModes",
    description="Configured operating mode for an airnet in a compressed air system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6449",
                browseName="EnumStrings",
                description="Available operating modes for an airnet in a compressed air system.",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.LocalizedText("Stopped", "0")],
            )
        )
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
cas_objtypes.AirnetConfigurationType(
    nodeId="ns=cas;i=5049",
    browseName="ns=di;Configuration",
    description="Configure the behavior of the topology element.",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=6193"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6233", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.ns["ns=cas;i=6448"]),
    ],
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6088",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible receiver types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6469", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.ReceiverTypeEnum,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=6473",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6474", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6056",
    browseName="ns=cas;RunningTime",
    description="Time spent running since last counter reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6334", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6476", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6477", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6478", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6479", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6433",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6434", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6485", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6486", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6487", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6443",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6450", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6488", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6489", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6490", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6468",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6470", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6491", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6492", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6493", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=6494",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6495", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6496", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6481",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6482", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6497", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6498", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6499", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6483",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6484", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6500", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6501", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6502", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6189",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6428", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6429", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6507", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6508", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6513", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6514", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6189"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6194",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6515", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6516", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6517", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6518", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6519", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6520", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6194"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6346",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6347", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6510", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6511", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6512", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6523", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6524", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6195",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6521", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6522", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6529", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6530", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6531", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6532", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6195"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6351",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6352", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6525", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6526", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6527", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6528", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6534", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6159",
    browseName="ns=cas;<Quantity>",
    description="Manufacturer or system specific measurements or calculations.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6160", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6533", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6535", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6537", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6539", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6540", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=ns0.datatypes.Number,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6159"])
cas_objtypes.ConfigurationType(
    nodeId="ns=cas;i=5038",
    browseName="ns=di;Configuration",
    description="Configure the behavior of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6564", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        )
    ],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5038"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=6582",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6583", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
cas_objtypes.DesignType(
    nodeId="ns=cas;i=5010",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=6022"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6587", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5010"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6553",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6554", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6592", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6593", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6594", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6556",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6557", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6595", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6596", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6597", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6599",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible filter types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6600", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FilterTypeEnum,
)
o6.reference(cas_objtypes.FilterDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6599"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6589",
    browseName="ns=cas;FilterClass",
    description="Filter classes according to ISO 8573-1.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6601", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FilterClassDataType,
    value=cas_datypes.FilterClassDataType(a=cas_datypes.FilterClassEnum(0), b=cas_datypes.FilterClassEnum(0), c=cas_datypes.FilterClassEnum(0)),
)
o6.reference(cas_objtypes.FilterDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6589"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6603",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible receiver types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6604", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.ReceiverTypeEnum,
)
o6.reference(cas_objtypes.ReceiverDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6603"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6566",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6576", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6598", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6602", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6605", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=6606",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6607", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6608", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6586",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6588", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6609", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6610", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6611", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6614",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible sensor types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6617", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.SensorTypeEnum,
)
o6.reference(cas_objtypes.SensorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6614"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6615",
    browseName="ns=cas;SensorTechnology",
    description="Selection of sensor technologies this sensor uses.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6618", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.SensorTechnologyOptionSet,
)
o6.reference(cas_objtypes.SensorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6615"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6620",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible valve types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6622", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.ValveTypeEnum,
)
o6.reference(cas_objtypes.ValveDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6620"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6621",
    browseName="ns=cas;NumberOfPorts",
    description="Number of ports of a valve.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6623", browseName="Definition", dataType=o6.String))],
    dataType=o6.UInt16,
)
o6.reference(cas_objtypes.ValveDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6621"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6624",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible dryer types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6626", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.DryerTypeEnum,
)
o6.reference(cas_objtypes.DryerDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6624"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6625",
    browseName="ns=cas;LowestAmbientTemperature",
    description="Lowest allowable ambient temperature for the dryer to work as intended.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6627", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6628", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6631", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.DryerDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6625"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6590",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6591", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6612", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6613", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6633", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6632",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible condensate drain types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6636", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.DrainTypeEnum,
)
o6.reference(cas_objtypes.DrainDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6632"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6638",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible condensate separator types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6640", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.SeparatorTypeEnum,
)
o6.reference(cas_objtypes.SeparatorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6638"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6642",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible converter types.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6643", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.ConverterTypeEnum,
)
o6.reference(cas_objtypes.ConverterDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6642"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6644",
    browseName="ns=cas;ActivePressureBand",
    description="Indicates the actual active pressure band.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6645", browseName="Definition", dataType=o6.String))],
    dataType=o6.UInt16,
)
o6.reference(cas_objtypes.CompressorOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6644"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6183",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6280", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6304", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6305", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6306", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6650", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6652", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6066",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the part.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6653", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6654", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Enumeration,
)
o6.reference(cas_objtypes.OperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6066"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6223",
    browseName="ns=cas;HealthState",
    description="Actual health state of the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6658", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6676", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetHealthStateEnum,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6019",
    browseName="ns=cas;CompressorsIsolated",
    description="Number of isolated compressors in the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6105", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6128", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6663", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6683", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6019"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6366",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6367", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6664", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6665", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6685", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6686", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6687", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6294",
    browseName="ns=cas;NextCalibrationDate",
    description="Date when the sensor is scheduled for the next calibration.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6688", browseName="Definition", dataType=o6.String))],
    dataType=o6.DateTime,
)
cas_objtypes.CalibrationType(
    nodeId="ns=cas;i=5002",
    browseName="ns=cas;Calibration",
    description="Dates important for the calibration of a sensor.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6293"]), o6.hasComponent(o6.ns["ns=cas;i=6294"])],
)
o6.reference(cas_objtypes.SensorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5002"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6089",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible sensor types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6689", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.SensorTypeEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6690",
    browseName="ns=cas;SensorTechnology",
    description="Selection of sensor technologies this sensor uses.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6692", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.SensorTechnologyOptionSet,
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=cas;i=5017",
    browseName="ns=di;Identification",
    description="Identification properties of the topology element.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6285",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6286",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6298",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6299",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6300", browseName="ns=di;DeviceClass", description="Domain or for what purpose this item is used.", dataType=o6.String, value="MCS"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6301",
                browseName="ns=di;DeviceRevision",
                description="A string representation of the overall revision level of the component. Often, it is increased when either the SoftwareRevision and / or the HardwareRevision of the component is increased. As an example, it can be used in ERP systems together with the ProductCode.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6302",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6303",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6634", browseName="ns=di;ManufacturerUri", description="A globally unique identifier of the manufacturer of the MachineryItem.", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6647", browseName="ns=di;Model", description="A human-readable, localized name of the model of the MachineryItem.", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6649",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6660",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6694",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6702",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6717",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6713", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
o6.reference(cas_objtypes.MCSType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5017"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6715",
    browseName="ns=cas;LastCalibrationDate",
    description="Date when the sensor was last calibrated.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6718", browseName="Definition", dataType=o6.String))],
    dataType=o6.DateTime,
)
o6.reference(cas_objtypes.CalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6715"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6716",
    browseName="ns=cas;NextCalibrationDate",
    description="Date when the sensor is scheduled for the next calibration.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6719", browseName="Definition", dataType=o6.String))],
    dataType=o6.DateTime,
)
o6.reference(cas_objtypes.CalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6716"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=6739",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6740", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6726",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6727", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6747", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6748", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6749", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6729",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6730", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6750", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6751", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6752", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6735",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6736", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6753", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6754", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6755", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=6756",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6757", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6758", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6743",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6744", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6759", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6760", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6761", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6745",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6746", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6762", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6763", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6764", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6349",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6350", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6768", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6772", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6773", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6774", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6775", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6354",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6355", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6776", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6777", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6778", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6779", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6780", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6801",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6802", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6803",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6804", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6814",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6411", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6412", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6413", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6414", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6415", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6815", browseName="Id", dataType=o6.Boolean)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6818",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6403", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6404", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6405", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6819", browseName="Id", dataType=o6.Boolean)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6824",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6825", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6829",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6830", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6831",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6832", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6843",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6503", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6504", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6505", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6844", browseName="Id", dataType=o6.Boolean)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6849",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6850", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6854",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6855", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6856",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6857", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6867",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6703", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6704", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6705", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6709", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6710", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6868", browseName="Id", dataType=o6.Boolean)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6871",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6637", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6639", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6641", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6872", browseName="Id", dataType=o6.Boolean)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6877",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6878", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6882",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6883", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6884",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6885", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6896",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6765", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6766", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6767", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6897", browseName="Id", dataType=o6.Boolean)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6902",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6903", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6912",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6913", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6914",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6915", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6925",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6926", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6935",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6936", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6939",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6940", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6956",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6957", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6966",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6967", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=6970",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6971", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashCASSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=cas;i=5150",
    browseName="ns=cas;http://opcfoundation.org/UA/CAS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6979", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6980", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-07-13T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6981", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CAS/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6982", browseName="NamespaceVersion", dataType=o6.String, value="1.00.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6983", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6984", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6985", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="\n      ")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=6986",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6987", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6786",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6787", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6994", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6995", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6996", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6789",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6790", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6997", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6998", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6999", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6421",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7001", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6421"]))
o6.reference(o6.ns["ns=cas;i=7001"], "i=3065", "i=8961")

o6.call(nodeId="ns=cas;i=7002", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=7002"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7003", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=7003"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7004", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=7004"], "i=3065", "i=15013")

o6.call(nodeId="ns=cas;i=7005", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=7005"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6475",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=7006", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6475"]))
o6.reference(o6.ns["ns=cas;i=7006"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6873",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7013", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6873"]))
o6.reference(o6.ns["ns=cas;i=7013"], "i=3065", "i=8944")

o6.call(nodeId="ns=cas;i=7014", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=7014"], "i=3065", "i=11093")

ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5075",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6480", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=6473"]),
        o6.hasComponent(o6.ns["ns=cas;i=6494"]),
        o6.hasComponent(o6.ns["ns=cas;i=7005"]),
        o6.hasComponent(o6.ns["ns=cas;i=7006"]),
        o6.hasComponent(o6.ns["ns=cas;i=7014"]),
    ],
)


o6.call(nodeId="ns=cas;i=7015", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=7015"], "i=3065", "i=17242")

o6.call(nodeId="ns=cas;i=7016", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=7016"], "i=3065", "i=17225")

o6.call(nodeId="ns=cas;i=7017", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=7017"], "i=3065", "i=17225")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6552",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7018", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6552"]))
o6.reference(o6.ns["ns=cas;i=7018"], "i=3065", "i=8961")

o6.call(nodeId="ns=cas;i=7019", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=7019"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7020", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=7020"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7021", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=7021"], "i=3065", "i=15013")

o6.call(nodeId="ns=cas;i=7022", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=7022"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6584",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=7023", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6584"]))
o6.reference(o6.ns["ns=cas;i=7023"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7024", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=7024"], "i=3065", "i=11093")

ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5077",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6585", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=6582"]),
        o6.hasComponent(o6.ns["ns=cas;i=6606"]),
        o6.hasComponent(o6.ns["ns=cas;i=7022"]),
        o6.hasComponent(o6.ns["ns=cas;i=7023"]),
        o6.hasComponent(o6.ns["ns=cas;i=7024"]),
    ],
)


o6.call(nodeId="ns=cas;i=7025", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=7025"], "i=3065", "i=17242")

o6.call(nodeId="ns=cas;i=7026", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=7026"], "i=3065", "i=17225")

o6.call(nodeId="ns=cas;i=7027", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=7027"], "i=3065", "i=17225")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6725",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7028", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6725"]))
o6.reference(o6.ns["ns=cas;i=7028"], "i=3065", "i=8961")

o6.call(nodeId="ns=cas;i=7029", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=7029"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7030", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=7030"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7031", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=7031"], "i=3065", "i=15013")

o6.call(nodeId="ns=cas;i=7032", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=7032"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6741",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=7033", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6741"]))
o6.reference(o6.ns["ns=cas;i=7033"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7034", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=7034"], "i=3065", "i=11093")

ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5079",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6742", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=6739"]),
        o6.hasComponent(o6.ns["ns=cas;i=6756"]),
        o6.hasComponent(o6.ns["ns=cas;i=7032"]),
        o6.hasComponent(o6.ns["ns=cas;i=7033"]),
        o6.hasComponent(o6.ns["ns=cas;i=7034"]),
    ],
)


o6.call(nodeId="ns=cas;i=7035", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=7035"], "i=3065", "i=17242")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6288",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7036", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6288"]))
o6.reference(o6.ns["ns=cas;i=7036"], "i=3065", "i=2829")

o6.call(nodeId="ns=cas;i=7037", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7037"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7038", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7038"], "i=3065", "i=2803")

ns0.objtypes.ConditionType(
    nodeId="ns=cas;i=5080",
    browseName="ns=cas;<Event>",
    description="Manufacturer or system specific conditions.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6289", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6290", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6343", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6344", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6357", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6395", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6400", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6402", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6805", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6806", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6807", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6808", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6809", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6810", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6811", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6812", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6813", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=cas;i=6291"]),
        o6.hasComponent(o6.ns["ns=cas;i=6358"]),
        o6.hasComponent(o6.ns["ns=cas;i=6801"]),
        o6.hasComponent(o6.ns["ns=cas;i=6803"]),
        o6.hasComponent(o6.ns["ns=cas;i=7036"]),
        o6.hasComponent(o6.ns["ns=cas;i=7037"]),
        o6.hasComponent(o6.ns["ns=cas;i=7038"]),
    ],
    _allow_abstract=True,
)
o6.reference(cas_objtypes.EventsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5080"])


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6820",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7039", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6820"]))
o6.reference(o6.ns["ns=cas;i=7039"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6821",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7040", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6821"]))
o6.reference(o6.ns["ns=cas;i=7040"], "i=3065", "i=2829")

o6.call(nodeId="ns=cas;i=7041", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7041"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7042", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7042"], "i=3065", "i=2803")

ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5082",
    browseName="ns=cas;EmergencyStop",
    description="Indicating an emergency stop of a component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6368", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6416", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6418", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6419", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6451", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6465", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6466", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6467", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6472", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6816", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6817", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6822", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6823", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6826", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6827", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6828", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6833", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6834", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6835", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6836", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6837", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6838", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6839", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6840", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6841", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5074", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5075"]),
        o6.hasComponent(o6.ns["ns=cas;i=6369"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=6417", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=6433"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6437", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=6443"]),
        o6.hasComponent(o6.ns["ns=cas;i=6468"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6471", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=6481"]),
        o6.hasComponent(o6.ns["ns=cas;i=6483"]),
        o6.hasComponent(o6.ns["ns=cas;i=6814"]),
        o6.hasComponent(o6.ns["ns=cas;i=6818"]),
        o6.hasComponent(o6.ns["ns=cas;i=6824"]),
        o6.hasComponent(o6.ns["ns=cas;i=6829"]),
        o6.hasComponent(o6.ns["ns=cas;i=6831"]),
        o6.hasComponent(o6.ns["ns=cas;i=7001"]),
        o6.hasComponent(o6.ns["ns=cas;i=7002"]),
        o6.hasComponent(o6.ns["ns=cas;i=7003"]),
        o6.hasComponent(o6.ns["ns=cas;i=7004"]),
        o6.hasComponent(o6.ns["ns=cas;i=7015"]),
        o6.hasComponent(o6.ns["ns=cas;i=7016"]),
        o6.hasComponent(o6.ns["ns=cas;i=7017"]),
        o6.hasComponent(o6.ns["ns=cas;i=7039"]),
        o6.hasComponent(o6.ns["ns=cas;i=7040"]),
        o6.hasComponent(o6.ns["ns=cas;i=7041"]),
        o6.hasComponent(o6.ns["ns=cas;i=7042"]),
    ],
)
o6.reference(cas_objtypes.EventsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5082"])


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6845",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7043", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6845"]))
o6.reference(o6.ns["ns=cas;i=7043"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6846",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7044", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6846"]))
o6.reference(o6.ns["ns=cas;i=7044"], "i=3065", "i=2829")

o6.call(nodeId="ns=cas;i=7045", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7045"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7046", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7046"], "i=3065", "i=2803")

ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5083",
    browseName="ns=cas;Service",
    description="Indicates that a component requires service.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6345", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6353", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6536", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6550", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6551", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6558", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6559", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6561", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6562", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6581", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6842", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6847", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6848", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6851", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6852", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6853", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6858", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6859", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6860", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6861", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6862", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6863", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6864", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6865", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6866", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5076", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5077"]),
        o6.hasComponent(o6.ns["ns=cas;i=6346"]),
        o6.hasComponent(o6.ns["ns=cas;i=6351"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=6538", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=6553"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6555", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=6556"]),
        o6.hasComponent(o6.ns["ns=cas;i=6566"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6580", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=6586"]),
        o6.hasComponent(o6.ns["ns=cas;i=6590"]),
        o6.hasComponent(o6.ns["ns=cas;i=6843"]),
        o6.hasComponent(o6.ns["ns=cas;i=6849"]),
        o6.hasComponent(o6.ns["ns=cas;i=6854"]),
        o6.hasComponent(o6.ns["ns=cas;i=6856"]),
        o6.hasComponent(o6.ns["ns=cas;i=7018"]),
        o6.hasComponent(o6.ns["ns=cas;i=7019"]),
        o6.hasComponent(o6.ns["ns=cas;i=7020"]),
        o6.hasComponent(o6.ns["ns=cas;i=7021"]),
        o6.hasComponent(o6.ns["ns=cas;i=7025"]),
        o6.hasComponent(o6.ns["ns=cas;i=7026"]),
        o6.hasComponent(o6.ns["ns=cas;i=7027"]),
        o6.hasComponent(o6.ns["ns=cas;i=7043"]),
        o6.hasComponent(o6.ns["ns=cas;i=7044"]),
        o6.hasComponent(o6.ns["ns=cas;i=7045"]),
        o6.hasComponent(o6.ns["ns=cas;i=7046"]),
    ],
)
o6.reference(cas_objtypes.EventsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5083"])


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6874",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7047", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6874"]))
o6.reference(o6.ns["ns=cas;i=7047"], "i=3065", "i=2829")

o6.call(nodeId="ns=cas;i=7048", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7048"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7049", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7049"], "i=3065", "i=2803")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6898",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7050", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6898"]))
o6.reference(o6.ns["ns=cas;i=7050"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6899",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7051", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6899"]))
o6.reference(o6.ns["ns=cas;i=7051"], "i=3065", "i=2829")

o6.call(nodeId="ns=cas;i=7054", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7054"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7056", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7056"], "i=3065", "i=2803")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6059",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7060",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7060", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6059"]))
o6.reference(o6.ns["ns=cas;i=7060"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6216",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7065",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7065", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6216"]))
o6.reference(o6.ns["ns=cas;i=7065"], "i=3065", "i=2829")

o6.call(nodeId="ns=cas;i=7066", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7066"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7067", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7067"], "i=3065", "i=2803")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6950",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7068",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7068", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6950"]))
o6.reference(o6.ns["ns=cas;i=7068"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6953",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7069",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7069", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6953"]))
o6.reference(o6.ns["ns=cas;i=7069"], "i=3065", "i=2829")

o6.call(nodeId="ns=cas;i=7070", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7070"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7071", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7071"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7072", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=7072"], "i=3065", "i=17225")

o6.call(nodeId="ns=cas;i=7073", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=7073"], "i=3065", "i=17225")

ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5084",
    browseName="ns=cas;Shutdown",
    description="Indicating a shutdown of a component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6365", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6711", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6723", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6724", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6731", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6732", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6733", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6734", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6738", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6869", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6870", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6875", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6876", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6879", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6880", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6881", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6886", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6887", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6888", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6889", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6890", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6891", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6892", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6893", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6894", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5078", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5079"]),
        o6.hasComponent(o6.ns["ns=cas;i=6366"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=6721", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=6726"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6728", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=6729"]),
        o6.hasComponent(o6.ns["ns=cas;i=6735"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6737", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=6743"]),
        o6.hasComponent(o6.ns["ns=cas;i=6745"]),
        o6.hasComponent(o6.ns["ns=cas;i=6867"]),
        o6.hasComponent(o6.ns["ns=cas;i=6871"]),
        o6.hasComponent(o6.ns["ns=cas;i=6877"]),
        o6.hasComponent(o6.ns["ns=cas;i=6882"]),
        o6.hasComponent(o6.ns["ns=cas;i=6884"]),
        o6.hasComponent(o6.ns["ns=cas;i=7013"]),
        o6.hasComponent(o6.ns["ns=cas;i=7028"]),
        o6.hasComponent(o6.ns["ns=cas;i=7029"]),
        o6.hasComponent(o6.ns["ns=cas;i=7030"]),
        o6.hasComponent(o6.ns["ns=cas;i=7031"]),
        o6.hasComponent(o6.ns["ns=cas;i=7035"]),
        o6.hasComponent(o6.ns["ns=cas;i=7047"]),
        o6.hasComponent(o6.ns["ns=cas;i=7048"]),
        o6.hasComponent(o6.ns["ns=cas;i=7049"]),
        o6.hasComponent(o6.ns["ns=cas;i=7072"]),
        o6.hasComponent(o6.ns["ns=cas;i=7073"]),
    ],
)
o6.reference(cas_objtypes.EventsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5084"])


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6785",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7074",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7074", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6785"]))
o6.reference(o6.ns["ns=cas;i=7074"], "i=3065", "i=8961")

o6.call(nodeId="ns=cas;i=7075", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=7075"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7076", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=7076"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7077", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=7077"], "i=3065", "i=15013")

o6.call(nodeId="ns=cas;i=7078", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=7078"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6988",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7079",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=7079", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6988"]))
o6.reference(o6.ns["ns=cas;i=7079"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7080", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=7080"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7081", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=7081"], "i=3065", "i=17242")

o6.call(nodeId="ns=cas;i=7082", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=7082"], "i=3065", "i=17225")

o6.call(nodeId="ns=cas;i=7083", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=7083"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6795",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6796", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7000", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7084", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7085", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=7086",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7087", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7088", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5089",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6989", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=6986"]),
        o6.hasComponent(o6.ns["ns=cas;i=7078"]),
        o6.hasComponent(o6.ns["ns=cas;i=7079"]),
        o6.hasComponent(o6.ns["ns=cas;i=7080"]),
        o6.hasComponent(o6.ns["ns=cas;i=7086"]),
    ],
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6990",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6991", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7089", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7090", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7091", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6992",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6993", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7092", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7093", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7094", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5085",
    browseName="ns=cas;Warning",
    description="Indicating a general warning of a component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6348", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6356", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6781", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6783", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6784", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6791", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6792", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6793", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6794", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6798", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6895", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6900", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6901", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6904", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6905", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6906", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6916", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6917", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6918", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6919", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6920", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6921", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6922", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6923", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6924", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5088", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5089"]),
        o6.hasComponent(o6.ns["ns=cas;i=6349"]),
        o6.hasComponent(o6.ns["ns=cas;i=6354"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=6782", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=6786"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6788", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=6789"]),
        o6.hasComponent(o6.ns["ns=cas;i=6795"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6797", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=6896"]),
        o6.hasComponent(o6.ns["ns=cas;i=6902"]),
        o6.hasComponent(o6.ns["ns=cas;i=6912"]),
        o6.hasComponent(o6.ns["ns=cas;i=6914"]),
        o6.hasComponent(o6.ns["ns=cas;i=6990"]),
        o6.hasComponent(o6.ns["ns=cas;i=6992"]),
        o6.hasComponent(o6.ns["ns=cas;i=7050"]),
        o6.hasComponent(o6.ns["ns=cas;i=7051"]),
        o6.hasComponent(o6.ns["ns=cas;i=7054"]),
        o6.hasComponent(o6.ns["ns=cas;i=7056"]),
        o6.hasComponent(o6.ns["ns=cas;i=7074"]),
        o6.hasComponent(o6.ns["ns=cas;i=7075"]),
        o6.hasComponent(o6.ns["ns=cas;i=7076"]),
        o6.hasComponent(o6.ns["ns=cas;i=7077"]),
        o6.hasComponent(o6.ns["ns=cas;i=7081"]),
        o6.hasComponent(o6.ns["ns=cas;i=7082"]),
        o6.hasComponent(o6.ns["ns=cas;i=7083"]),
    ],
)
o6.reference(cas_objtypes.EventsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5085"])


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7098",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7097",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7097", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7098"]))
o6.reference(o6.ns["ns=cas;i=7097"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7102",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7101",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7101", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7102"]))
o6.reference(o6.ns["ns=cas;i=7101"], "i=3065", "i=2829")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=7105",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7106", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7110", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7110"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7111", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7111"], "i=3065", "i=2803")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=7117",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7118", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=7121",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7122", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7133",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7132",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7132", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7133"]))
o6.reference(o6.ns["ns=cas;i=7132"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7137",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7136",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7136", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7137"]))
o6.reference(o6.ns["ns=cas;i=7136"], "i=3065", "i=2829")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=7140",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7141", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7145", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=7145"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=7146", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=7146"], "i=3065", "i=2803")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=7152",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7153", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=7156",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7157", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=6616",
    browseName="ns=cas;SoftSensor",
    description="Indicates if the sensor is a software or hardware sensor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=6619", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("This sensor is a hardware sensor."))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=6691", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("This sensor is a software sensor."))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7165", browseName="Definition", dataType=o6.String)),
    ],
    dataType=o6.Boolean,
)
o6.reference(cas_objtypes.SensorDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6616"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6565",
    browseName="ns=cas;LoadedTime",
    description="Time spent in loaded state since last counter reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6651", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6697", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6698", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6699", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7183", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6574",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7190", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7191", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7192", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7193", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7194", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7195", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6575",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7196", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7197", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7198", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7199", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7200", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7201", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6577",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7202", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7203", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7204", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7205", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7206", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7207", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6578",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7208", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7209", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7210", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7211", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7212", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7213", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6907",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6014", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7216", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7217", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7218", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7219", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7220", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6579",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7214", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7222", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7223", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7224", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7225", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7226", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6629",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7227", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7228", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7229", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7230", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7231", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7232", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6635",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7233", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7234", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7235", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7236", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7237", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7238", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6720",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7239", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7240", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7241", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7242", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7243", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7244", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6722",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7245", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7246", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7247", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7248", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7249", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7250", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6908",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7221", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7251", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7252", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7253", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7254", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7255", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6909",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7256", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7257", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7265", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7266", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7267", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6084",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible condensate separator types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7272", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.SeparatorTypeEnum,
)
cas_objtypes.SeparatorDesignType(
    nodeId="ns=cas;i=5048",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6084"])],
)
o6.reference(cas_objtypes.SeparatorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5048"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6910",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7268", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7269", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7270", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7271", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7273", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7274", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6911",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7275", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7276", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7289", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7290", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7291", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7292", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7009",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7293", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7294", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7295", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7296", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7321", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7322", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7012",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7323", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7324", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7325", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7326", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7327", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7328", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7052",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7329", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7331", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7332", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7333", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7334", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7053",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7335", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7336", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7344", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7345", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7346", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7347", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7357",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7356",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7356", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7357"]))
o6.reference(o6.ns["ns=cas;i=7356"], "i=3065", "i=8961")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7358",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7359", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7360", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7361", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7362", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7364",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7365", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7366", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7367", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7368", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7373",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7374", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7375", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7376", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7377", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7378", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=7378"], "i=3065", "i=17259")

ns0.vartypes.DataTypeDescriptionType(nodeId="ns=cas;i=7380", browseName="ns=cas;SensorTechnologyOptionSet", dataType=o6.String, value="SensorTechnologyOptionSet")
o6.reference(o6.ns["ns=cas;i=5175"], "i=39", o6.ns["ns=cas;i=7380"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=cas;i=6023",
    browseName="ns=cas;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/CAS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6024", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CAS/")),
        o6.hasComponent(o6.ns["ns=cas;i=6445"]),
        o6.hasComponent(o6.ns["ns=cas;i=7380"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/CAS/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/CAS/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="FilterClassDataType">\n  <opc:Documentation>information about the used filter class according to ISO 8573-1 of a filter</opc:Documentation>\n  <opc:Field TypeName="tns:FilterClassEnum" Name="A"/>\n  <opc:Field TypeName="tns:FilterClassEnum" Name="B"/>\n  <opc:Field TypeName="tns:FilterClassEnum" Name="C"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:OptionSet" Name="SensorTechnologyOptionSet">\n  <opc:Documentation>flags for the used sensor technologies for a sensor</opc:Documentation>\n  <opc:Field TypeName="opc:ByteString" Name="Value"/>\n  <opc:Field TypeName="opc:ByteString" Name="ValidBits"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="AirnetHealthStateEnum">\n  <opc:EnumeratedValue Name="OK" Value="0"/>\n  <opc:EnumeratedValue Name="Warning" Value="1"/>\n  <opc:EnumeratedValue Name="Error" Value="2"/>\n  <opc:EnumeratedValue Name="Critical" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AirnetIntegratedStateEnum">\n  <opc:EnumeratedValue Name="FullyIntegrated" Value="0"/>\n  <opc:EnumeratedValue Name="PartiallyIntegrated" Value="1"/>\n  <opc:EnumeratedValue Name="FullyIsolated" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AirnetOperatingStateEnum">\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="Stopped" Value="1"/>\n  <opc:EnumeratedValue Name="Starting" Value="2"/>\n  <opc:EnumeratedValue Name="Stopping" Value="3"/>\n  <opc:EnumeratedValue Name="Operational" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CompressorOperatingStateEnum">\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="Stopped" Value="1"/>\n  <opc:EnumeratedValue Name="Starting" Value="2"/>\n  <opc:EnumeratedValue Name="Stopping" Value="3"/>\n  <opc:EnumeratedValue Name="Unloaded" Value="4"/>\n  <opc:EnumeratedValue Name="Loading" Value="5"/>\n  <opc:EnumeratedValue Name="Unloading" Value="6"/>\n  <opc:EnumeratedValue Name="Loaded" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CompressorTypeEnum">\n  <opc:Documentation>possible compressor types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="AxialTurboCompressor" Value="1"/>\n  <opc:EnumeratedValue Name="BellowsCompressor" Value="2"/>\n  <opc:EnumeratedValue Name="DiaphragmCompressor" Value="3"/>\n  <opc:EnumeratedValue Name="LiquidRingCompressor" Value="4"/>\n  <opc:EnumeratedValue Name="PistonCompressor" Value="5"/>\n  <opc:EnumeratedValue Name="RadialTurboCompressor" Value="6"/>\n  <opc:EnumeratedValue Name="RootsCompressor" Value="7"/>\n  <opc:EnumeratedValue Name="ScrewCompressor" Value="8"/>\n  <opc:EnumeratedValue Name="ScrollCompressor" Value="9"/>\n  <opc:EnumeratedValue Name="SideChannelCompressor" Value="10"/>\n  <opc:EnumeratedValue Name="StraightLobeCompressor" Value="11"/>\n  <opc:EnumeratedValue Name="VaneCompressor" Value="12"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ConverterTypeEnum">\n  <opc:Documentation>possible converter types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="CatalyticHCConverter" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DisplacementTypeEnum">\n  <opc:Documentation>possible displacement types for a compressor</opc:Documentation>\n  <opc:EnumeratedValue Name="PositiveDisplacement" Value="0"/>\n  <opc:EnumeratedValue Name="DynamicDisplacement" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DrainTypeEnum">\n  <opc:Documentation>possible condensate drain types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="CapacitiveDrain" Value="1"/>\n  <opc:EnumeratedValue Name="LevelControlledDrain" Value="2"/>\n  <opc:EnumeratedValue Name="TimedDrain" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DryerOperatingStateEnum">\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="Stopped" Value="1"/>\n  <opc:EnumeratedValue Name="Running" Value="2"/>\n  <opc:EnumeratedValue Name="RefrigerantCompressorStopped" Value="3"/>\n  <opc:EnumeratedValue Name="RefrigerantCompressorRunning" Value="4"/>\n  <opc:EnumeratedValue Name="PurgeValveClosed" Value="5"/>\n  <opc:EnumeratedValue Name="PurgeValveOpen" Value="6"/>\n  <opc:EnumeratedValue Name="ParallelModeOfBothVessels" Value="7"/>\n  <opc:EnumeratedValue Name="Depressurizing" Value="8"/>\n  <opc:EnumeratedValue Name="Desorbing" Value="9"/>\n  <opc:EnumeratedValue Name="Cooling" Value="10"/>\n  <opc:EnumeratedValue Name="Pressurizing" Value="11"/>\n  <opc:EnumeratedValue Name="RegeneratedVesselInStand-by" Value="12"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DryerTypeEnum">\n  <opc:Documentation>possible dryer types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="AbsorptionDryer" Value="1"/>\n  <opc:EnumeratedValue Name="AdsorptionDryer" Value="2"/>\n  <opc:EnumeratedValue Name="MembraneDryer" Value="3"/>\n  <opc:EnumeratedValue Name="RefrigerationDryer" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FilterClassEnum">\n  <opc:Documentation>possible filter classes according to ISO 8573-1</opc:Documentation>\n  <opc:EnumeratedValue Name="0" Value="0"/>\n  <opc:EnumeratedValue Name="1" Value="1"/>\n  <opc:EnumeratedValue Name="2" Value="2"/>\n  <opc:EnumeratedValue Name="3" Value="3"/>\n  <opc:EnumeratedValue Name="4" Value="4"/>\n  <opc:EnumeratedValue Name="5" Value="5"/>\n  <opc:EnumeratedValue Name="6" Value="6"/>\n  <opc:EnumeratedValue Name="7" Value="7"/>\n  <opc:EnumeratedValue Name="8" Value="8"/>\n  <opc:EnumeratedValue Name="9" Value="9"/>\n  <opc:EnumeratedValue Name="X" Value="10"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FilterTypeEnum">\n  <opc:Documentation>possible filter types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="ActivatedCarbonFilter" Value="1"/>\n  <opc:EnumeratedValue Name="AdsorptionFilter" Value="2"/>\n  <opc:EnumeratedValue Name="CoalescingFilter" Value="3"/>\n  <opc:EnumeratedValue Name="ParticulateFilter" Value="4"/>\n  <opc:EnumeratedValue Name="FabricFilter" Value="5"/>\n  <opc:EnumeratedValue Name="SterileFilter" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FluidTypeEnum">\n  <opc:Documentation>possible process fluid types</opc:Documentation>\n  <opc:EnumeratedValue Name="Air" Value="0"/>\n  <opc:EnumeratedValue Name="Condensate" Value="1"/>\n  <opc:EnumeratedValue Name="Oil" Value="2"/>\n  <opc:EnumeratedValue Name="Water" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="HealthStateEnum">\n  <opc:EnumeratedValue Name="OK" Value="0"/>\n  <opc:EnumeratedValue Name="Warning" Value="1"/>\n  <opc:EnumeratedValue Name="Error" Value="2"/>\n  <opc:EnumeratedValue Name="Critical" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="IntegratedStateEnum">\n  <opc:EnumeratedValue Name="FullyIntegrated" Value="0"/>\n  <opc:EnumeratedValue Name="PartiallyIntegrated" Value="1"/>\n  <opc:EnumeratedValue Name="FullyIsolated" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="IpVersionEnum">\n  <opc:EnumeratedValue Name="IPv4" Value="0"/>\n  <opc:EnumeratedValue Name="IPv6" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="LubricationTypeEnum">\n  <opc:Documentation>possible lubrication types for the compression process of a compressor</opc:Documentation>\n  <opc:EnumeratedValue Name="NoLubrication" Value="0"/>\n  <opc:EnumeratedValue Name="OilLubricated" Value="1"/>\n  <opc:EnumeratedValue Name="WaterLubricated" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="OperatingStateEnum">\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="Stopped" Value="1"/>\n  <opc:EnumeratedValue Name="Starting" Value="2"/>\n  <opc:EnumeratedValue Name="Stopping" Value="3"/>\n  <opc:EnumeratedValue Name="Operational" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ReceiverTypeEnum">\n  <opc:Documentation>possible receiver types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="DryReceiver" Value="1"/>\n  <opc:EnumeratedValue Name="WetReceiver" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SensorTypeEnum">\n  <opc:Documentation>possible sensor types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="Ammeter" Value="1"/>\n  <opc:EnumeratedValue Name="DewPointSensor" Value="2"/>\n  <opc:EnumeratedValue Name="FlowRateSensor" Value="3"/>\n  <opc:EnumeratedValue Name="FlowSpeedSensor" Value="4"/>\n  <opc:EnumeratedValue Name="HumiditySensor" Value="5"/>\n  <opc:EnumeratedValue Name="OilConcentrationSensor" Value="6"/>\n  <opc:EnumeratedValue Name="ParticleCounter" Value="7"/>\n  <opc:EnumeratedValue Name="PressureSensor" Value="8"/>\n  <opc:EnumeratedValue Name="TemperatureSensor" Value="9"/>\n  <opc:EnumeratedValue Name="Voltmeter" Value="10"/>\n  <opc:EnumeratedValue Name="VolumeSensor" Value="11"/>\n  <opc:EnumeratedValue Name="Wattmeter" Value="12"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SeparatorTypeEnum">\n  <opc:Documentation>possible condensate separator types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="CentrifugalOilyWaterSeparator" Value="1"/>\n  <opc:EnumeratedValue Name="EmulsionSplittingSeparator" Value="2"/>\n  <opc:EnumeratedValue Name="FlotationSeparator" Value="3"/>\n  <opc:EnumeratedValue Name="GravityPlateSeparator" Value="4"/>\n  <opc:EnumeratedValue Name="HydrocycloneOilyWaterSeparator" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ValveTypeEnum">\n  <opc:Documentation>possible valve types</opc:Documentation>\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="CheckValve" Value="1"/>\n  <opc:EnumeratedValue Name="ContinuousValve" Value="2"/>\n  <opc:EnumeratedValue Name="FlowControlValve" Value="3"/>\n  <opc:EnumeratedValue Name="PressureValve" Value="4"/>\n  <opc:EnumeratedValue Name="SwitchingValve" Value="5"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=cas;i=7381", browseName="ns=cas;SensorTechnologyOptionSet", dataType=o6.String, value="//xs:element[@name='SensorTechnologyOptionSet']"
)
o6.reference(o6.ns["ns=cas;i=5176"], "i=39", o6.ns["ns=cas;i=7381"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=cas;i=6025",
    browseName="ns=cas;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/CAS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6026", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CAS/Types.xsd")),
        o6.hasComponent(o6.ns["ns=cas;i=6446"]),
        o6.hasComponent(o6.ns["ns=cas;i=7381"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/CAS/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/CAS/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AirnetHealthStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OK_0"/>\n   <xs:enumeration value="Warning_1"/>\n   <xs:enumeration value="Error_2"/>\n   <xs:enumeration value="Critical_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AirnetHealthStateEnum" name="AirnetHealthStateEnum"/>\n <xs:complexType name="ListOfAirnetHealthStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AirnetHealthStateEnum" name="AirnetHealthStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAirnetHealthStateEnum" name="ListOfAirnetHealthStateEnum" nillable="true"/>\n <xs:simpleType name="AirnetIntegratedStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="FullyIntegrated_0"/>\n   <xs:enumeration value="PartiallyIntegrated_1"/>\n   <xs:enumeration value="FullyIsolated_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AirnetIntegratedStateEnum" name="AirnetIntegratedStateEnum"/>\n <xs:complexType name="ListOfAirnetIntegratedStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AirnetIntegratedStateEnum" name="AirnetIntegratedStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAirnetIntegratedStateEnum" name="ListOfAirnetIntegratedStateEnum" nillable="true"/>\n <xs:simpleType name="AirnetOperatingStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="Stopped_1"/>\n   <xs:enumeration value="Starting_2"/>\n   <xs:enumeration value="Stopping_3"/>\n   <xs:enumeration value="Operational_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AirnetOperatingStateEnum" name="AirnetOperatingStateEnum"/>\n <xs:complexType name="ListOfAirnetOperatingStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AirnetOperatingStateEnum" name="AirnetOperatingStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAirnetOperatingStateEnum" name="ListOfAirnetOperatingStateEnum" nillable="true"/>\n <xs:simpleType name="CompressorOperatingStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="Stopped_1"/>\n   <xs:enumeration value="Starting_2"/>\n   <xs:enumeration value="Stopping_3"/>\n   <xs:enumeration value="Unloaded_4"/>\n   <xs:enumeration value="Loading_5"/>\n   <xs:enumeration value="Unloading_6"/>\n   <xs:enumeration value="Loaded_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CompressorOperatingStateEnum" name="CompressorOperatingStateEnum"/>\n <xs:complexType name="ListOfCompressorOperatingStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CompressorOperatingStateEnum" name="CompressorOperatingStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCompressorOperatingStateEnum" name="ListOfCompressorOperatingStateEnum" nillable="true"/>\n <xs:simpleType name="CompressorTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible compressor types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="AxialTurboCompressor_1"/>\n   <xs:enumeration value="BellowsCompressor_2"/>\n   <xs:enumeration value="DiaphragmCompressor_3"/>\n   <xs:enumeration value="LiquidRingCompressor_4"/>\n   <xs:enumeration value="PistonCompressor_5"/>\n   <xs:enumeration value="RadialTurboCompressor_6"/>\n   <xs:enumeration value="RootsCompressor_7"/>\n   <xs:enumeration value="ScrewCompressor_8"/>\n   <xs:enumeration value="ScrollCompressor_9"/>\n   <xs:enumeration value="SideChannelCompressor_10"/>\n   <xs:enumeration value="StraightLobeCompressor_11"/>\n   <xs:enumeration value="VaneCompressor_12"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CompressorTypeEnum" name="CompressorTypeEnum"/>\n <xs:complexType name="ListOfCompressorTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CompressorTypeEnum" name="CompressorTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCompressorTypeEnum" name="ListOfCompressorTypeEnum" nillable="true"/>\n <xs:simpleType name="ConverterTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible converter types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="CatalyticHCConverter_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ConverterTypeEnum" name="ConverterTypeEnum"/>\n <xs:complexType name="ListOfConverterTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConverterTypeEnum" name="ConverterTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConverterTypeEnum" name="ListOfConverterTypeEnum" nillable="true"/>\n <xs:simpleType name="DisplacementTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible displacement types for a compressor</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="PositiveDisplacement_0"/>\n   <xs:enumeration value="DynamicDisplacement_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DisplacementTypeEnum" name="DisplacementTypeEnum"/>\n <xs:complexType name="ListOfDisplacementTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DisplacementTypeEnum" name="DisplacementTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDisplacementTypeEnum" name="ListOfDisplacementTypeEnum" nillable="true"/>\n <xs:simpleType name="DrainTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible condensate drain types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="CapacitiveDrain_1"/>\n   <xs:enumeration value="LevelControlledDrain_2"/>\n   <xs:enumeration value="TimedDrain_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DrainTypeEnum" name="DrainTypeEnum"/>\n <xs:complexType name="ListOfDrainTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DrainTypeEnum" name="DrainTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDrainTypeEnum" name="ListOfDrainTypeEnum" nillable="true"/>\n <xs:simpleType name="DryerOperatingStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="Stopped_1"/>\n   <xs:enumeration value="Running_2"/>\n   <xs:enumeration value="RefrigerantCompressorStopped_3"/>\n   <xs:enumeration value="RefrigerantCompressorRunning_4"/>\n   <xs:enumeration value="PurgeValveClosed_5"/>\n   <xs:enumeration value="PurgeValveOpen_6"/>\n   <xs:enumeration value="ParallelModeOfBothVessels_7"/>\n   <xs:enumeration value="Depressurizing_8"/>\n   <xs:enumeration value="Desorbing_9"/>\n   <xs:enumeration value="Cooling_10"/>\n   <xs:enumeration value="Pressurizing_11"/>\n   <xs:enumeration value="RegeneratedVesselInStand-by_12"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DryerOperatingStateEnum" name="DryerOperatingStateEnum"/>\n <xs:complexType name="ListOfDryerOperatingStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DryerOperatingStateEnum" name="DryerOperatingStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDryerOperatingStateEnum" name="ListOfDryerOperatingStateEnum" nillable="true"/>\n <xs:simpleType name="DryerTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible dryer types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="AbsorptionDryer_1"/>\n   <xs:enumeration value="AdsorptionDryer_2"/>\n   <xs:enumeration value="MembraneDryer_3"/>\n   <xs:enumeration value="RefrigerationDryer_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DryerTypeEnum" name="DryerTypeEnum"/>\n <xs:complexType name="ListOfDryerTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DryerTypeEnum" name="DryerTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDryerTypeEnum" name="ListOfDryerTypeEnum" nillable="true"/>\n <xs:simpleType name="FilterClassEnum">\n  <xs:annotation>\n   <xs:documentation>possible filter classes according to ISO 8573-1</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="0_0"/>\n   <xs:enumeration value="1_1"/>\n   <xs:enumeration value="2_2"/>\n   <xs:enumeration value="3_3"/>\n   <xs:enumeration value="4_4"/>\n   <xs:enumeration value="5_5"/>\n   <xs:enumeration value="6_6"/>\n   <xs:enumeration value="7_7"/>\n   <xs:enumeration value="8_8"/>\n   <xs:enumeration value="9_9"/>\n   <xs:enumeration value="X_10"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FilterClassEnum" name="FilterClassEnum"/>\n <xs:complexType name="ListOfFilterClassEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FilterClassEnum" name="FilterClassEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFilterClassEnum" name="ListOfFilterClassEnum" nillable="true"/>\n <xs:simpleType name="FilterTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible filter types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="ActivatedCarbonFilter_1"/>\n   <xs:enumeration value="AdsorptionFilter_2"/>\n   <xs:enumeration value="CoalescingFilter_3"/>\n   <xs:enumeration value="ParticulateFilter_4"/>\n   <xs:enumeration value="FabricFilter_5"/>\n   <xs:enumeration value="SterileFilter_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FilterTypeEnum" name="FilterTypeEnum"/>\n <xs:complexType name="ListOfFilterTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FilterTypeEnum" name="FilterTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFilterTypeEnum" name="ListOfFilterTypeEnum" nillable="true"/>\n <xs:simpleType name="FluidTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible process fluid types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Air_0"/>\n   <xs:enumeration value="Condensate_1"/>\n   <xs:enumeration value="Oil_2"/>\n   <xs:enumeration value="Water_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FluidTypeEnum" name="FluidTypeEnum"/>\n <xs:complexType name="ListOfFluidTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FluidTypeEnum" name="FluidTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFluidTypeEnum" name="ListOfFluidTypeEnum" nillable="true"/>\n <xs:simpleType name="HealthStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OK_0"/>\n   <xs:enumeration value="Warning_1"/>\n   <xs:enumeration value="Error_2"/>\n   <xs:enumeration value="Critical_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:HealthStateEnum" name="HealthStateEnum"/>\n <xs:complexType name="ListOfHealthStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:HealthStateEnum" name="HealthStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfHealthStateEnum" name="ListOfHealthStateEnum" nillable="true"/>\n <xs:simpleType name="IntegratedStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="FullyIntegrated_0"/>\n   <xs:enumeration value="PartiallyIntegrated_1"/>\n   <xs:enumeration value="FullyIsolated_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:IntegratedStateEnum" name="IntegratedStateEnum"/>\n <xs:complexType name="ListOfIntegratedStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:IntegratedStateEnum" name="IntegratedStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfIntegratedStateEnum" name="ListOfIntegratedStateEnum" nillable="true"/>\n <xs:simpleType name="IpVersionEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="IPv4_0"/>\n   <xs:enumeration value="IPv6_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:IpVersionEnum" name="IpVersionEnum"/>\n <xs:complexType name="ListOfIpVersionEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:IpVersionEnum" name="IpVersionEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfIpVersionEnum" name="ListOfIpVersionEnum" nillable="true"/>\n <xs:simpleType name="LubricationTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible lubrication types for the compression process of a compressor</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NoLubrication_0"/>\n   <xs:enumeration value="OilLubricated_1"/>\n   <xs:enumeration value="WaterLubricated_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:LubricationTypeEnum" name="LubricationTypeEnum"/>\n <xs:complexType name="ListOfLubricationTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:LubricationTypeEnum" name="LubricationTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLubricationTypeEnum" name="ListOfLubricationTypeEnum" nillable="true"/>\n <xs:simpleType name="OperatingStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="Stopped_1"/>\n   <xs:enumeration value="Starting_2"/>\n   <xs:enumeration value="Stopping_3"/>\n   <xs:enumeration value="Operational_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:OperatingStateEnum" name="OperatingStateEnum"/>\n <xs:complexType name="ListOfOperatingStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OperatingStateEnum" name="OperatingStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOperatingStateEnum" name="ListOfOperatingStateEnum" nillable="true"/>\n <xs:simpleType name="ReceiverTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible receiver types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="DryReceiver_1"/>\n   <xs:enumeration value="WetReceiver_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ReceiverTypeEnum" name="ReceiverTypeEnum"/>\n <xs:complexType name="ListOfReceiverTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ReceiverTypeEnum" name="ReceiverTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfReceiverTypeEnum" name="ListOfReceiverTypeEnum" nillable="true"/>\n <xs:simpleType name="SensorTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible sensor types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="Ammeter_1"/>\n   <xs:enumeration value="DewPointSensor_2"/>\n   <xs:enumeration value="FlowRateSensor_3"/>\n   <xs:enumeration value="FlowSpeedSensor_4"/>\n   <xs:enumeration value="HumiditySensor_5"/>\n   <xs:enumeration value="OilConcentrationSensor_6"/>\n   <xs:enumeration value="ParticleCounter_7"/>\n   <xs:enumeration value="PressureSensor_8"/>\n   <xs:enumeration value="TemperatureSensor_9"/>\n   <xs:enumeration value="Voltmeter_10"/>\n   <xs:enumeration value="VolumeSensor_11"/>\n   <xs:enumeration value="Wattmeter_12"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SensorTypeEnum" name="SensorTypeEnum"/>\n <xs:complexType name="ListOfSensorTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SensorTypeEnum" name="SensorTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSensorTypeEnum" name="ListOfSensorTypeEnum" nillable="true"/>\n <xs:simpleType name="SeparatorTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible condensate separator types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="CentrifugalOilyWaterSeparator_1"/>\n   <xs:enumeration value="EmulsionSplittingSeparator_2"/>\n   <xs:enumeration value="FlotationSeparator_3"/>\n   <xs:enumeration value="GravityPlateSeparator_4"/>\n   <xs:enumeration value="HydrocycloneOilyWaterSeparator_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SeparatorTypeEnum" name="SeparatorTypeEnum"/>\n <xs:complexType name="ListOfSeparatorTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SeparatorTypeEnum" name="SeparatorTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSeparatorTypeEnum" name="ListOfSeparatorTypeEnum" nillable="true"/>\n <xs:simpleType name="ValveTypeEnum">\n  <xs:annotation>\n   <xs:documentation>possible valve types</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="CheckValve_1"/>\n   <xs:enumeration value="ContinuousValve_2"/>\n   <xs:enumeration value="FlowControlValve_3"/>\n   <xs:enumeration value="PressureValve_4"/>\n   <xs:enumeration value="SwitchingValve_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ValveTypeEnum" name="ValveTypeEnum"/>\n <xs:complexType name="ListOfValveTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ValveTypeEnum" name="ValveTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfValveTypeEnum" name="ListOfValveTypeEnum" nillable="true"/>\n <xs:complexType name="FilterClassDataType">\n  <xs:annotation>\n   <xs:documentation>information about the used filter class according to ISO 8573-1 of a filter</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:FilterClassEnum" name="A"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:FilterClassEnum" name="B"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:FilterClassEnum" name="C"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:FilterClassDataType" name="FilterClassDataType"/>\n <xs:complexType name="ListOfFilterClassDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FilterClassDataType" name="FilterClassDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFilterClassDataType" name="ListOfFilterClassDataType" nillable="true"/>\n <xs:complexType name="SensorTechnologyOptionSet">\n  <xs:annotation>\n   <xs:documentation>flags for the used sensor technologies for a sensor</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:OptionSet">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:SensorTechnologyOptionSet" name="SensorTechnologyOptionSet"/>\n <xs:complexType name="ListOfSensorTechnologyOptionSet">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SensorTechnologyOptionSet" name="SensorTechnologyOptionSet" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSensorTechnologyOptionSet" name="ListOfSensorTechnologyOptionSet" nillable="true"/>\n</xs:schema>\n',
)


o6.call(nodeId="ns=cas;i=7383", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=7383"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7384", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=7384"], "i=3065", "i=15013")

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=7385",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7386", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7389", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=7389"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7391",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7390",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=7390", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7391"]))
o6.reference(o6.ns["ns=cas;i=7390"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7392", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=7392"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7394", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=7394"], "i=3065", "i=17242")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7395",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7396", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7397", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7398", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7399", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7400", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=7400"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7401",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7402", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7403", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7404", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7405", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7406", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=7406"], "i=3065", "i=17225")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7412",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7411",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7411", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7412"]))
o6.reference(o6.ns["ns=cas;i=7411"], "i=3065", "i=8961")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7413",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7414", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7415", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7416", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7417", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7419",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7420", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7421", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7422", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7423", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7428",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7429", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7430", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7431", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7432", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7433", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=7433"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7436", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=7436"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7437", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=7437"], "i=3065", "i=15013")

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=7438",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7439", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7442", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=7442"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7444",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7443",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=7443", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7444"]))
o6.reference(o6.ns["ns=cas;i=7443"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7445", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=7445"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7447", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=7447"], "i=3065", "i=17242")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7448",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7449", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7450", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7451", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7452", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7453", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=7453"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7454",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7455", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7456", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7457", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7458", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7459", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=7459"], "i=3065", "i=17225")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7465",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7464",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7464", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7465"]))
o6.reference(o6.ns["ns=cas;i=7464"], "i=3065", "i=8961")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7466",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7467", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7468", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7469", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7470", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7472",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7473", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7474", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7475", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7476", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7481",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7482", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7483", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7484", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7485", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7486", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=7486"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7489", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=7489"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7490", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=7490"], "i=3065", "i=15013")

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=7491",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7492", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7495", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=7495"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7497",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7496",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=7496", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7497"]))
o6.reference(o6.ns["ns=cas;i=7496"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7498", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=7498"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7500", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=7500"], "i=3065", "i=17242")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7501",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7502", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7503", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7504", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7505", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7506", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=7506"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7507",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7508", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7509", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7510", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7511", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7512", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=7512"], "i=3065", "i=17225")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7518",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7517",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=7517", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7518"]))
o6.reference(o6.ns["ns=cas;i=7517"], "i=3065", "i=8961")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7519",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7520", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7521", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7522", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7523", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7525",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7526", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7527", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7528", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7529", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7534",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7535", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7536", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7537", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7538", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7539", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=7539"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7542", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=7542"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=7543", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=7543"], "i=3065", "i=15013")

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=7544",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7545", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7548", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=7548"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7550",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7549",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=7549", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7550"]))
o6.reference(o6.ns["ns=cas;i=7549"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7551", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=7551"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=7553", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=7553"], "i=3065", "i=17242")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7554",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7555", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7556", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7557", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7558", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7559", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=7559"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7560",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7561", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7562", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7563", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7564", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=7565", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=7565"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6057",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6058", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7566", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7567", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7568", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6069",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6070", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7569", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7570", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7571", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7572", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7573", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6930",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6931", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7574", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7575", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7576", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7577", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7578", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6001",
    browseName="ns=cas;RunningTimeToNextService",
    description="Running time left until the running time of the next service level is exceeded.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6003", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6004", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7580", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7581", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7582", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.StatisticsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6001"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6948",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6949", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7583", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7584", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7585", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6951",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6952", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7586", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7587", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7588", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7589", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7590", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=6961",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6962", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7591", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7592", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7593", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7594", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7595", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7095",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7096", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7596", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7597", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7598", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7099",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7100", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7599", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7600", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7601", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7602", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7603", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7112",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7113", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7604", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7605", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7606", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7607", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7608", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7130",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7131", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7609", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7610", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7611", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7134",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7135", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7612", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7613", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7614", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7615", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7616", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=7147",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7148", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7617", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7618", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7619", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7620", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7621", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=7387",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7388", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7622", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5098",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7393", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=7385"]),
        o6.hasComponent(o6.ns["ns=cas;i=7387"]),
        o6.hasComponent(o6.ns["ns=cas;i=7389"]),
        o6.hasComponent(o6.ns["ns=cas;i=7390"]),
        o6.hasComponent(o6.ns["ns=cas;i=7392"]),
    ],
)
ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5068",
    browseName="ns=cas;EmergencyStop",
    description="Indicating an emergency stop of a component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6314", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6315", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6927", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6928", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6929", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6932", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6933", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6934", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6937", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6938", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6941", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6942", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6943", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6944", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6945", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6946", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6947", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7352", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7354", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7355", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7369", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7370", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7371", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7372", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7382", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5097", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5098"]),
        o6.hasComponent(o6.ns["ns=cas;i=6057"]),
        o6.hasComponent(o6.ns["ns=cas;i=6069"]),
        o6.hasComponent(o6.ns["ns=cas;i=6925"]),
        o6.hasComponent(o6.ns["ns=cas;i=6930"]),
        o6.hasComponent(o6.ns["ns=cas;i=6935"]),
        o6.hasComponent(o6.ns["ns=cas;i=6939"]),
        o6.hasComponent(o6.ns["ns=cas;i=7060"]),
        o6.hasComponent(o6.ns["ns=cas;i=7065"]),
        o6.hasComponent(o6.ns["ns=cas;i=7066"]),
        o6.hasComponent(o6.ns["ns=cas;i=7067"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=7353", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=7356"]),
        o6.hasComponent(o6.ns["ns=cas;i=7358"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=7363", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=7364"]),
        o6.hasComponent(o6.ns["ns=cas;i=7373"]),
        o6.hasComponent(o6.ns["ns=cas;i=7378"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=7379", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=7383"]),
        o6.hasComponent(o6.ns["ns=cas;i=7384"]),
        o6.hasComponent(o6.ns["ns=cas;i=7394"]),
        o6.hasComponent(o6.ns["ns=cas;i=7395"]),
        o6.hasComponent(o6.ns["ns=cas;i=7400"]),
        o6.hasComponent(o6.ns["ns=cas;i=7401"]),
        o6.hasComponent(o6.ns["ns=cas;i=7406"]),
    ],
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=7440",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7441", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7623", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5100",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7446", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=7438"]),
        o6.hasComponent(o6.ns["ns=cas;i=7440"]),
        o6.hasComponent(o6.ns["ns=cas;i=7442"]),
        o6.hasComponent(o6.ns["ns=cas;i=7443"]),
        o6.hasComponent(o6.ns["ns=cas;i=7445"]),
    ],
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=7493",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7494", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7624", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5102",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7499", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=7491"]),
        o6.hasComponent(o6.ns["ns=cas;i=7493"]),
        o6.hasComponent(o6.ns["ns=cas;i=7495"]),
        o6.hasComponent(o6.ns["ns=cas;i=7496"]),
        o6.hasComponent(o6.ns["ns=cas;i=7498"]),
    ],
)
ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5087",
    browseName="ns=cas;Shutdown",
    description="Indicating a shutdown of a component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7103", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7104", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7107", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7108", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7109", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7114", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7115", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7116", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7119", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7120", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7123", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7124", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7125", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7126", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7127", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7128", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7129", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7460", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7462", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7463", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7477", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7478", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7479", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7480", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7488", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5101", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5102"]),
        o6.hasComponent(o6.ns["ns=cas;i=7095"]),
        o6.hasComponent(o6.ns["ns=cas;i=7097"]),
        o6.hasComponent(o6.ns["ns=cas;i=7099"]),
        o6.hasComponent(o6.ns["ns=cas;i=7101"]),
        o6.hasComponent(o6.ns["ns=cas;i=7105"]),
        o6.hasComponent(o6.ns["ns=cas;i=7110"]),
        o6.hasComponent(o6.ns["ns=cas;i=7111"]),
        o6.hasComponent(o6.ns["ns=cas;i=7112"]),
        o6.hasComponent(o6.ns["ns=cas;i=7117"]),
        o6.hasComponent(o6.ns["ns=cas;i=7121"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=7461", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=7464"]),
        o6.hasComponent(o6.ns["ns=cas;i=7466"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=7471", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=7472"]),
        o6.hasComponent(o6.ns["ns=cas;i=7481"]),
        o6.hasComponent(o6.ns["ns=cas;i=7486"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=7487", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=7489"]),
        o6.hasComponent(o6.ns["ns=cas;i=7490"]),
        o6.hasComponent(o6.ns["ns=cas;i=7500"]),
        o6.hasComponent(o6.ns["ns=cas;i=7501"]),
        o6.hasComponent(o6.ns["ns=cas;i=7506"]),
        o6.hasComponent(o6.ns["ns=cas;i=7507"]),
        o6.hasComponent(o6.ns["ns=cas;i=7512"]),
    ],
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=7546",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7547", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7625", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5104",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7552", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=7544"]),
        o6.hasComponent(o6.ns["ns=cas;i=7546"]),
        o6.hasComponent(o6.ns["ns=cas;i=7548"]),
        o6.hasComponent(o6.ns["ns=cas;i=7549"]),
        o6.hasComponent(o6.ns["ns=cas;i=7551"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7055",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7348", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7349", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7350", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7351", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7626", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7627", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7057",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7628", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7629", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7630", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7631", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7632", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7633", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7058",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7634", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7635", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7636", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7637", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7638", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7639", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7059",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7640", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7641", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7642", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7643", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7644", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7645", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7061",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7646", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7647", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7648", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7649", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7650", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7651", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6567",
    browseName="ns=cas;UnloadedTime",
    description="Time spent in unloaded state since last counter reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7184", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7185", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7662", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7663", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7664", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.CompressorStatisticsType(
    nodeId="ns=cas;i=5072",
    browseName="ns=di;Statistics",
    description="Data for statistics applications for the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6565"]), o6.hasComponent(o6.ns["ns=cas;i=6567"])],
)
o6.reference(cas_objtypes.CompressorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5072"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7666",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AbsorptionDryer"), description=o6.LocalizedText("Absorption dryer")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("AdsorptionDryer"), description=o6.LocalizedText("Adsorption dryer")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("MembraneDryer"), description=o6.LocalizedText("Membrane dryer")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("RefrigerationDryer"), description=o6.LocalizedText("Refrigeration dryer")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7667",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CheckValve"), description=o6.LocalizedText("Check valve")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ContinuousValve"), description=o6.LocalizedText("Continuous valve")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("FlowControlValve"), description=o6.LocalizedText("Flow control valve")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("PressureValve"), description=o6.LocalizedText("Pressure valve")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("SwitchingValve"), description=o6.LocalizedText("Switching valve")),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7166",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7652", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7653", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7665", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7668", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7669", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7670", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7169",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7671", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7672", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7673", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7675", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7676", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7677", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7170",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7678", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7679", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7681", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7683", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7684", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7685", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7171",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7686", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7687", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7688", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7689", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7690", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7691", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7172",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7692", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7693", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7694", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7695", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7696", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7697", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7173",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7745", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7746", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7747", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7748", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7749", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7750", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7174",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7751", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7752", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7753", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7754", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7761", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7762", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7175",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7763", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7764", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7765", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7766", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7767", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7768", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7680",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7735", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7736", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7737", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7738", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7772", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7773", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7176",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7770", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7776", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7777", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7778", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7779", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7780", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7177",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7781", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7782", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7783", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7784", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7785", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7786", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7791",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6015", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6016", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6118", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6119", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6120", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6169", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=7791"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7682",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7774", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7775", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7787", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7788", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7792", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7794", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7187",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7789", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7790", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7795", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7796", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7797", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7798", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7188",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7799", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7800", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7801", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7802", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7803", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7804", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7189",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7805", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7806", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7807", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7808", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7809", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7810", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5060",
    browseName="ns=cas;<Other>",
    description="Placeholder for manufacturer or system specific groups.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6179",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=6174"]),
        o6.hasComponent(o6.ns["ns=cas;i=6175"]),
        o6.hasComponent(o6.ns["ns=cas;i=6176"]),
        o6.hasComponent(o6.ns["ns=cas;i=6177"]),
        o6.hasComponent(o6.ns["ns=cas;i=6183"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7815", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
    ],
)
o6.reference(cas_objtypes.ElectricalCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5060"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6661",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7843", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7844", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7845", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7846", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7847", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7848", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6662",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7849", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7850", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7851", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7852", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7853", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7854", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6672",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7855", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7856", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7857", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7858", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7859", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=cas;i=5081",
    browseName="ns=di;Identification",
    description="Identification properties of the topology element.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6287",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6297",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7659",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7871",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7872", browseName="ns=di;DeviceClass", description="Domain or for what purpose this item is used.", dataType=o6.String, value="MCS"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7873",
                browseName="ns=di;DeviceRevision",
                description="A string representation of the overall revision level of the component. Often, it is increased when either the SoftwareRevision and / or the HardwareRevision of the component is increased. As an example, it can be used in ERP systems together with the ProductCode.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7874",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7875",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7876", browseName="ns=di;ManufacturerUri", description="A globally unique identifier of the manufacturer of the MachineryItem.", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7877", browseName="ns=di;Model", description="A human-readable, localized name of the model of the MachineryItem.", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7878",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7879",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7880",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7881",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7883",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=7882", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
o6.reference(o6.ns["ns=cas;i=5081"], "i=47", o6.ns["ns=cas;i=6295"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=cas;i=5005",
    browseName="ns=di;Identification",
    description="Identification properties of the topology element.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6047",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6133",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6381",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6382",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=6383", browseName="ns=di;DeviceClass", description="Domain or for what purpose this item is used.", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6384",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6385",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6386", browseName="ns=di;ManufacturerUri", description="A globally unique identifier of the manufacturer of the MachineryItem.", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6387", browseName="ns=di;Model", description="A human-readable, localized name of the model of the MachineryItem.", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6388",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6389",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6390",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6391",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7885",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=7884", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
    _allow_abstract=True,
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5005"])
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=cas;i=5170",
    browseName="ns=di;Identification",
    description="Identification properties of the topology element.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6134",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6307",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6380",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=7886", browseName="ns=di;DeviceClass", description="Domain or for what purpose this item is used.", dataType=o6.String)
        ),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6673",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7860", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7861", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7862", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7863", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7892", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7893", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6680",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7894", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7895", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7896", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7897", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7898", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7899", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5108",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of electrical properties between inlet and outlet of the component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6674",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=6661"]),
        o6.hasComponent(o6.ns["ns=cas;i=6662"]),
        o6.hasComponent(o6.ns["ns=cas;i=6672"]),
        o6.hasComponent(o6.ns["ns=cas;i=6673"]),
        o6.hasComponent(o6.ns["ns=cas;i=6680"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7816", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
    ],
)
o6.reference(cas_objtypes.ElectricalCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5108"])


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7901",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7900",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7900", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7901"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7903",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7902",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7904",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7902",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7902", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7903"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=7904"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7906",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7905",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7907",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7905",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7905", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7906"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=7907"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7910",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7909",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7911",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7909",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7909", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7910"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=7911"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7913",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7912",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7912", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7913"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7918",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7917",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7917", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7918"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6250",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7920",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7920", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6250"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6251",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7922",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6360",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7922",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7922", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6251"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=6360"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6361",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7923",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7924",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7923",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7923", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6361"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=7924"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7927",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7926",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7928",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7926",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7926", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7927"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=7928"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7930",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7929",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7929", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7930"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7935",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7934",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7934", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7935"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7941",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7940",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7940", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=7941"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8233",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7942",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8234",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=7942",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=7942", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8233"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=8234"]))

ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7811",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7865", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7866", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7867", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7891", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7943", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7944", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7812",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7945", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7946", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7947", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7948", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7949", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7950", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7813",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7951", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7952", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7953", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7954", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7955", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7956", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=7960",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("PositiveDisplacement"), description=o6.LocalizedText("Positive displacement compressor")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DynamicDisplacement"), description=o6.LocalizedText("Dynamic displacement compressor")),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7864",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7957", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7958", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7959", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7961", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7962", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7963", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7734",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7887", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7888", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7889", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7964", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7965", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7966", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7967",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7971", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7972", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7973", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7974", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7975", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7976", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7968",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7977", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7979", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7985", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7986", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7987", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7988", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8001",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[11],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("0"), description=o6.LocalizedText("As specified by the equipment user or supplier and more stringent than class 1.")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("1"),
            description=o6.LocalizedText(
                "Particles: By Particle Size: 0.1 &#181;m &lt; d &#8804; 0.5 &#181;m: &#8804; 20,000; 0.5 &#181; m&lt; d &#8804; 1.0 &#181;m: &#8804; 400; 1.0 &#181;m &lt; d &#8804; 5.0 &#181;m: &#8804; 10;\nWater: Vapor Pressure Dewpoint: &#8804; -70 &#176;C, &#8804; -94 &#176;F;\nOil: Liquid, Aerosol, &amp; Vapor: &#8804; 0.01 mg/m3;",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("2"),
            description=o6.LocalizedText(
                "Particles: By Particle Size: 0.1 &#181;m &lt; d &#8804; 0.5 &#181;m: &#8804; 400,000; 0.5 &#181; m&lt; d &#8804; 1.0 &#181;m: &#8804; 6,000; 1.0 &#181;m &lt; d &#8804; 5.0 &#181;m: &#8804; 100;\nWater: Vapor Pressure Dewpoint: &#8804; -40 &#176;C, &#8804; -40 &#176;F;\nOil: Liquid, Aerosol, &amp; Vapor: &#8804; 0.1 mg/m3;",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("3"),
            description=o6.LocalizedText(
                "Particles: By Particle Size: 0.5 &#181; m&lt; d &#8804; 1.0 &#181;m: &#8804; 90,000; 1.0 &#181;m &lt; d &#8804; 5.0 &#181;m: &#8804; 1,000;\nWater: Vapor Pressure Dewpoint: &#8804; -20 &#176;C, &#8804; -4 &#176;F;\nOil: Liquid, Aerosol, &amp; Vapor: &#8804; 1 mg/m3;",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("4"),
            description=o6.LocalizedText(
                "Particles: By Particle Size: 1.0 &#181;m &lt; d &#8804; 5.0 &#181;m: &#8804; 10,000;\nWater: Vapor Pressure Dewpoint: &#8804; +3 &#176;C, &#8804; +37 &#176;F;\nOil: Liquid, Aerosol, &amp; Vapor: &#8804; 5 mg/m3;",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("5"),
            description=o6.LocalizedText(
                "Particles: By Particle Size: 1.0 &#181;m &lt; d &#8804; 5.0 &#181;m: &#8804; 100,000;\nWater: Vapor Pressure Dewpoint: &#8804; +7 &#176;C, &#8804; +45 &#176;F;",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("6"),
            description=o6.LocalizedText("Particles: By Mass: 0 &#8211; &#8804; 5 mg/m3;\nWater: Vapor Pressure Dewpoint: &#8804; +10 &#176;C, &#8804; +50 &#176;F;", ""),
        ),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("7"), description=o6.LocalizedText("Particles: By Mass: 5 &#8211; &#8804; 10 mg/m3;\nWater: Liquid: &#8804; 0.5 g/m3;", "")
        ),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("8"), description=o6.LocalizedText("Water: Liquid: &#8804; 5 g/m3;", "")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("9"), description=o6.LocalizedText("Water: Liquid: &#8804; 10 g/m3;", "")),
        ns0.datatypes.EnumValueType(
            value=10,
            displayName=o6.LocalizedText("X"),
            description=o6.LocalizedText("Particles: By Mass: &gt; 10 mg/m3;\nWater: Liquid: &gt; 10 g/m3;\nOil: Liquid, Aerosol, &amp; Vapor: &gt; 5 mg/m3;", ""),
        ),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7339",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7996", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7997", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7998", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7999", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8002", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8003", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7340",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8004", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8005", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8007", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8008", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8009", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7341",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8010", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8011", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8013", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8014", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8016", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7342",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8017", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8018", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8019", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8020", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8022", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8023", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7343",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8024", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8025", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8026", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8027", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8028", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8029", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6681",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8000", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8030", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8031", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8032", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8033", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8034", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6682",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8035", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8036", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8037", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8038", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8039", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8040", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7817",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8041", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8042", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8043", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8044", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8045", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7818",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8046", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8047", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8048", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8049", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8050", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8051", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6090",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible valve types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8057", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.ValveTypeEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6091",
    browseName="ns=cas;NumberOfPorts",
    description="Number of ports of a valve.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8058", browseName="Definition", dataType=o6.String))],
    dataType=o6.UInt16,
)
cas_objtypes.ValveDesignType(
    nodeId="ns=cas;i=5065",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6090"]), o6.hasComponent(o6.ns["ns=cas;i=6091"])],
)
o6.reference(cas_objtypes.ValveType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5065"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6087",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible filter types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8059", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FilterTypeEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=8060",
    browseName="ns=cas;FilterClass",
    description="Filter classes according to ISO 8573-1.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8061", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FilterClassDataType,
    value=cas_datypes.FilterClassDataType(a=cas_datypes.FilterClassEnum(0), b=cas_datypes.FilterClassEnum(0), c=cas_datypes.FilterClassEnum(0)),
)
cas_objtypes.FilterDesignType(
    nodeId="ns=cas;i=5061",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6087"]), o6.hasComponent(o6.ns["ns=cas;i=8060"])],
)
o6.reference(cas_objtypes.FilterType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5061"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6072",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible condensate drain types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8062", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.DrainTypeEnum,
)
cas_objtypes.DrainDesignType(
    nodeId="ns=cas;i=5039",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6072"])],
)
o6.reference(cas_objtypes.DrainType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5039"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6085",
    browseName="ns=cas;ComponentClass",
    description="Enumeration of possible converter types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8063", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.ConverterTypeEnum,
)
cas_objtypes.ConverterDesignType(
    nodeId="ns=cas;i=5054",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6085"])],
)
o6.reference(cas_objtypes.ConverterType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5054"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6203",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8070", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8071", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8073", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8074", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8075", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6204",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8076", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8077", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8078", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8079", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8080", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8081", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6213",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8082", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8083", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8084", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8085", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8086", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8087", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6214",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8088", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8089", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8090", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8091", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8092", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8093", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5032",
    browseName="ns=cas;Ambient",
    description="Measurements and calculations of ambient air at the topology element.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6203"]), o6.hasComponent(o6.ns["ns=cas;i=6204"]), o6.hasComponent(o6.ns["ns=cas;i=6213"]), o6.hasComponent(o6.ns["ns=cas;i=6214"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8102",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8101",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8101", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8102"]))
o6.reference(o6.ns["ns=cas;i=8101"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8106",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8105",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8105", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8106"]))
o6.reference(o6.ns["ns=cas;i=8105"], "i=3065", "i=2829")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8109",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8110", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8114", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=8114"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=8115", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=8115"], "i=3065", "i=2803")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8121",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8122", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8125",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8126", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6455",
    browseName="ns=cas;AirDeliveryRate",
    description="Volume of generated compressed air per time frame.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8151", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8152", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8153", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8154", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8155", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7969",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7989", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7995", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8157", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8158", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8159", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8160", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
cas_objtypes.DrainOperationalType(
    nodeId="ns=cas;i=5158",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.call(nodeId="ns=cas;i=8161", browseName="ns=cas;DrainTest", description="Invoke a drain test on a condensate drain."))],
)
o6.reference(cas_objtypes.DrainType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5158"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6456",
    browseName="ns=cas;CompressorsIntegrated",
    description="Number of integrated compressors in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8156", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8163", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8164", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8165", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8166", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7720",
    browseName="ns=cas;CompressorsIsolated",
    description="Number of isolated compressors in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8167", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8168", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8169", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8170", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8171", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6771",
    browseName="ns=cas;HealthState",
    description="Actual health state of the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8174", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8175", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetHealthStateEnum,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6771"])


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8179",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8178",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8178", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8179"]))
o6.reference(o6.ns["ns=cas;i=8178"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8183",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8182",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8182", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8183"]))
o6.reference(o6.ns["ns=cas;i=8182"], "i=3065", "i=2829")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8186",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8187", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8191", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=8191"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=8192", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=8192"], "i=3065", "i=2803")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8199",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8200", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8203",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8204", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=7186",
    browseName="ns=cas;IntegratedState",
    description="Actual integrated state of the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8212", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8213", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetIntegratedStateEnum,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=7186"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=8021",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8214", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8215", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetOperatingStateEnum,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=8021"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7821",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8052", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8053", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8054", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8055", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8056", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8218", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5109",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of electrical properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7820",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=6681"]),
        o6.hasComponent(o6.ns["ns=cas;i=6682"]),
        o6.hasComponent(o6.ns["ns=cas;i=7817"]),
        o6.hasComponent(o6.ns["ns=cas;i=7818"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7819", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7821"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7822",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8219", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8221", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8222", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8223", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8224", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6656",
    browseName="ns=cas;IntegratedState",
    description="Actual integrated state of the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8216", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8230", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetIntegratedStateEnum,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8237",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8235",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9756",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8235",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=8235", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8237"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9756"]))

ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=8217",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the compressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8232", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8236", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.CompressorOperatingStateEnum,
)
o6.reference(cas_objtypes.CompressorOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=8217"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7823",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8225", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8226", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8227", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8228", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8229", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8238", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7713",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8241", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8242", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8243", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8244", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8245", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8246", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8250",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8249",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8249", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8250"]))
o6.reference(o6.ns["ns=cas;i=8249"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8254",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8253",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8253", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8254"]))
o6.reference(o6.ns["ns=cas;i=8253"], "i=3065", "i=2829")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8257",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8258", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8262", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=8262"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=8263", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=8263"], "i=3065", "i=2803")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8269",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8270", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8273",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8274", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8283",
    browseName="ns=cas;ControlPressure",
    description="Current pressure in the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8285", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8286", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8287", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8288", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8289", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=8283"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8290",
    browseName="ns=cas;ControlPressure",
    description="Current pressure in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8292", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8293", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8294", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8295", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8296", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8301",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CatalyticHCConverter"), description=o6.LocalizedText("Catalytic hydrocarbons converter")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8302",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Air"), description=o6.LocalizedText("Air used as fluid")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Condensate"), description=o6.LocalizedText("Condensate used as fluid")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Oil"), description=o6.LocalizedText("Oil used as fluid")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Water"), description=o6.LocalizedText("Water used as fluid")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8303",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CapacitiveDrain"), description=o6.LocalizedText("Capacitive drain")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("LevelControlledDrain"), description=o6.LocalizedText("Level controlled drain")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("TimedDrain"), description=o6.LocalizedText("Timed drain")),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7970",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8196", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8291", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8304", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8305", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8307", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8308", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5051",
    browseName="ns=cas;Ambient",
    description="Measurements and calculations of ambient air at the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=7967"]), o6.hasComponent(o6.ns["ns=cas;i=7968"]), o6.hasComponent(o6.ns["ns=cas;i=7969"]), o6.hasComponent(o6.ns["ns=cas;i=7970"])],
)
o6.reference(cas_objtypes.AirnetType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5051"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7714",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8282", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8298", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8299", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8300", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8306", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8309", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7717",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8310", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8311", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8312", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8313", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8314", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8315", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8324",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8323",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8323", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8324"]))
o6.reference(o6.ns["ns=cas;i=8323"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8328",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8327",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8327", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8328"]))
o6.reference(o6.ns["ns=cas;i=8327"], "i=3065", "i=2829")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8331",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8332", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7718",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8316", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8317", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8318", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8319", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8320", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8335", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)


o6.call(nodeId="ns=cas;i=8337", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=8337"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=8339", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=8339"], "i=3065", "i=2803")

ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8345",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8346", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=8349",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8350", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7719",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8338", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8357", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8366", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8367", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8368", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8369", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7721",
    browseName="ns=cas;CompressorsNotAvailable",
    description="Number of unavailable compressors in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8172", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8173", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8370", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8371", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8372", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7722",
    browseName="ns=cas;ControlPressure",
    description="Current pressure in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8373", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8374", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8375", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8376", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8377", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=7723",
    browseName="ns=cas;HealthState",
    description="Actual health state of the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8378", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8379", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetHealthStateEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=7724",
    browseName="ns=cas;IntegratedState",
    description="Actual integrated state of the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8380", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8381", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetIntegratedStateEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=7725",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8382", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8383", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetOperatingStateEnum,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7726",
    browseName="ns=cas;SpecificEnergy",
    description="Electrical energy consumed in the generation of a volume of compressed air.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8384", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8385", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8386", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8387", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8388", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7727",
    browseName="ns=cas;SpecificEnergyCost",
    description="Costs for generating a volume of compressed air.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8389", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8396", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8397", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8398", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8399", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7744",
    browseName="ns=cas;VolumeFlowRateAvailable",
    description="Measured or calculated available volume flow rate of the process fluid in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8400", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8401", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8402", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8403", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8404", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7769",
    browseName="ns=cas;VolumeFlowRateUnavailable",
    description="Calculated unavailable volume flow rate of the process fluid in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8405", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8406", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8407", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8408", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8409", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.AirnetOperationalType(
    nodeId="ns=cas;i=5056",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=6455"]),
        o6.hasComponent(o6.ns["ns=cas;i=6456"]),
        o6.hasComponent(o6.ns["ns=cas;i=7720"]),
        o6.hasComponent(o6.ns["ns=cas;i=7721"]),
        o6.hasComponent(o6.ns["ns=cas;i=7722"]),
        o6.hasComponent(o6.ns["ns=cas;i=7723"]),
        o6.hasComponent(o6.ns["ns=cas;i=7724"]),
        o6.hasComponent(o6.ns["ns=cas;i=7725"]),
        o6.hasComponent(o6.ns["ns=cas;i=7726"]),
        o6.hasComponent(o6.ns["ns=cas;i=7727"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=7743", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7744"]),
        o6.hasComponent(o6.ns["ns=cas;i=7769"]),
    ],
)
ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5086",
    browseName="ns=cas;Service",
    description="Indicates that a component requires service.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6954", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6955", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6958", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6959", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6960", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6963", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6964", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6965", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6968", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6969", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6972", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6973", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6974", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6975", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6976", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6977", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6978", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7407", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7409", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7410", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7424", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7425", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7426", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7427", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7435", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5099", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5100"]),
        o6.hasComponent(o6.ns["ns=cas;i=6948"]),
        o6.hasComponent(o6.ns["ns=cas;i=6951"]),
        o6.hasComponent(o6.ns["ns=cas;i=6956"]),
        o6.hasComponent(o6.ns["ns=cas;i=6961"]),
        o6.hasComponent(o6.ns["ns=cas;i=6966"]),
        o6.hasComponent(o6.ns["ns=cas;i=6970"]),
        o6.hasComponent(o6.ns["ns=cas;i=7068"]),
        o6.hasComponent(o6.ns["ns=cas;i=7069"]),
        o6.hasComponent(o6.ns["ns=cas;i=7070"]),
        o6.hasComponent(o6.ns["ns=cas;i=7071"]),
        o6.hasComponent(o6.ns["ns=cas;i=7411"]),
        o6.hasComponent(o6.ns["ns=cas;i=7413"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=7418", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=7419"]),
        o6.hasComponent(o6.ns["ns=cas;i=7428"]),
        o6.hasComponent(o6.ns["ns=cas;i=7433"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=7434", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=7436"]),
        o6.hasComponent(o6.ns["ns=cas;i=7437"]),
        o6.hasComponent(o6.ns["ns=cas;i=7447"]),
        o6.hasComponent(o6.ns["ns=cas;i=7448"]),
        o6.hasComponent(o6.ns["ns=cas;i=7453"]),
        o6.hasComponent(o6.ns["ns=cas;i=7454"]),
        o6.hasComponent(o6.ns["ns=cas;i=7459"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=8420", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8424",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8423",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8423", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8424"]))
o6.reference(o6.ns["ns=cas;i=8423"], "i=3065", "i=8961")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8425",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8426", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8427", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8428", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8429", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8431",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8432", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8433", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8434", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8435", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8440",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8441", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8442", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8443", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8444", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8445", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=8445"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=8448", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=8448"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=8449", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=8449"], "i=3065", "i=15013")

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=8450",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8451", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8454", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=8454"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8456",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8455",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=8455", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8456"]))
o6.reference(o6.ns["ns=cas;i=8455"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=8457", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=8457"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=8459", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=8459"], "i=3065", "i=17242")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8460",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8461", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8462", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8463", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8464", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8465", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=8465"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8466",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8467", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8468", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8469", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8470", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8471", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=8471"], "i=3065", "i=17225")

ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=8297",
    browseName="ns=cas;FluidType",
    description="Enumeration of possible coolant types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8477", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FluidTypeEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=7771",
    browseName="ns=cas;FluidType",
    description="Enumeration of possible process fluid types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8481", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FluidTypeEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=8480",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the part.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8495", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8496", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Enumeration,
)
cas_objtypes.OperationalType(
    nodeId="ns=cas;i=5021",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=8480"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8492", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
o6.reference(cas_objtypes.MCSType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5021"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7824",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8239", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8497", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8498", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8499", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8500", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7825",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8501", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8502", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8503", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8504", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8505", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8506", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7828",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8507", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8508", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8509", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8510", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8511", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8512", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5127",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of electrical properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7827",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7822"]),
        o6.hasComponent(o6.ns["ns=cas;i=7823"]),
        o6.hasComponent(o6.ns["ns=cas;i=7824"]),
        o6.hasComponent(o6.ns["ns=cas;i=7825"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7826", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7828"]),
    ],
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=8493",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the part.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8515", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8516", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Enumeration,
)
cas_objtypes.OperationalType(
    nodeId="ns=cas;i=5704",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=8493"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8494", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5090",
    browseName="ns=cas;Warning",
    description="Indicating a general warning of a component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7138", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7139", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7142", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7143", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7144", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7149", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7150", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7151", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7154", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7155", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7158", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7159", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7160", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7161", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7162", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7163", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7164", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7513", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7515", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7516", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7530", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7531", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7532", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7533", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7541", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5103", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5104"]),
        o6.hasComponent(o6.ns["ns=cas;i=7130"]),
        o6.hasComponent(o6.ns["ns=cas;i=7132"]),
        o6.hasComponent(o6.ns["ns=cas;i=7134"]),
        o6.hasComponent(o6.ns["ns=cas;i=7136"]),
        o6.hasComponent(o6.ns["ns=cas;i=7140"]),
        o6.hasComponent(o6.ns["ns=cas;i=7145"]),
        o6.hasComponent(o6.ns["ns=cas;i=7146"]),
        o6.hasComponent(o6.ns["ns=cas;i=7147"]),
        o6.hasComponent(o6.ns["ns=cas;i=7152"]),
        o6.hasComponent(o6.ns["ns=cas;i=7156"]),
        o6.hasComponent(o6.ns["ns=cas;i=7517"]),
        o6.hasComponent(o6.ns["ns=cas;i=7519"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=7524", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=7525"]),
        o6.hasComponent(o6.ns["ns=cas;i=7534"]),
        o6.hasComponent(o6.ns["ns=cas;i=7539"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=7540", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=7542"]),
        o6.hasComponent(o6.ns["ns=cas;i=7543"]),
        o6.hasComponent(o6.ns["ns=cas;i=7553"]),
        o6.hasComponent(o6.ns["ns=cas;i=7554"]),
        o6.hasComponent(o6.ns["ns=cas;i=7559"]),
        o6.hasComponent(o6.ns["ns=cas;i=7560"]),
        o6.hasComponent(o6.ns["ns=cas;i=7565"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=8526", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8530",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8529",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8529", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8530"]))
o6.reference(o6.ns["ns=cas;i=8529"], "i=3065", "i=8961")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8531",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8532", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8533", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8534", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8535", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8537",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8541", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8542", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8543", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8544", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8549",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8550", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8551", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8552", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8553", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8554", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=8554"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=8557", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=8557"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=8558", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=8558"], "i=3065", "i=15013")

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=8559",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8560", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6010",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7303", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7304", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7305", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7306", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7307", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8563", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
o6.reference(cas_objtypes.ParticleType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6010"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6044",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7308", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7309", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7310", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7311", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7312", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8564", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)


o6.call(nodeId="ns=cas;i=8567", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=8567"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8569",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8568",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=8568", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8569"]))
o6.reference(o6.ns["ns=cas;i=8568"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=8570", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=8570"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=8572", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=8572"], "i=3065", "i=17242")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8573",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8574", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8575", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8576", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8577", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8578", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=8578"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8579",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8580", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8581", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8582", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8583", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8584", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=8584"], "i=3065", "i=17225")

ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8517",
    browseName="ns=cas;RealTime",
    description="Real time passed since last counter reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8586", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8587", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8588", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8589", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8590", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8520",
    browseName="ns=cas;RunningTime",
    description="Time spent running since last counter reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8591", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8592", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8593", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8594", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8595", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8099",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8100", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8598", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8599", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8600", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8103",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8104", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8601", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8602", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8603", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8604", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8605", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8116",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8117", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8606", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8607", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8608", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8609", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8610", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8523",
    browseName="ns=cas;RealTime",
    description="Real time passed since last counter reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8596", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8597", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8611", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8612", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8613", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8539",
    browseName="ns=cas;RunningTime",
    description="Time spent running since last counter reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8614", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8615", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8616", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8617", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8618", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8176",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8177", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8624", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8625", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8626", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8180",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8181", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8627", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8628", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8629", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8630", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8631", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8193",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8194", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8632", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8633", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8634", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8636", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8637", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=8452",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8453", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8639", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5152",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8458", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=8450"]),
        o6.hasComponent(o6.ns["ns=cas;i=8452"]),
        o6.hasComponent(o6.ns["ns=cas;i=8454"]),
        o6.hasComponent(o6.ns["ns=cas;i=8455"]),
        o6.hasComponent(o6.ns["ns=cas;i=8457"]),
    ],
)
ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5004",
    browseName="ns=cas;Service",
    description="Indicates that a component requires service.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8107", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8108", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8111", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8112", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8113", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8118", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8119", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8120", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8123", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8124", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8127", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8128", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8129", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8130", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8131", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8132", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8133", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8419", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8421", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8422", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8436", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8437", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8438", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8439", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8447", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5148", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5152"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=7408", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=8099"]),
        o6.hasComponent(o6.ns["ns=cas;i=8101"]),
        o6.hasComponent(o6.ns["ns=cas;i=8103"]),
        o6.hasComponent(o6.ns["ns=cas;i=8105"]),
        o6.hasComponent(o6.ns["ns=cas;i=8109"]),
        o6.hasComponent(o6.ns["ns=cas;i=8114"]),
        o6.hasComponent(o6.ns["ns=cas;i=8115"]),
        o6.hasComponent(o6.ns["ns=cas;i=8116"]),
        o6.hasComponent(o6.ns["ns=cas;i=8121"]),
        o6.hasComponent(o6.ns["ns=cas;i=8125"]),
        o6.hasComponent(o6.ns["ns=cas;i=8423"]),
        o6.hasComponent(o6.ns["ns=cas;i=8425"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=8430", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=8431"]),
        o6.hasComponent(o6.ns["ns=cas;i=8440"]),
        o6.hasComponent(o6.ns["ns=cas;i=8445"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=8446", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=8448"]),
        o6.hasComponent(o6.ns["ns=cas;i=8449"]),
        o6.hasComponent(o6.ns["ns=cas;i=8459"]),
        o6.hasComponent(o6.ns["ns=cas;i=8460"]),
        o6.hasComponent(o6.ns["ns=cas;i=8465"]),
        o6.hasComponent(o6.ns["ns=cas;i=8466"]),
        o6.hasComponent(o6.ns["ns=cas;i=8471"]),
    ],
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=8565",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8566", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8641", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5164",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8571", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=8559"]),
        o6.hasComponent(o6.ns["ns=cas;i=8565"]),
        o6.hasComponent(o6.ns["ns=cas;i=8567"]),
        o6.hasComponent(o6.ns["ns=cas;i=8568"]),
        o6.hasComponent(o6.ns["ns=cas;i=8570"]),
    ],
)
ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5131",
    browseName="ns=cas;Warning",
    description="Indicating a general warning of a component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8184", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8185", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8188", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8189", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8190", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8195", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8197", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8198", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8201", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8202", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8205", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8206", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8207", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8208", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8209", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8210", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8211", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8525", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8527", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8528", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8545", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8546", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8547", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8548", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8556", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5163", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5164"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=7514", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=8176"]),
        o6.hasComponent(o6.ns["ns=cas;i=8178"]),
        o6.hasComponent(o6.ns["ns=cas;i=8180"]),
        o6.hasComponent(o6.ns["ns=cas;i=8182"]),
        o6.hasComponent(o6.ns["ns=cas;i=8186"]),
        o6.hasComponent(o6.ns["ns=cas;i=8191"]),
        o6.hasComponent(o6.ns["ns=cas;i=8192"]),
        o6.hasComponent(o6.ns["ns=cas;i=8193"]),
        o6.hasComponent(o6.ns["ns=cas;i=8199"]),
        o6.hasComponent(o6.ns["ns=cas;i=8203"]),
        o6.hasComponent(o6.ns["ns=cas;i=8529"]),
        o6.hasComponent(o6.ns["ns=cas;i=8531"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=8536", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=8537"]),
        o6.hasComponent(o6.ns["ns=cas;i=8549"]),
        o6.hasComponent(o6.ns["ns=cas;i=8554"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=8555", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=8557"]),
        o6.hasComponent(o6.ns["ns=cas;i=8558"]),
        o6.hasComponent(o6.ns["ns=cas;i=8572"]),
        o6.hasComponent(o6.ns["ns=cas;i=8573"]),
        o6.hasComponent(o6.ns["ns=cas;i=8578"]),
        o6.hasComponent(o6.ns["ns=cas;i=8579"]),
        o6.hasComponent(o6.ns["ns=cas;i=8584"]),
    ],
)
cas_objtypes.EventsType(
    nodeId="ns=cas;i=5020",
    browseName="ns=cas;Events",
    description="Alarms and conditions of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5004"]),
        o6.hasComponent(o6.ns["ns=cas;i=5131"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8064", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
o6.reference(cas_objtypes.MCSType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5020"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8094",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8654", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8655", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8656", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8657", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8658", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8659", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8095",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8660", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8661", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8662", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8663", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8664", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8665", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8096",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8666", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8667", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8668", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8669", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8670", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8097",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8671", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8672", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8673", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8674", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8675", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8676", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8135",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8677", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8678", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8679", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8680", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8681", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8682", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5134",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of electrical properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8134",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8094"]),
        o6.hasComponent(o6.ns["ns=cas;i=8095"]),
        o6.hasComponent(o6.ns["ns=cas;i=8096"]),
        o6.hasComponent(o6.ns["ns=cas;i=8097"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8098", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8135"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8136",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8683", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8684", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8685", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8686", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8687", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8688", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8137",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8689", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8690", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8691", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8692", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8693", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8694", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8138",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8695", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8696", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8697", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8698", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8699", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8139",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8700", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8701", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8702", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8703", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8704", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8705", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6430",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7313", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7314", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7315", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7316", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7317", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8707", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6435",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7318", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7319", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7320", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7654", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7655", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8708", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6442",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7656", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7657", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7658", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7660", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7698", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8709", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6463",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7704", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7705", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7706", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7707", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7708", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8711", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6542",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7709", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7710", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7711", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7712", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7728", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8712", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8142",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8706", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8710", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8713", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8714", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8715", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8716", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5139",
    browseName="ns=cas;Input",
    description="Measured or calculated electrical properties at the input of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8141",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8136"]),
        o6.hasComponent(o6.ns["ns=cas;i=8137"]),
        o6.hasComponent(o6.ns["ns=cas;i=8138"]),
        o6.hasComponent(o6.ns["ns=cas;i=8139"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8140", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8142"]),
    ],
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8247",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8248", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8717", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8718", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8719", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8251",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8252", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8720", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8721", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8722", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8723", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8724", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8730",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8729",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8729", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8730"]))
o6.reference(o6.ns["ns=cas;i=8729"], "i=3065", "i=8961")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8731",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8732", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8733", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8734", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8735", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8264",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8265", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8736", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8737", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8738", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8739", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8740", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8742",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8743", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8744", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8745", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8746", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8751",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8752", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8753", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8754", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8755", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8756", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=8756"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=8759", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=8759"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=8760", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=8760"], "i=3065", "i=15013")

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=8761",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8762", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=8763",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8764", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8765", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8766", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=8766"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8768",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8767",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=8767", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8768"]))
o6.reference(o6.ns["ns=cas;i=8767"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=8769", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=8769"], "i=3065", "i=11093")

ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5168",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8770", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=8761"]),
        o6.hasComponent(o6.ns["ns=cas;i=8763"]),
        o6.hasComponent(o6.ns["ns=cas;i=8766"]),
        o6.hasComponent(o6.ns["ns=cas;i=8767"]),
        o6.hasComponent(o6.ns["ns=cas;i=8769"]),
    ],
)


o6.call(nodeId="ns=cas;i=8771", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=8771"], "i=3065", "i=17242")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8772",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8773", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8774", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8775", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8776", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8777", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=8777"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8778",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8779", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8780", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8781", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8782", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8783", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=8783"], "i=3065", "i=17225")

ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5136",
    browseName="ns=cas;Service",
    description="Indicates that a component requires service.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8255", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8256", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8259", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8260", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8261", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8266", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8267", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8268", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8271", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8272", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8275", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8276", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8277", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8278", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8279", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8280", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8281", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8725", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8727", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8728", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8747", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8748", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8749", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8750", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8758", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5167", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5168"]),
        o6.hasComponent(o6.ns["ns=cas;i=8247"]),
        o6.hasComponent(o6.ns["ns=cas;i=8249"]),
        o6.hasComponent(o6.ns["ns=cas;i=8251"]),
        o6.hasComponent(o6.ns["ns=cas;i=8253"]),
        o6.hasComponent(o6.ns["ns=cas;i=8257"]),
        o6.hasComponent(o6.ns["ns=cas;i=8262"]),
        o6.hasComponent(o6.ns["ns=cas;i=8263"]),
        o6.hasComponent(o6.ns["ns=cas;i=8264"]),
        o6.hasComponent(o6.ns["ns=cas;i=8269"]),
        o6.hasComponent(o6.ns["ns=cas;i=8273"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=8726", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=8729"]),
        o6.hasComponent(o6.ns["ns=cas;i=8731"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=8741", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=8742"]),
        o6.hasComponent(o6.ns["ns=cas;i=8751"]),
        o6.hasComponent(o6.ns["ns=cas;i=8756"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=8757", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=8759"]),
        o6.hasComponent(o6.ns["ns=cas;i=8760"]),
        o6.hasComponent(o6.ns["ns=cas;i=8771"]),
        o6.hasComponent(o6.ns["ns=cas;i=8772"]),
        o6.hasComponent(o6.ns["ns=cas;i=8777"]),
        o6.hasComponent(o6.ns["ns=cas;i=8778"]),
        o6.hasComponent(o6.ns["ns=cas;i=8783"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8143",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8784", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8785", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8786", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8787", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8788", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8789", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6549",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7729", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7730", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7731", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7732", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7733", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8791", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6568",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7739", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7740", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7741", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7742", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7755", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8793", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8144",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8790", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8792", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8794", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8795", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8796", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8797", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8798",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CentrifugalOilyWaterSeparator"), description=o6.LocalizedText("Centrifugal oily water separator")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("EmulsionSplittingSeparator"), description=o6.LocalizedText("Emulsion splitting separator")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("FlotationSeparator"), description=o6.LocalizedText("Flotation separator")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("GravityPlateSeparator"), description=o6.LocalizedText("Gravity plate separator")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("HydrocycloneOilyWaterSeparator"), description=o6.LocalizedText("Hydrocyclone oily water separator")),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6571",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7756", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7757", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7758", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7759", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7760", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8799", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7180",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7980", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7981", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7982", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7983", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7984", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8800", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7260",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7990", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7991", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7992", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7993", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7994", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8813", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7263",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8358", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8359", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8360", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8361", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8362", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8814", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7297",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8363", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8364", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8390", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8391", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8392", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8815", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7300",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8393", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8394", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8395", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8561", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8562", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8816", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6011",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8817", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8818", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8819", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8820", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8821", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8822", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
o6.reference(cas_objtypes.ParticleType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6011"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6045",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8823", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8824", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8825", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8826", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8827", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8829", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7829",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8513", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8514", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8833", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8834", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8835", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8836", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6431",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8830", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8831", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8832", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8842", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8843", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8852", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8321",
    browseName="AckedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8322", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8856", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unacknowledged", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8857", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8858", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Acknowledged", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8325",
    browseName="ActiveState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8326", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8859", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8860", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8861", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Inactive", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8862", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8863", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Active", "en"))),
    ],
    dataType=o6.LocalizedText,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8869",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8868",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=8868", browseName="Confirm", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8869"]))
o6.reference(o6.ns["ns=cas;i=8868"], "i=3065", "i=8961")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8870",
    browseName="ConfirmedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8871", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unconfirmed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8872", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8873", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8874", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Confirmed", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8340",
    browseName="EnabledState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8341", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8875", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8876", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8877", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Disabled", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8878", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8879", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Enabled", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8881",
    browseName="LatchedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8882", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unlatched", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8883", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8884", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8885", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Latched", "en"))),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8890",
    browseName="OutOfServiceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8891", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("In Service", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8892", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8893", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8894", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Out of Service", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8895", browseName="PlaceInService")
o6.reference(o6.ns["ns=cas;i=8895"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=8898", browseName="RemoveFromService")
o6.reference(o6.ns["ns=cas;i=8898"], "i=3065", "i=17259")

o6.call(nodeId="ns=cas;i=8899", browseName="Reset")
o6.reference(o6.ns["ns=cas;i=8899"], "i=3065", "i=15013")

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cas;i=8900",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8901", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=cas;i=8902",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8903", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8904", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8905", browseName="OneShotShelve")
o6.reference(o6.ns["ns=cas;i=8905"], "i=3065", "i=11093")

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=8907",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=8906",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ShelvingTime",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("If not 0, this parameter specifies a fixed time for which the Alarm is to be shelved."),
        )
    ],
)
o6.call(nodeId="ns=cas;i=8906", browseName="TimedShelve", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=8907"]))
o6.reference(o6.ns["ns=cas;i=8906"], "i=3065", "i=11093")

o6.call(nodeId="ns=cas;i=8908", browseName="Unshelve")
o6.reference(o6.ns["ns=cas;i=8908"], "i=3065", "i=11093")

ns0.objtypes.ShelvedStateMachineType(
    nodeId="ns=cas;i=5174",
    browseName="ShelvingState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8909", browseName="UnshelveTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=cas;i=8900"]),
        o6.hasComponent(o6.ns["ns=cas;i=8902"]),
        o6.hasComponent(o6.ns["ns=cas;i=8905"]),
        o6.hasComponent(o6.ns["ns=cas;i=8906"]),
        o6.hasComponent(o6.ns["ns=cas;i=8908"]),
    ],
)


o6.call(nodeId="ns=cas;i=8910", browseName="Silence")
o6.reference(o6.ns["ns=cas;i=8910"], "i=3065", "i=17242")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8911",
    browseName="SilenceState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8912", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Not Silenced", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8913", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8914", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8915", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Silenced", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8916", browseName="Suppress")
o6.reference(o6.ns["ns=cas;i=8916"], "i=3065", "i=17225")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=8917",
    browseName="SuppressedState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8918", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("Unsuppressed", "en"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8919", browseName="Id", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8920", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8921", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Suppressed", "en"))),
    ],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=8922", browseName="Unsuppress")
o6.reference(o6.ns["ns=cas;i=8922"], "i=3065", "i=17225")

ns0.objtypes.OffNormalAlarmType(
    nodeId="ns=cas;i=5144",
    browseName="ns=cas;Warning",
    description="Indicating a general warning of a component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8329", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8330", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8333", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8334", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8336", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8342", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8343", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8344", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8347", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8348", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8351", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8352", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8353", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8354", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8355", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8356", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8365", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8864", browseName="AudibleEnabled", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8866", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8867", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8886", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8887", browseName="MaxTimeShelved", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8888", browseName="OffDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8889", browseName="OnDelay", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8897", browseName="ReAlarmTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.objtypes.AlarmGroupType(nodeId="ns=cas;i=5173", browseName="FirstInGroup")),
        o6.hasComponent(o6.ns["ns=cas;i=5174"]),
        o6.hasComponent(o6.ns["ns=cas;i=8321"]),
        o6.hasComponent(o6.ns["ns=cas;i=8323"]),
        o6.hasComponent(o6.ns["ns=cas;i=8325"]),
        o6.hasComponent(o6.ns["ns=cas;i=8327"]),
        o6.hasComponent(o6.ns["ns=cas;i=8331"]),
        o6.hasComponent(o6.ns["ns=cas;i=8337"]),
        o6.hasComponent(o6.ns["ns=cas;i=8339"]),
        o6.hasComponent(o6.ns["ns=cas;i=8340"]),
        o6.hasComponent(o6.ns["ns=cas;i=8345"]),
        o6.hasComponent(o6.ns["ns=cas;i=8349"]),
        o6.hasComponent(ns0.vartypes.AudioVariableType(nodeId="ns=cas;i=8865", browseName="AudibleSound", dataType=ns0.datatypes.AudioDataType)),
        o6.hasComponent(o6.ns["ns=cas;i=8868"]),
        o6.hasComponent(o6.ns["ns=cas;i=8870"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=8880", browseName="FirstInGroupFlag", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=8881"]),
        o6.hasComponent(o6.ns["ns=cas;i=8890"]),
        o6.hasComponent(o6.ns["ns=cas;i=8895"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=8896", browseName="ReAlarmRepeatCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=cas;i=8898"]),
        o6.hasComponent(o6.ns["ns=cas;i=8899"]),
        o6.hasComponent(o6.ns["ns=cas;i=8910"]),
        o6.hasComponent(o6.ns["ns=cas;i=8911"]),
        o6.hasComponent(o6.ns["ns=cas;i=8916"]),
        o6.hasComponent(o6.ns["ns=cas;i=8917"]),
        o6.hasComponent(o6.ns["ns=cas;i=8922"]),
    ],
)
cas_objtypes.EventsType(
    nodeId="ns=cas;i=5700",
    browseName="ns=cas;Events",
    description="Alarms and conditions of the topology element.",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5136"]),
        o6.hasComponent(o6.ns["ns=cas;i=5144"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8065", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6436",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8853", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8854", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8855", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8923", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8924", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8925", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6444",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8926", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8927", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8928", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8929", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8930", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8931", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8145",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8801", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8932", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8933", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8938", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8939", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7062",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8950", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8951", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8952", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8953", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8954", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8955", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6464",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8942", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8943", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8958", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8959", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8960", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8961", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7063",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8956", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8957", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8964", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8965", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8966", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8967", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7064",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8968", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8969", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8970", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8971", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8972", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8973", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7215",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8974", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8975", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8976", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8977", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8978", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8979", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7258",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8980", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8981", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8982", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8983", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8984", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8985", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7259",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8986", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8987", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8988", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8989", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8990", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8991", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7279",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8992", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8993", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8994", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8995", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8996", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8997", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7282",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8998", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8999", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9000", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9001", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9002", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9003", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7283",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9004", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9005", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9007", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9008", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9009", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7284",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9010", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9011", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9013", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9014", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9015", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6543",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8962", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8963", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9016", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9017", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9018", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9019", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6560",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9020", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9022", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9023", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9024", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9025", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8146",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8940", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8941", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9026", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9027", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9028", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9029", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7285",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9031", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9032", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9033", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9034", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9035", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9036", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7286",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9037", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9038", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9039", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9040", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9041", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9042", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7287",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9043", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9044", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9045", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9046", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9047", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9048", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7830",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8837", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8838", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8839", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8840", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8841", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9059", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6569",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9054", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9055", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9056", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9057", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9058", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9063", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7288",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9049", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9050", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9051", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9052", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9068", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9069", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7337",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9070", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9071", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9072", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9073", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9074", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9076", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6572",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9064", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9065", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9066", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9067", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9075", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9078", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7338",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9077", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9079", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9080", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9081", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9082", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9085", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7181",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9083", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9084", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9086", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9087", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9088", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9089", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8150",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9030", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9053", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9090", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9091", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9092", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9093", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5147",
    browseName="ns=cas;Output",
    description="Measured or calculated electrical properties at the output of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8148",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8143"]),
        o6.hasComponent(o6.ns["ns=cas;i=8144"]),
        o6.hasComponent(o6.ns["ns=cas;i=8145"]),
        o6.hasComponent(o6.ns["ns=cas;i=8146"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8147", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8150"]),
    ],
)
cas_objtypes.ElectricalCircuitType(
    nodeId="ns=cas;i=5053",
    browseName="ns=cas;ElectricalCircuit",
    description="Measurements and calculations of the electrical ports and delta of the topology element.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5134"]), o6.hasComponent(o6.ns["ns=cas;i=5139"]), o6.hasComponent(o6.ns["ns=cas;i=5147"])],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7261",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9096", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9097", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9098", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9099", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9100", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9105", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8802",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9101", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9102", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9103", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9104", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9109", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9110", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8805",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9111", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9112", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9113", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9114", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9115", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9116", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8806",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9117", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9118", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9119", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9120", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9121", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9122", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8807",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9123", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9124", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9125", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9126", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9127", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9128", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8808",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9129", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9130", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9131", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9132", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9133", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9134", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7831",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9060", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9061", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9062", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9140", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9141", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8809",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9135", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9136", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9137", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9138", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9139", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9145", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8810",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9146", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9148", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9149", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9150", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9151", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9152", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8811",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9153", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9154", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9155", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9156", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9157", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9158", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8812",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9159", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9160", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9161", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9162", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9163", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9164", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8828",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9165", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9166", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9167", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9168", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9169", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9175", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7277",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9106", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9107", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9108", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9176", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9177", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9178", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7298",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9179", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9180", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9181", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9182", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9183", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9184", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7301",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9185", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9186", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9187", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9188", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9189", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9190", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8844",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9191", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9192", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9193", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9194", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9195", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9196", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8847",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9197", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9198", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9199", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9200", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9201", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9202", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7832",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9142", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9143", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9144", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9205", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9206", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9207", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8848",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9203", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9204", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9210", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9211", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9212", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9213", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8849",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9214", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9215", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9216", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9217", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9218", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9219", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8850",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9220", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9221", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9222", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9223", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9224", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9225", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8851",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9226", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9227", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9228", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9229", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9230", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9231", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8934",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9232", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9233", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9234", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9235", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9236", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9237", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6012",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9241", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9242", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9243", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9244", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9245", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9246", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.UInt64,
)
o6.reference(cas_objtypes.ParticleType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6012"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8935",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9238", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9239", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9240", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9247", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9248", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9249", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8936",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9250", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9251", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9252", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9253", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9254", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9255", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8937",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9256", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9257", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9258", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9259", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9260", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9261", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6046",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9262", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9263", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9265", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9266", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9267", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5007",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6044"]), o6.hasComponent(o6.ns["ns=cas;i=6045"]), o6.hasComponent(o6.ns["ns=cas;i=6046"])],
)
o6.reference(cas_objtypes.FluidQuantitiesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5007"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7835",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9208", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9209", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9270", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9271", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9272", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9273", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5142",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of electrical properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7834",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7829"]),
        o6.hasComponent(o6.ns["ns=cas;i=7830"]),
        o6.hasComponent(o6.ns["ns=cas;i=7831"]),
        o6.hasComponent(o6.ns["ns=cas;i=7832"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7833", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7835"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6432",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9268", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9269", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9275", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9276", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9277", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9278", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5041",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6430"]), o6.hasComponent(o6.ns["ns=cas;i=6431"]), o6.hasComponent(o6.ns["ns=cas;i=6432"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5034",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of fluid properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7011",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5041"]),
        o6.hasComponent(o6.ns["ns=cas;i=6907"]),
        o6.hasComponent(o6.ns["ns=cas;i=6908"]),
        o6.hasComponent(o6.ns["ns=cas;i=6909"]),
        o6.hasComponent(o6.ns["ns=cas;i=6910"]),
        o6.hasComponent(o6.ns["ns=cas;i=6911"]),
        o6.hasComponent(o6.ns["ns=cas;i=7009"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7010", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7012"]),
        o6.hasComponent(o6.ns["ns=cas;i=7052"]),
        o6.hasComponent(o6.ns["ns=cas;i=7053"]),
        o6.hasComponent(o6.ns["ns=cas;i=7812"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8944",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9282", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9283", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9284", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9285", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9286", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9287", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8947",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9288", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9289", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9290", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9291", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9292", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9293", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8948",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9294", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9295", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9296", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9297", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9298", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9299", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=9147",
    browseName="ns=cas;FluidType",
    description="Enumeration of possible process fluid types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9305", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FluidTypeEnum,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8949",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9300", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9301", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9302", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9303", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9304", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9306", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8240",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of the environment in which the component, piping or system is working.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7674", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9170", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9171", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9172", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9173", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9307", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5140",
    browseName="ns=cas;Ambient",
    description="Measurements and calculations of ambient air at the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=7680"]), o6.hasComponent(o6.ns["ns=cas;i=7682"]), o6.hasComponent(o6.ns["ns=cas;i=7734"]), o6.hasComponent(o6.ns["ns=cas;i=8240"])],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5140"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7836",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9274", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9335", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9336", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9337", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9338", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9339", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9308",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9361", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9362", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9363", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9364", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9365", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9366", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9309",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9367", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9368", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9369", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9370", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9371", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9372", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9310",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9373", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9374", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9375", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9376", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9377", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9378", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9311",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9379", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9380", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9381", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9382", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9383", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9384", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9312",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9385", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9386", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9387", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9388", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9389", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9390", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9313",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9391", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9392", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9393", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9394", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9395", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9396", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9314",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9397", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9398", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9399", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9405", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9406", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9407", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9317",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9408", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9409", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9410", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9411", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9412", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9413", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9318",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9414", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9415", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9416", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9417", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9418", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9419", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9319",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9420", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9421", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9422", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9423", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9424", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9425", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9320",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9426", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9427", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9428", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9429", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9430", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9431", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9321",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9432", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9433", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9434", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9435", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9436", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9437", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7837",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9400", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9401", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9402", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9403", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9404", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9441", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9322",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9438", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9439", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9440", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9443", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9444", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9445", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9323",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9446", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9447", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9448", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9449", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9450", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9451", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9324",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9452", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9453", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9454", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9455", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9456", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9457", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9325",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9458", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9459", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9460", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9461", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9462", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9463", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9326",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9464", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9465", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9466", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9467", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9468", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9469", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9329",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9470", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9471", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9472", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9473", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9474", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9475", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9330",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9476", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9477", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9478", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9479", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9480", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9481", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9331",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9482", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9483", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9484", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9485", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9486", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9487", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7838",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9442", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9491", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9492", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9493", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9494", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9332",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9488", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9489", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9490", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9496", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9497", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9498", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9333",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9499", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9500", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9501", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9502", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9503", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9504", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9334",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9505", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9506", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9507", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9508", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9509", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9510", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9340",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9511", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9512", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9513", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9514", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9515", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9516", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9341",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9517", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9518", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9519", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9520", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9521", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9522", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9342",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9523", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9524", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9525", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9526", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9527", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9528", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9343",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9529", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9530", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9531", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9532", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9533", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9534", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6438",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9279", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9280", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9281", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9535", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9536", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9537", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5045",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6435"]), o6.hasComponent(o6.ns["ns=cas;i=6436"]), o6.hasComponent(o6.ns["ns=cas;i=6438"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5217",
    browseName="ns=cas;Inlet",
    description="Measured or calculated fluid properties at the inlet of the component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7281",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5045"]),
        o6.hasComponent(o6.ns["ns=cas;i=7062"]),
        o6.hasComponent(o6.ns["ns=cas;i=7063"]),
        o6.hasComponent(o6.ns["ns=cas;i=7064"]),
        o6.hasComponent(o6.ns["ns=cas;i=7215"]),
        o6.hasComponent(o6.ns["ns=cas;i=7258"]),
        o6.hasComponent(o6.ns["ns=cas;i=7259"]),
        o6.hasComponent(o6.ns["ns=cas;i=7279"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7280", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7282"]),
        o6.hasComponent(o6.ns["ns=cas;i=7283"]),
        o6.hasComponent(o6.ns["ns=cas;i=7284"]),
    ],
)
o6.reference(cas_objtypes.FluidCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5217"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9346",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9541", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9542", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9543", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9544", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9545", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9546", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9347",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9547", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9548", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9549", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9550", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9551", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9552", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9348",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9553", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9554", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9555", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9556", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9557", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9558", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9349",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9559", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9560", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9561", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9562", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9563", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9564", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9350",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9565", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9566", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9567", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9568", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9569", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9570", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9351",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9571", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9572", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9573", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9574", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9575", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9576", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9352",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9577", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9578", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9579", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9580", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9581", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9582", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7839",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9495", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9584", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9585", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9586", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9587", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9588", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7842",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9589", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9590", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9591", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9592", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9593", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9594", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5155",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of electrical properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7841",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7836"]),
        o6.hasComponent(o6.ns["ns=cas;i=7837"]),
        o6.hasComponent(o6.ns["ns=cas;i=7838"]),
        o6.hasComponent(o6.ns["ns=cas;i=7839"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7840", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7842"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9595",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9630", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9631", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9632", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9633", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9634", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9635", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9596",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9636", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9637", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9638", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9639", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9640", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9641", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9597",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9642", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9643", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9644", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9645", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9646", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9598",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9647", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9648", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9649", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9650", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9651", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9652", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9601",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9653", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9654", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9655", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9656", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9657", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9658", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5066",
    browseName="ns=cas;Input",
    description="Measured or calculated electrical properties at the input of the component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9600",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9595"]),
        o6.hasComponent(o6.ns["ns=cas;i=9596"]),
        o6.hasComponent(o6.ns["ns=cas;i=9597"]),
        o6.hasComponent(o6.ns["ns=cas;i=9598"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9599", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9601"]),
    ],
)
o6.reference(cas_objtypes.ElectricalCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5066"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9602",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9659", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9660", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9661", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9662", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9663", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9664", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9603",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9665", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9666", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9667", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9668", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9669", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9670", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9604",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9671", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9672", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9673", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9674", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9675", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9605",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9676", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9677", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9678", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9679", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9680", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9681", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9608",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9682", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9683", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9684", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9685", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9686", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9689", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5052",
    browseName="ns=cas;Input",
    description="Measured or calculated electrical properties at the input of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9607",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9602"]),
        o6.hasComponent(o6.ns["ns=cas;i=9603"]),
        o6.hasComponent(o6.ns["ns=cas;i=9604"]),
        o6.hasComponent(o6.ns["ns=cas;i=9605"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9606", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9608"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9609",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9690", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9691", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9692", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9693", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9694", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9695", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9610",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9696", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9697", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9698", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9699", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9700", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9701", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9611",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9702", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9703", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9704", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9705", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9706", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9612",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9707", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9708", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9709", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9710", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9711", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9712", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9615",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9713", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9714", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9715", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9716", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9717", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9718", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5132",
    browseName="ns=cas;Input",
    description="Measured or calculated electrical properties at the input of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9614",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9609"]),
        o6.hasComponent(o6.ns["ns=cas;i=9610"]),
        o6.hasComponent(o6.ns["ns=cas;i=9611"]),
        o6.hasComponent(o6.ns["ns=cas;i=9612"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9613", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9615"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6453",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9538", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9539", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9540", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9720", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9721", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9722", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5046",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6442"]), o6.hasComponent(o6.ns["ns=cas;i=6444"]), o6.hasComponent(o6.ns["ns=cas;i=6453"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5040",
    browseName="ns=cas;Outlet",
    description="Measured or calculated fluid properties at the outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9328",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5046"]),
        o6.hasComponent(o6.ns["ns=cas;i=9320"]),
        o6.hasComponent(o6.ns["ns=cas;i=9321"]),
        o6.hasComponent(o6.ns["ns=cas;i=9322"]),
        o6.hasComponent(o6.ns["ns=cas;i=9323"]),
        o6.hasComponent(o6.ns["ns=cas;i=9324"]),
        o6.hasComponent(o6.ns["ns=cas;i=9325"]),
        o6.hasComponent(o6.ns["ns=cas;i=9326"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9327", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9329"]),
        o6.hasComponent(o6.ns["ns=cas;i=9330"]),
        o6.hasComponent(o6.ns["ns=cas;i=9331"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9353",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9583", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9687", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9688", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9719", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9729", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9730", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9616",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9724", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9725", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9726", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9727", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9728", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9734", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9354",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9731", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9732", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9733", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9739", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9740", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9741", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9617",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9735", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9736", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9737", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9738", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9744", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9745", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9355",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9742", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9743", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9749", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9750", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9751", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9752", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8410",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9094", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9095", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9174", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9723", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9754", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9755", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9759",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9758",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9760",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9758",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9758", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9759"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9760"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9762",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9761",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9761", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9762"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9767",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9766",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9766", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9767"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6323",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9768",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9768", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6323"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=6332",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9769",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9770",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9769",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9769", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=6332"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9770"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9772",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9771",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9773",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9771",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9771", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9772"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9773"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9776",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9775",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9777",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9775",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9775", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9776"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9777"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9779",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9778",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9778", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9779"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9784",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9783",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9783", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9784"]))

ns0.objtypes.FileType(
    nodeId="ns=cas;i=5025",
    browseName="ns=cas;ConfigurationFile",
    description="Configuration file for the MCS in a compressed air system.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6327", browseName="MimeType", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9774", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9780", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9781", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9782", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=9768"]),
        o6.hasComponent(o6.ns["ns=cas;i=9769"]),
        o6.hasComponent(o6.ns["ns=cas;i=9771"]),
        o6.hasComponent(o6.ns["ns=cas;i=9775"]),
        o6.hasComponent(o6.ns["ns=cas;i=9778"]),
        o6.hasComponent(o6.ns["ns=cas;i=9783"]),
    ],
)
o6.reference(cas_objtypes.MCSConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5025"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9788",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[13],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Not specified in this enumeration")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AxialTurboCompressor"), description=o6.LocalizedText("Axial Turbo compressor")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("BellowsCompressor"), description=o6.LocalizedText("Bellows compressor")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("DiaphragmCompressor"), description=o6.LocalizedText("Diaphragm compressor")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("LiquidRingCompressor"), description=o6.LocalizedText("Liquid ring compressor")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("PistonCompressor"), description=o6.LocalizedText("Piston compressor")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("RadialTurboCompressor"), description=o6.LocalizedText("Radial Turbo compressor")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("RootsCompressor"), description=o6.LocalizedText("Roots compressor")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ScrewCompressor"), description=o6.LocalizedText("Screw compressor")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("ScrollCompressor"), description=o6.LocalizedText("Scroll compressor")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("SideChannelCompressor"), description=o6.LocalizedText("Side channel compressor")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("StraightLobeCompressor"), description=o6.LocalizedText("Straight lobe compressor")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("VaneCompressor"), description=o6.LocalizedText("Vane compressor")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9789",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NoLubrication"), description=o6.LocalizedText("No lubrication")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("OilLubricated"), description=o6.LocalizedText("Oil lubricated")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("WaterLubricated"), description=o6.LocalizedText("Water lubricated")),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9618",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9746", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9747", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9748", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9790", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9791", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8411",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9786", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9787", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9792", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9793", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9794", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9795", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9619",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9796", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9801", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9802", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9803", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9804", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9805", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9622",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9806", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9807", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9808", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9809", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9810", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9811", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5143",
    browseName="ns=cas;Input",
    description="Measured or calculated electrical properties at the input of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9621",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9616"]),
        o6.hasComponent(o6.ns["ns=cas;i=9617"]),
        o6.hasComponent(o6.ns["ns=cas;i=9618"]),
        o6.hasComponent(o6.ns["ns=cas;i=9619"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9620", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9622"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9623",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9812", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9813", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9814", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9815", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9816", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9817", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=cas;i=5189",
    browseName="ns=di;Identification",
    description="Identification properties of the topology element.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7921",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7937",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7939",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9824", browseName="ns=di;DeviceClass", description="Domain or for what purpose this item is used.", dataType=o6.String, value="Compressor"
            )
        ),
    ],
)
o6.reference(cas_objtypes.CompressorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5189"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8412",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9797", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9798", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9799", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9800", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9825", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9826", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9834",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9833",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=cas;i=9833", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9834"]))
o6.reference(o6.ns["ns=cas;i=9833"], "i=3065", "i=2829")

ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8413",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9827", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9828", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9831", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9832", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9835", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9836", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8414",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9837", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9838", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9839", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9840", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9841", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9842", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8415",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9843", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9844", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9845", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9846", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9847", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9848", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8472",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9849", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9850", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9851", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9852", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9853", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9854", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8475",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9855", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9856", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9857", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9858", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9859", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9860", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8476",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9861", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9862", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9863", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9864", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9865", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9866", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9872",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9871",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9871", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9872"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9874",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9873",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9875",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9873",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9873", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9874"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9875"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9877",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9876",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9878",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9876",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9876", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9877"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9878"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9881",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9880",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9882",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9880",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9880", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9881"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9882"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9884",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9883",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9883", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9884"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9889",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9888",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9888", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9889"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9891",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9890",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9890", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9891"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9893",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9892",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9894",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9892",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9892", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9893"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9894"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9896",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9895",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9897",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9895",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9895", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9896"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9897"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9900",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9899",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9901",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9899",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9899", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9900"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9901"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9903",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9902",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9902", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9903"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9908",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9907",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9907", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9908"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9910",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9909",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9909", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9910"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9912",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9911",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9913",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9911",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9911", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9912"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9913"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9915",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9914",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9916",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9914",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9914", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9915"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9916"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9919",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9918",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9920",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9918",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9918", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9919"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9920"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9922",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9921",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9921", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9922"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9927",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9926",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9926", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9927"]))

ns0.objtypes.FileType(
    nodeId="ns=cas;i=5125",
    browseName="ns=cas;ConfigurationFile",
    description="Configuration file for the MCS in a compressed air system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6376", browseName="MimeType", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9917", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9923", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9924", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9925", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=9909"]),
        o6.hasComponent(o6.ns["ns=cas;i=9911"]),
        o6.hasComponent(o6.ns["ns=cas;i=9914"]),
        o6.hasComponent(o6.ns["ns=cas;i=9918"]),
        o6.hasComponent(o6.ns["ns=cas;i=9921"]),
        o6.hasComponent(o6.ns["ns=cas;i=9926"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9931",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9930",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9930", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9931"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9933",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9932",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9934",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9932",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9932", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9933"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9934"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9936",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9935",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9937",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9935",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9935", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9936"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9937"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9940",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9939",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9941",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9939",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9939", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9940"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=9941"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9943",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9942",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9942", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9943"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=9948",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=9947",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=9947", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=9948"]))

ns0.objtypes.FileType(
    nodeId="ns=cas;i=5126",
    browseName="ns=cas;ConfigurationFile",
    description="Configuration file for the MCS in a compressed air system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6401", browseName="MimeType", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9938", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9944", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9945", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9946", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=cas;i=9930"]),
        o6.hasComponent(o6.ns["ns=cas;i=9932"]),
        o6.hasComponent(o6.ns["ns=cas;i=9935"]),
        o6.hasComponent(o6.ns["ns=cas;i=9939"]),
        o6.hasComponent(o6.ns["ns=cas;i=9942"]),
        o6.hasComponent(o6.ns["ns=cas;i=9947"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9624",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9818", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9819", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9820", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9821", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9822", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9951", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9625",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9952", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9953", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9954", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9955", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9956", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9626",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9957", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9958", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9959", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9960", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9961", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9962", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9629",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9963", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9964", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9965", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9966", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9967", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9968", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5178",
    browseName="ns=cas;Input",
    description="Measured or calculated electrical properties at the input of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9628",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9623"]),
        o6.hasComponent(o6.ns["ns=cas;i=9624"]),
        o6.hasComponent(o6.ns["ns=cas;i=9625"]),
        o6.hasComponent(o6.ns["ns=cas;i=9626"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9627", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9629"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9969",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10004", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10005", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10007", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10008", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10009", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9970",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10010", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10011", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10013", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10014", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10015", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9971",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10016", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10017", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10018", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10019", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10020", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9972",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10021", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10022", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10023", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10024", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10025", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10026", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9975",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10027", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10028", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10029", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10030", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10031", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10032", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5067",
    browseName="ns=cas;Output",
    description="Measured or calculated electrical properties at the output of the component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9974",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9969"]),
        o6.hasComponent(o6.ns["ns=cas;i=9970"]),
        o6.hasComponent(o6.ns["ns=cas;i=9971"]),
        o6.hasComponent(o6.ns["ns=cas;i=9972"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9973", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9975"]),
    ],
)
o6.reference(cas_objtypes.ElectricalCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5067"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9976",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10033", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10034", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10035", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10036", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10037", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10038", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9977",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10039", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10040", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10041", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10042", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10043", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10044", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9978",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10045", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10046", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10047", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10048", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10049", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9979",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10050", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10051", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10052", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10053", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10054", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10055", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9982",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10056", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10057", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10058", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10059", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10060", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10061", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5110",
    browseName="ns=cas;Output",
    description="Measured or calculated electrical properties at the output of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9981",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9976"]),
        o6.hasComponent(o6.ns["ns=cas;i=9977"]),
        o6.hasComponent(o6.ns["ns=cas;i=9978"]),
        o6.hasComponent(o6.ns["ns=cas;i=9979"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9980", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9982"]),
    ],
)
cas_objtypes.ElectricalCircuitType(
    nodeId="ns=cas;i=5050",
    browseName="ns=cas;ElectricalCircuit",
    description="Measurements and calculations of the electrical ports and delta of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5052"]), o6.hasComponent(o6.ns["ns=cas;i=5109"]), o6.hasComponent(o6.ns["ns=cas;i=5110"])],
)
o6.reference(cas_objtypes.AirnetType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5050"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8478",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9867", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9868", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9869", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9870", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10067", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10068", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8482",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10069", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10073", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10074", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10077", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10078", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10079", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10085",
    browseName="ns=cas;<Quantity>",
    description="Measurement or calculation performed by a sensor.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6461", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6462", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7700", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7701", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Number,
)
cas_objtypes.OperationalType(
    nodeId="ns=cas;i=5137",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=10085"])],
)
o6.reference(cas_objtypes.SensorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5137"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8483",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10080", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10081", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10082", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10083", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10084", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10086", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6075",
    browseName="ns=cas;CompressorsIsolated",
    description="Number of isolated compressors in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6684", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10076", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10092", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10093", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8484",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10087", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10088", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10089", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10090", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10091", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10094", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8485",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10095", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10097", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10098", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10099", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10100", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10101", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8486",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10102", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10103", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10104", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10105", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10106", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10107", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8487",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10108", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10109", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10110", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10111", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10112", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10114", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9983",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10062", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10064", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10065", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10066", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10131", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9984",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10132", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10133", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10134", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10135", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10136", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10137", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9985",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10138", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10139", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10140", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10141", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10142", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9986",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10143", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10145", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10146", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10147", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10148", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9989",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10149", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10150", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10151", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10152", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10153", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10154", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5133",
    browseName="ns=cas;Output",
    description="Measured or calculated electrical properties at the output of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9988",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9983"]),
        o6.hasComponent(o6.ns["ns=cas;i=9984"]),
        o6.hasComponent(o6.ns["ns=cas;i=9985"]),
        o6.hasComponent(o6.ns["ns=cas;i=9986"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9987", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9989"]),
    ],
)
cas_objtypes.ElectricalCircuitType(
    nodeId="ns=cas;i=5055",
    browseName="ns=cas;ElectricalCircuit",
    description="Measurements and calculations of the electrical ports and delta of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5127"]), o6.hasComponent(o6.ns["ns=cas;i=5132"]), o6.hasComponent(o6.ns["ns=cas;i=5133"])],
)
o6.reference(cas_objtypes.MCSType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5055"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9990",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10155", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10156", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10157", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10158", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10159", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10160", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9991",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10161", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10162", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10163", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10164", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10165", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10166", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9992",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10167", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10168", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10169", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10170", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10171", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9993",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10172", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10173", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10174", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10175", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10176", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10177", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9996",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10178", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10179", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10180", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10181", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10182", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10183", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5146",
    browseName="ns=cas;Output",
    description="Measured or calculated electrical properties at the output of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9995",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9990"]),
        o6.hasComponent(o6.ns["ns=cas;i=9991"]),
        o6.hasComponent(o6.ns["ns=cas;i=9992"]),
        o6.hasComponent(o6.ns["ns=cas;i=9993"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9994", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9996"]),
    ],
)
cas_objtypes.ElectricalCircuitType(
    nodeId="ns=cas;i=5141",
    browseName="ns=cas;ElectricalCircuit",
    description="Measurements and calculations of the electrical ports and delta of the topology element.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5142"]), o6.hasComponent(o6.ns["ns=cas;i=5143"]), o6.hasComponent(o6.ns["ns=cas;i=5146"])],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9997",
    browseName="ns=cas;ApparentPower",
    description="Measured or calculated actual apparent power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10184", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10185", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10186", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10187", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10188", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10189", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9998",
    browseName="ns=cas;Current",
    description="Measured or calculated actual root mean square of the electric power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10190", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10191", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10192", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10193", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10194", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10195", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9999",
    browseName="ns=cas;Energy",
    description="Measured or calculated accumulated electrical energy consumed including all auxiliary components (e.g. on a compressor including fans, controller, …) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10196", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10197", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10198", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10199", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10200", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10000",
    browseName="ns=cas;Power",
    description="Measured or calculated actual electric real power consumption including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10201", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10202", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10203", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10204", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10205", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10206", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10003",
    browseName="ns=cas;Voltage",
    description="Measured or calculated actual root mean square of the voltage applied including all auxiliary components (e.g. on a compressor including fans, controller, …).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10207", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10209", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10210", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10211", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10212", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ElectricalQuantitiesType(
    nodeId="ns=cas;i=5180",
    browseName="ns=cas;Output",
    description="Measured or calculated electrical properties at the output of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=10002",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9997"]),
        o6.hasComponent(o6.ns["ns=cas;i=9998"]),
        o6.hasComponent(o6.ns["ns=cas;i=9999"]),
        o6.hasComponent(o6.ns["ns=cas;i=10000"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=10001", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=10003"]),
    ],
)
cas_objtypes.ElectricalCircuitType(
    nodeId="ns=cas;i=5145",
    browseName="ns=cas;ElectricalCircuit",
    description="Measurements and calculations of the electrical ports and delta of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5155"]), o6.hasComponent(o6.ns["ns=cas;i=5178"]), o6.hasComponent(o6.ns["ns=cas;i=5180"])],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5145"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8491",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10119", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10120", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10121", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10122", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10214", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10215", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8621",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10216", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10217", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10218", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10219", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10220", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10221", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6292",
    browseName="ns=cas;RealTimeSinceLastService",
    description="Real time passed since the sensor was last serviced.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10228", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10229", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10230", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10231", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10232", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.MaintenanceType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6292"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6506",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10070", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10071", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10072", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10236", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10237", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10238", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5129",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6463"]), o6.hasComponent(o6.ns["ns=cas;i=6464"]), o6.hasComponent(o6.ns["ns=cas;i=6506"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5116",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of fluid properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7179",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5129"]),
        o6.hasComponent(o6.ns["ns=cas;i=7172"]),
        o6.hasComponent(o6.ns["ns=cas;i=7173"]),
        o6.hasComponent(o6.ns["ns=cas;i=7174"]),
        o6.hasComponent(o6.ns["ns=cas;i=7175"]),
        o6.hasComponent(o6.ns["ns=cas;i=7176"]),
        o6.hasComponent(o6.ns["ns=cas;i=7177"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7178", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7187"]),
        o6.hasComponent(o6.ns["ns=cas;i=7188"]),
        o6.hasComponent(o6.ns["ns=cas;i=7189"]),
        o6.hasComponent(o6.ns["ns=cas;i=7864"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9358",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9753", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10130", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10239", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10240", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10241", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9359",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10242", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10243", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10244", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10245", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10246", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10247", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=9360",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10248", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10249", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10250", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10251", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10252", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10253", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8622",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10222", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10223", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10225", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10227", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10261", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10262", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6648",
    browseName="ns=cas;IsentropicEfficiency",
    description="Calculated isentropic efficiency.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6669", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6670", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6671", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10263", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10264", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.CompressorOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6648"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10113",
    browseName="ns=cas;IsentropicEfficiency",
    description="Calculated isentropic efficiency.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10115", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10116", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10117", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10265", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10266", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6659",
    browseName="ns=cas;SpecificEnergyRequirement",
    description="Calculated shaft input energy per unit of compressor actual rate of flow.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6677", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6678", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6679", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10267", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10268", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.CompressorOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6659"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6098",
    browseName="ns=cas;SpecificEnergyRequirement",
    description="Calculated shaft input energy per unit of compressor actual rate of flow.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6137", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6224", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6225", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10269", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10270", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6646",
    browseName="ns=cas;FlowRateRatio",
    description="Calculated ratio of actual and maximum possible flow rate of a compressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6666", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6667", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6668", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10271", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10272", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.CompressorOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6646"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6062",
    browseName="ns=cas;FlowRateRatio",
    description="Calculated ratio of actual and maximum possible flow rate of a compressor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6219", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6220", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6221", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10273", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10274", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.CompressorOperationalType(
    nodeId="ns=cas;i=5070",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=6061"]),
        o6.hasComponent(o6.ns["ns=cas;i=6062"]),
        o6.hasComponent(o6.ns["ns=cas;i=6067"]),
        o6.hasComponent(o6.ns["ns=cas;i=6098"]),
        o6.hasComponent(o6.ns["ns=cas;i=10113"]),
    ],
)
o6.reference(cas_objtypes.CompressorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5070"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8623",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10275", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10276", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10277", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10278", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10279", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10281", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6259",
    browseName="ns=cas;RealTimeToNextService",
    description="Real time left until the real time of the next service level is exceeded.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6397", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6398", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6399", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10280", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10282", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6396",
    browseName="ns=cas;RealTimeToNextService",
    description="Real time left until the real time of the next service level is exceeded.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10283", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10284", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10285", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10286", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10288", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8635",
    browseName="ns=cas;AbsolutePressure",
    description="Measured or calculated actual absolute pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10287", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10289", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10290", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10291", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10292", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10293", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10096",
    browseName="ns=cas;RunningTimeToNextService",
    description="Running time left until the running time of the next service level is exceeded.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10118", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10259", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10260", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10295", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10297", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.StatisticsType(
    nodeId="ns=cas;i=5018",
    browseName="ns=di;Statistics",
    description="Data for statistics applications for the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8518",
                browseName="ns=ia;ResetCondition",
                description="The reason and context for the reset of the statistics, which is done without a trigger from an OPC UA Client, like calling the ResetStatistics Method. ResetCondition is a vendor-specific, human readable string. ResetCondition is non-localized and might contain an expression that can be parsed by certain clients. Examples are: “AFTER 4 HOURS”, “AFTER 1000 ITEMS”, “OPERATOR”. “OPERATOR” means, that an operator resets the statistics on a local HMI.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8521",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=6259"]),
        o6.hasComponent(o6.ns["ns=cas;i=8517"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8519", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8520"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8522", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.ns["ns=cas;i=10096"]),
    ],
)
o6.reference(cas_objtypes.MCSType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5018"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10224",
    browseName="ns=cas;RealTimeSinceLastService",
    description="Real time passed since the sensor was last serviced.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10233", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10234", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10235", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10299", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10300", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6714",
    browseName="ns=cas;RealTimeToNextService",
    description="Real time left until the sensor is scheduled for the next servicing.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10301", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10302", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10303", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10304", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10305", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.MaintenanceType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6714"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6693",
    browseName="ns=cas;CatalyticMaterialTemperature",
    description="Measured actual temperature of the catalytic material inside a converter.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6695", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6696", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6700", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10307", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10308", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.ConverterOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6693"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6454",
    browseName="ns=cas;CatalyticMaterialTemperature",
    description="Measured actual temperature of the catalytic material inside a converter.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6458", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6459", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8015", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10309", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10310", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ConverterOperationalType(
    nodeId="ns=cas;i=5159",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6454"])],
)
o6.reference(cas_objtypes.ConverterType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5159"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6701",
    browseName="ns=cas;PressureDewPoint",
    description="Measured or calculated actual pressure dew point of the process fluid at a dryer.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6706", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6707", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6708", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10311", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10312", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.DryerOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6701"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6452",
    browseName="ns=cas;PressureDewPoint",
    description="Measured or calculated actual pressure dew point of the process fluid at a dryer.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6457", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6544", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6545", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10313", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10314", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8638",
    browseName="ns=cas;AccumulatedVolume",
    description="Measured or calculated accumulated volume of a fluid since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10294", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10296", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10315", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10316", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10317", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10318", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6546",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10254", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10255", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10256", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10257", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10258", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10323", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5153",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6542"]), o6.hasComponent(o6.ns["ns=cas;i=6543"]), o6.hasComponent(o6.ns["ns=cas;i=6546"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5037",
    browseName="ns=cas;Inlet",
    description="Measured or calculated fluid properties at the inlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8804",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5153"]),
        o6.hasComponent(o6.ns["ns=cas;i=7285"]),
        o6.hasComponent(o6.ns["ns=cas;i=7286"]),
        o6.hasComponent(o6.ns["ns=cas;i=7287"]),
        o6.hasComponent(o6.ns["ns=cas;i=7288"]),
        o6.hasComponent(o6.ns["ns=cas;i=7337"]),
        o6.hasComponent(o6.ns["ns=cas;i=7338"]),
        o6.hasComponent(o6.ns["ns=cas;i=8802"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8803", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8805"]),
        o6.hasComponent(o6.ns["ns=cas;i=8806"]),
        o6.hasComponent(o6.ns["ns=cas;i=8807"]),
    ],
)
cas_objtypes.FluidCircuitType(
    nodeId="ns=cas;i=5031",
    browseName="ns=cas;ProcessFluidCircuit",
    description="Measurements and calculations of the process fluid ports and delta of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5034"]), o6.hasComponent(o6.ns["ns=cas;i=5037"]), o6.hasComponent(o6.ns["ns=cas;i=5040"]), o6.hasComponent(o6.ns["ns=cas;i=6009"])],
)
o6.reference(cas_objtypes.AirnetType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5031"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6563",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10324", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10325", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10326", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10327", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10328", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10329", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5154",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6549"]), o6.hasComponent(o6.ns["ns=cas;i=6560"]), o6.hasComponent(o6.ns["ns=cas;i=6563"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5124",
    browseName="ns=cas;Outlet",
    description="Measured or calculated fluid properties at the outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9357",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5154"]),
        o6.hasComponent(o6.ns["ns=cas;i=9349"]),
        o6.hasComponent(o6.ns["ns=cas;i=9350"]),
        o6.hasComponent(o6.ns["ns=cas;i=9351"]),
        o6.hasComponent(o6.ns["ns=cas;i=9352"]),
        o6.hasComponent(o6.ns["ns=cas;i=9353"]),
        o6.hasComponent(o6.ns["ns=cas;i=9354"]),
        o6.hasComponent(o6.ns["ns=cas;i=9355"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9356", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9358"]),
        o6.hasComponent(o6.ns["ns=cas;i=9359"]),
        o6.hasComponent(o6.ns["ns=cas;i=9360"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8640",
    browseName="ns=cas;DewPoint",
    description="Measured or calculated actual dew point of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10319", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10320", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10321", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10322", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10330", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10331", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6570",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10336", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10337", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10338", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10339", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10340", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10341", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5172",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6568"]), o6.hasComponent(o6.ns["ns=cas;i=6569"]), o6.hasComponent(o6.ns["ns=cas;i=6570"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5165",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of fluid properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7168",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5172"]),
        o6.hasComponent(o6.ns["ns=cas;i=7055"]),
        o6.hasComponent(o6.ns["ns=cas;i=7057"]),
        o6.hasComponent(o6.ns["ns=cas;i=7058"]),
        o6.hasComponent(o6.ns["ns=cas;i=7059"]),
        o6.hasComponent(o6.ns["ns=cas;i=7061"]),
        o6.hasComponent(o6.ns["ns=cas;i=7166"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7167", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7169"]),
        o6.hasComponent(o6.ns["ns=cas;i=7170"]),
        o6.hasComponent(o6.ns["ns=cas;i=7171"]),
        o6.hasComponent(o6.ns["ns=cas;i=7813"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6573",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10342", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10343", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10344", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10345", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10346", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10347", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5181",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6571"]), o6.hasComponent(o6.ns["ns=cas;i=6572"]), o6.hasComponent(o6.ns["ns=cas;i=6573"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5166",
    browseName="ns=cas;Inlet",
    description="Measured or calculated fluid properties at the inlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8846",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5181"]),
        o6.hasComponent(o6.ns["ns=cas;i=8808"]),
        o6.hasComponent(o6.ns["ns=cas;i=8809"]),
        o6.hasComponent(o6.ns["ns=cas;i=8810"]),
        o6.hasComponent(o6.ns["ns=cas;i=8811"]),
        o6.hasComponent(o6.ns["ns=cas;i=8812"]),
        o6.hasComponent(o6.ns["ns=cas;i=8828"]),
        o6.hasComponent(o6.ns["ns=cas;i=8844"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8845", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8847"]),
        o6.hasComponent(o6.ns["ns=cas;i=8848"]),
        o6.hasComponent(o6.ns["ns=cas;i=8849"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7182",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10348", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10349", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10350", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10351", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10352", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10353", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5182",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=7180"]), o6.hasComponent(o6.ns["ns=cas;i=7181"]), o6.hasComponent(o6.ns["ns=cas;i=7182"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5169",
    browseName="ns=cas;Outlet",
    description="Measured or calculated fluid properties at the outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9345",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5182"]),
        o6.hasComponent(o6.ns["ns=cas;i=9332"]),
        o6.hasComponent(o6.ns["ns=cas;i=9333"]),
        o6.hasComponent(o6.ns["ns=cas;i=9334"]),
        o6.hasComponent(o6.ns["ns=cas;i=9340"]),
        o6.hasComponent(o6.ns["ns=cas;i=9341"]),
        o6.hasComponent(o6.ns["ns=cas;i=9342"]),
        o6.hasComponent(o6.ns["ns=cas;i=9343"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9344", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9346"]),
        o6.hasComponent(o6.ns["ns=cas;i=9347"]),
        o6.hasComponent(o6.ns["ns=cas;i=9348"]),
    ],
)
cas_objtypes.FluidCircuitType(
    nodeId="ns=cas;i=5135",
    browseName="ns=cas;ProcessFluidCircuit",
    description="Measurements and calculations of the process fluid ports and delta of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5165"]), o6.hasComponent(o6.ns["ns=cas;i=5166"]), o6.hasComponent(o6.ns["ns=cas;i=5169"]), o6.hasComponent(o6.ns["ns=cas;i=9147"])],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5135"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8642",
    browseName="ns=cas;GaugePressure",
    description="Measured or calculated actual gauge pressure of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10332", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10333", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10334", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10335", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10354", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10355", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7262",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10360", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10361", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10362", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10363", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10364", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10365", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5186",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=7260"]), o6.hasComponent(o6.ns["ns=cas;i=7261"]), o6.hasComponent(o6.ns["ns=cas;i=7262"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5123",
    browseName="ns=cas;Inlet",
    description="Measured or calculated fluid properties at the inlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8946",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5186"]),
        o6.hasComponent(o6.ns["ns=cas;i=8850"]),
        o6.hasComponent(o6.ns["ns=cas;i=8851"]),
        o6.hasComponent(o6.ns["ns=cas;i=8934"]),
        o6.hasComponent(o6.ns["ns=cas;i=8935"]),
        o6.hasComponent(o6.ns["ns=cas;i=8936"]),
        o6.hasComponent(o6.ns["ns=cas;i=8937"]),
        o6.hasComponent(o6.ns["ns=cas;i=8944"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8945", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8947"]),
        o6.hasComponent(o6.ns["ns=cas;i=8948"]),
        o6.hasComponent(o6.ns["ns=cas;i=8949"]),
    ],
)
cas_objtypes.FluidCircuitType(
    nodeId="ns=cas;i=5138",
    browseName="ns=cas;CoolantCircuit",
    description="Measurements and calculations of the coolant ports and delta of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5116"]), o6.hasComponent(o6.ns["ns=cas;i=5123"]), o6.hasComponent(o6.ns["ns=cas;i=5124"]), o6.hasComponent(o6.ns["ns=cas;i=8297"])],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5138"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7278",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10366", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10367", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10368", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10369", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10370", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10371", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5201",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=7263"]), o6.hasComponent(o6.ns["ns=cas;i=7277"]), o6.hasComponent(o6.ns["ns=cas;i=7278"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5179",
    browseName="ns=cas;<Other>",
    description="Placeholder for manufacturer or system specific groups.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=7716",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5201"]),
        o6.hasComponent(o6.ns["ns=cas;i=7339"]),
        o6.hasComponent(o6.ns["ns=cas;i=7340"]),
        o6.hasComponent(o6.ns["ns=cas;i=7341"]),
        o6.hasComponent(o6.ns["ns=cas;i=7342"]),
        o6.hasComponent(o6.ns["ns=cas;i=7343"]),
        o6.hasComponent(o6.ns["ns=cas;i=7713"]),
        o6.hasComponent(o6.ns["ns=cas;i=7714"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7715", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7717"]),
        o6.hasComponent(o6.ns["ns=cas;i=7718"]),
        o6.hasComponent(o6.ns["ns=cas;i=7719"]),
    ],
)
o6.reference(cas_objtypes.FluidCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5179"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7299",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10372", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10373", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10374", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10375", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10376", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10377", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5216",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=7297"]), o6.hasComponent(o6.ns["ns=cas;i=7298"]), o6.hasComponent(o6.ns["ns=cas;i=7299"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5202",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of fluid properties between inlet and outlet of the component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6630",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5216"]),
        o6.hasComponent(o6.ns["ns=cas;i=6574"]),
        o6.hasComponent(o6.ns["ns=cas;i=6575"]),
        o6.hasComponent(o6.ns["ns=cas;i=6577"]),
        o6.hasComponent(o6.ns["ns=cas;i=6578"]),
        o6.hasComponent(o6.ns["ns=cas;i=6579"]),
        o6.hasComponent(o6.ns["ns=cas;i=6629"]),
        o6.hasComponent(o6.ns["ns=cas;i=6635"]),
        o6.hasComponent(o6.ns["ns=cas;i=6720"]),
        o6.hasComponent(o6.ns["ns=cas;i=6722"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7008", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7811"]),
    ],
)
o6.reference(cas_objtypes.FluidCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5202"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7302",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10378", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10379", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10380", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10381", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10382", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10383", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5265",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=7300"]), o6.hasComponent(o6.ns["ns=cas;i=7301"]), o6.hasComponent(o6.ns["ns=cas;i=7302"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5251",
    browseName="ns=cas;Outlet",
    description="Measured or calculated fluid properties at the outlet of the component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=9316",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5265"]),
        o6.hasComponent(o6.ns["ns=cas;i=9308"]),
        o6.hasComponent(o6.ns["ns=cas;i=9309"]),
        o6.hasComponent(o6.ns["ns=cas;i=9310"]),
        o6.hasComponent(o6.ns["ns=cas;i=9311"]),
        o6.hasComponent(o6.ns["ns=cas;i=9312"]),
        o6.hasComponent(o6.ns["ns=cas;i=9313"]),
        o6.hasComponent(o6.ns["ns=cas;i=9314"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=9315", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=9317"]),
        o6.hasComponent(o6.ns["ns=cas;i=9318"]),
        o6.hasComponent(o6.ns["ns=cas;i=9319"]),
    ],
)
o6.reference(cas_objtypes.FluidCircuitType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5251"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8643",
    browseName="ns=cas;MassFlowRate",
    description="Measured or calculated actual mass flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10356", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10357", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10358", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10359", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10384", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10385", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8644",
    browseName="ns=cas;OilConcentration",
    description="Measured or calculated actual oil concentration of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10386", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10387", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10388", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10389", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10390", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10391", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8648",
    browseName="ns=cas;RelativeHumidity",
    description="Measured or calculated actual relative humidity of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10392", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10393", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10394", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10395", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10396", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10397", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8651",
    browseName="ns=cas;Temperature",
    description="Measured or calculated actual temperature of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10398", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10399", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10400", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10401", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10402", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10403", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8652",
    browseName="ns=cas;Volume",
    description="Measured or calculated actual volume of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10404", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10405", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10406", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10407", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10408", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10409", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8653",
    browseName="ns=cas;VolumeFlowRate",
    description="Measured or calculated actual volume flow rate of a fluid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10410", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10411", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10412", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10413", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10414", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10415", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8416",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10416", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10417", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10418", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10419", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10420", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10421", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8417",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10422", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10423", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10424", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10425", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10426", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10427", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8418",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10428", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10429", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10430", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10431", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10432", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10433", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5162",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=8416"]), o6.hasComponent(o6.ns["ns=cas;i=8417"]), o6.hasComponent(o6.ns["ns=cas;i=8418"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5151",
    browseName="ns=cas;Delta",
    description="Measured or calculated deltas of fluid properties between inlet and outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8474",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5162"]),
        o6.hasComponent(o6.ns["ns=cas;i=8410"]),
        o6.hasComponent(o6.ns["ns=cas;i=8411"]),
        o6.hasComponent(o6.ns["ns=cas;i=8412"]),
        o6.hasComponent(o6.ns["ns=cas;i=8413"]),
        o6.hasComponent(o6.ns["ns=cas;i=8414"]),
        o6.hasComponent(o6.ns["ns=cas;i=8415"]),
        o6.hasComponent(o6.ns["ns=cas;i=8472"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8473", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8475"]),
        o6.hasComponent(o6.ns["ns=cas;i=8476"]),
        o6.hasComponent(o6.ns["ns=cas;i=8478"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8488",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10434", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10435", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10436", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10437", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10438", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10439", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8489",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10440", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10441", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10442", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10443", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10444", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10445", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8490",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10446", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10447", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10448", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10449", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10450", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10451", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5171",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=8488"]), o6.hasComponent(o6.ns["ns=cas;i=8489"]), o6.hasComponent(o6.ns["ns=cas;i=8490"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5156",
    browseName="ns=cas;Inlet",
    description="Measured or calculated fluid properties at the inlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8620",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5171"]),
        o6.hasComponent(o6.ns["ns=cas;i=8482"]),
        o6.hasComponent(o6.ns["ns=cas;i=8483"]),
        o6.hasComponent(o6.ns["ns=cas;i=8484"]),
        o6.hasComponent(o6.ns["ns=cas;i=8485"]),
        o6.hasComponent(o6.ns["ns=cas;i=8486"]),
        o6.hasComponent(o6.ns["ns=cas;i=8487"]),
        o6.hasComponent(o6.ns["ns=cas;i=8491"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8619", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8621"]),
        o6.hasComponent(o6.ns["ns=cas;i=8622"]),
        o6.hasComponent(o6.ns["ns=cas;i=8623"]),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8645",
    browseName="ns=cas;Fine",
    description="Particle count of sizes from 0.1 to 0.5 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10452", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10453", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10454", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10455", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10456", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10457", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8646",
    browseName="ns=cas;Large",
    description="Particle count of sizes from 1.0 to 5.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10458", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10459", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10460", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10461", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10462", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10463", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=8647",
    browseName="ns=cas;Medium",
    description="Particle count of sizes from 0.5 to 1.0 um.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10464", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10465", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10466", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10467", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10468", browseName="ns=cas;KindOfQuantity", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10469", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
cas_objtypes.ParticleType(
    nodeId="ns=cas;i=5183",
    browseName="ns=cas;ParticlesPerSizeRange",
    description="Collection of particle counts for a fluid according to ISO 8573.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=8645"]), o6.hasComponent(o6.ns["ns=cas;i=8646"]), o6.hasComponent(o6.ns["ns=cas;i=8647"])],
)
cas_objtypes.FluidQuantitiesType(
    nodeId="ns=cas;i=5157",
    browseName="ns=cas;Outlet",
    description="Measured or calculated fluid properties at the outlet of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8650",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5183"]),
        o6.hasComponent(o6.ns["ns=cas;i=8635"]),
        o6.hasComponent(o6.ns["ns=cas;i=8638"]),
        o6.hasComponent(o6.ns["ns=cas;i=8640"]),
        o6.hasComponent(o6.ns["ns=cas;i=8642"]),
        o6.hasComponent(o6.ns["ns=cas;i=8643"]),
        o6.hasComponent(o6.ns["ns=cas;i=8644"]),
        o6.hasComponent(o6.ns["ns=cas;i=8648"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8649", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8651"]),
        o6.hasComponent(o6.ns["ns=cas;i=8652"]),
        o6.hasComponent(o6.ns["ns=cas;i=8653"]),
    ],
)
cas_objtypes.FluidCircuitType(
    nodeId="ns=cas;i=5063",
    browseName="ns=cas;ProcessFluidCircuit",
    description="Measurements and calculations of the process fluid ports and delta of the topology element.",
    references=[o6.hasComponent(o6.ns["ns=cas;i=5151"]), o6.hasComponent(o6.ns["ns=cas;i=5156"]), o6.hasComponent(o6.ns["ns=cas;i=5157"]), o6.hasComponent(o6.ns["ns=cas;i=7771"])],
)
cas_objtypes.AirnetType(
    nodeId="ns=cas;i=5029",
    browseName="ns=machinery;<Component>",
    description="Represents of an airnet.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5030"]),
        o6.hasComponent(o6.ns["ns=cas;i=5032"]),
        o6.hasComponent(o6.ns["ns=cas;i=5047"]),
        o6.hasComponent(o6.ns["ns=cas;i=5049"]),
        o6.hasComponent(o6.ns["ns=cas;i=5053"]),
        o6.hasComponent(o6.ns["ns=cas;i=5056"]),
        o6.hasComponent(o6.ns["ns=cas;i=5063"]),
    ],
)
o6.reference(cas_objtypes.AirnetsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5029"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=10517",
    browseName="ns=cas;FluidType",
    description="Enumeration of possible process fluid types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10518", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FluidTypeEnum,
    value=cas_datypes.FluidTypeEnum.CONDENSATE,
)
cas_objtypes.FluidCircuitType(
    nodeId="ns=cas;i=5185",
    browseName="ns=cas;ProcessFluidCircuit",
    description="Measurements and calculations of the process fluid ports and delta of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=10517"])],
)
o6.reference(cas_objtypes.DrainType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5185"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=10516",
    browseName="ns=cas;FluidType",
    description="Enumeration of possible process fluid types.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10519", browseName="Definition", dataType=o6.String))],
    dataType=cas_datypes.FluidTypeEnum,
    value=cas_datypes.FluidTypeEnum.CONDENSATE,
)
cas_objtypes.FluidCircuitType(
    nodeId="ns=cas;i=5184",
    browseName="ns=cas;ProcessFluidCircuit",
    description="Measurements and calculations of the process fluid ports and delta of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=10516"])],
)
o6.reference(cas_objtypes.SeparatorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5184"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10529",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("IPv4"), description=o6.LocalizedText("IP address is in IPv4 format")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("IPv6"), description=o6.LocalizedText("IP address is in IPv6 format")),
    ],
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=6799",
    browseName="ns=cas;SoftSensor",
    description="Indicates if the sensor is a software or hardware sensor.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=6800", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("This sensor is a hardware sensor."))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=8162", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("This sensor is a software sensor."))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10531", browseName="Definition", dataType=o6.String)),
    ],
    dataType=o6.Boolean,
)
cas_objtypes.SensorDesignType(
    nodeId="ns=cas;i=5064",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6089"]), o6.hasComponent(o6.ns["ns=cas;i=6690"]), o6.hasComponent(o6.ns["ns=cas;i=6799"])],
)
o6.reference(cas_objtypes.SensorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5064"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10532",
    browseName="ns=cas;AirDeliveryRate",
    description="Volume of generated compressed air per time frame.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10538", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10539", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10540", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10541", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10542", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=10532"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10536",
    browseName="ns=cas;SpecificEnergyCost",
    description="Costs for generating a volume of compressed air.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10543", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10544", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10545", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10546", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10547", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=10536"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10534",
    browseName="ns=cas;SpecificEnergy",
    description="Electrical energy consumed in the generation of a volume of compressed air.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10548", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10549", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10550", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10551", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10552", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=10534"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10553",
    browseName="ns=cas;AirDeliveryRate",
    description="Volume of generated compressed air per time frame.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10559", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10560", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10561", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10562", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10563", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10555",
    browseName="ns=cas;SpecificEnergy",
    description="Electrical energy consumed in the generation of a volume of compressed air.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10564", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10565", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10566", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10567", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10568", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10557",
    browseName="ns=cas;SpecificEnergyCost",
    description="Costs for generating a volume of compressed air.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10569", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10570", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10571", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10572", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10573", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=6655",
    browseName="ns=cas;OnOff",
    description="Actual OnOff state of the component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6675", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("The component is switched off and not able to operate.")
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6769", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6770", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=10607",
                browseName="TrueState",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("The component is switched on and is in a specific operating state."),
            )
        ),
    ],
    dataType=o6.Boolean,
)
o6.reference(cas_objtypes.OperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6655"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10608",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OK"), description=o6.LocalizedText("All requirements can be fulfilled.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Warning"), description=o6.LocalizedText("Check required, possibly there is a problem that leads to an Error.")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Error"), description=o6.LocalizedText("Immediate action needed to avoid Critical.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Critical"), description=o6.LocalizedText("At least one requirement cannot be fulfilled.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10609",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("FullyIntegrated"), description=o6.LocalizedText("The MCS controls all compressors of this airnet.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("PartiallyIntegrated"), description=o6.LocalizedText("At least one compressor of this airnet is not controlled by the MCS.")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("FullyIsolated"), description=o6.LocalizedText("The MCS does not control any compressor of this airnet.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10610",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("The airnet is in a state not specified by this enumeration.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Stopped"), description=o6.LocalizedText("The requirements shall not be fulfilled.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Starting"), description=o6.LocalizedText("Transition phase to end in Operational state.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Stopping"), description=o6.LocalizedText("Transition phase to end in Stopped state.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Operational"), description=o6.LocalizedText("The requirements should be fulfilled.")),
    ],
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=7579",
    browseName="ns=cas;RunningTimeToNextService",
    description="Running time left until the running time of the next service level is exceeded.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10298", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10612", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10613", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10614", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10616", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.StatisticsType(
    nodeId="ns=cas;i=5130",
    browseName="ns=di;Statistics",
    description="Data for statistics applications for the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6054",
                browseName="ns=ia;ResetCondition",
                description="The reason and context for the reset of the statistics, which is done without a trigger from an OPC UA Client, like calling the ResetStatistics Method. ResetCondition is a vendor-specific, human readable string. ResetCondition is non-localized and might contain an expression that can be parsed by certain clients. Examples are: “AFTER 4 HOURS”, “AFTER 1000 ITEMS”, “OPERATOR”. “OPERATOR” means, that an operator resets the statistics on a local HMI.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=6060",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=6053"]),
        o6.hasComponent(o6.ns["ns=cas;i=6056"]),
        o6.hasComponent(o6.ns["ns=cas;i=6396"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6509", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.ns["ns=cas;i=7579"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=7661", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
    ],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5130"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6029",
    browseName="ns=cas;VolumeFlowRateAvailable",
    description="Measured or calculated available volume flow rate of the process fluid in the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6042", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6043", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6048", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10623", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10624", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6029"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6080",
    browseName="ns=cas;VolumeFlowRateAvailable",
    description="Measured or calculated available volume flow rate of the process fluid in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6106", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6107", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6108", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10625", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10626", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6031",
    browseName="ns=cas;VolumeFlowRateUnavailable",
    description="Calculated unavailable volume flow rate of the process fluid in the airnet.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6049", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6051", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6055", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10627", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10628", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.AirnetOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6031"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6082",
    browseName="ns=cas;VolumeFlowRateUnavailable",
    description="Calculated unavailable volume flow rate of the process fluid in the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6109", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6110", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6111", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10629", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10630", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=cas;i=7890",
    browseName="ns=cas;Volume",
    description="Total volume of the receiver.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10632", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10633", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10634", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10635", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10636", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.ReceiverDesignType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=7890"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=cas;i=10637",
    browseName="ns=cas;Volume",
    description="Total volume of the receiver.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10638", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10639", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10640", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10641", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10642", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.ReceiverDesignType(
    nodeId="ns=cas;i=5062",
    browseName="ns=cas;Design",
    description="Static design properties of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6088"]), o6.hasComponent(o6.ns["ns=cas;i=10637"])],
)
o6.reference(cas_objtypes.ReceiverType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5062"])
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10645",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OK"), description=o6.LocalizedText("The main function can be fulfilled.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Warning"), description=o6.LocalizedText("Check required, possibly there is a problem that leads to an Error.")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Error"), description=o6.LocalizedText("Immediate action needed to avoid Critical.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Critical"), description=o6.LocalizedText("The main function cannot be fulfilled.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10646",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("FullyIntegrated"), description=o6.LocalizedText("Compressed air generation or treatment is fully controlled by the MCS.")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("PartiallyIntegrated"), description=o6.LocalizedText("Compressed air generation or treatment is partially controlled by the MCS.")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("FullyIsolated"), description=o6.LocalizedText("Compressed air generation or treatment is not controlled by the MCS.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10647",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("The component is in a state not specified by this enumeration.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Stopped"), description=o6.LocalizedText("The main function shall not be fulfilled.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Starting"), description=o6.LocalizedText("Transition phase to end in Operational state.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Stopping"), description=o6.LocalizedText("Transition phase to end in Stopped state.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Operational"), description=o6.LocalizedText("The main function should be fulfilled.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10648",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("The compressor is in a state not specified by this enumeration.")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Stopped"), description=o6.LocalizedText("The motor is not running.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Starting"), description=o6.LocalizedText("Transition phase to end in Unloaded state.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Stopping"), description=o6.LocalizedText("Transition phase to end in Stopped state.")),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Unloaded"),
            description=o6.LocalizedText("The motor is running but the compressor does not deliver compressed air to the airnet."),
        ),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Loading"), description=o6.LocalizedText("Transition phase to end in Loaded state.")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Unloading"), description=o6.LocalizedText("Transition phase to end in Unloaded state.")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Loaded"), description=o6.LocalizedText("The compressor does deliver compressed air to the airnet.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=10649",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cas;i=3026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[13],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("The dryer is in a state not specified by this enumeration.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Stopped"), description=o6.LocalizedText("The dryer is stopped. This state is applicable to all adsorption dryers.")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("Running"), description=o6.LocalizedText("The dryer is running. This state is applicable to all dryers.")
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("RefrigerantCompressorStopped"),
            description=o6.LocalizedText(
                "The compressor of the refrigerant circuit is standing still, and the refrigerant dryer is operating using the stored cold. This state is applicable to refrigerant dryers."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("RefrigerantCompressorRunning"),
            description=o6.LocalizedText(
                "The compressor of the refrigerant circuit is running and compressing refrigerant, creating cold. This state is applicable to refrigerant dryers."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("PurgeValveClosed"),
            description=o6.LocalizedText(
                "Purge valve is closed, and no purge air is consumed, no purge of the humidity from membranes dryer. This state is applicable to membrane dryers."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("PurgeValveOpen"),
            description=o6.LocalizedText("Purge air can flow to purge the humidity out of the membrane dryer. This state is applicable to membrane dryers."),
        ),
        ns0.datatypes.EnumValueType(
            value=7,
            displayName=o6.LocalizedText("ParallelModeOfBothVessels"),
            description=o6.LocalizedText("Both vessels of the adsorption dryer are used in parallel for adsorption. This state is applicable to all adsorption dryers."),
        ),
        ns0.datatypes.EnumValueType(
            value=8,
            displayName=o6.LocalizedText("Depressurizing"),
            description=o6.LocalizedText(
                "One vessel of the adsorption dryer is depressurized for regeneration. This state is applicable to heatless and heated adsorption dryers, not HOC."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=9,
            displayName=o6.LocalizedText("Desorbing"),
            description=o6.LocalizedText(
                "One vessel of the adsorption dryer is in desorption phase, using purge or ambient air, heated or not heated. This state is applicable to all adsorption dryers."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=10,
            displayName=o6.LocalizedText("Cooling"),
            description=o6.LocalizedText(
                "One vessel of the adsorption dryer is being cooled after being heated in the previous desorption phase. This state is applicable to heated adsorption dryers and HOC."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=11,
            displayName=o6.LocalizedText("Pressurizing"),
            description=o6.LocalizedText("The depressurized vessel is pressurized again. This state is applicable to heatless and heated adsorption dryers, not HOC."),
        ),
        ns0.datatypes.EnumValueType(
            value=12,
            displayName=o6.LocalizedText("RegeneratedVesselInStand-by"),
            description=o6.LocalizedText("The regenerated vessel is in standby and ready for adsorption phase. This state is applicable to all adsorption dryers."),
        ),
    ],
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=6657",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the airnet.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8231", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10650", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.AirnetOperatingStateEnum,
)
cas_objtypes.AirnetOperationalType(
    nodeId="ns=cas;i=5008",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=6073"]),
        o6.hasComponent(o6.ns["ns=cas;i=6075"]),
        o6.hasComponent(o6.ns["ns=cas;i=6078"]),
        o6.hasComponent(o6.ns["ns=cas;i=6080"]),
        o6.hasComponent(o6.ns["ns=cas;i=6082"]),
        o6.hasComponent(o6.ns["ns=cas;i=6223"]),
        o6.hasComponent(o6.ns["ns=cas;i=6656"]),
        o6.hasComponent(o6.ns["ns=cas;i=6657"]),
        o6.hasComponent(o6.ns["ns=cas;i=8290"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8479", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.ns["ns=cas;i=10553"]),
        o6.hasComponent(o6.ns["ns=cas;i=10555"]),
        o6.hasComponent(o6.ns["ns=cas;i=10557"]),
    ],
)
o6.reference(cas_objtypes.AirnetType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5008"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10665",
    browseName="ns=cas;RealTimeToNextService",
    description="Real time left until the real time of the next service level is exceeded.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10666", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10667", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10668", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10669", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10675", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=10670",
    browseName="ns=cas;OnOff",
    description="Actual OnOff state of the dryer. For membrane dryers this describes the state of the controller.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=10671", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("The dryer is switched off."))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10672", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("The dryer is switched on."))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10678", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10679", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Boolean,
)
o6.reference(cas_objtypes.DryerOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=10670"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=10673",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the dryer.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10680", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10681", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.DryerOperatingStateEnum,
)
o6.reference(cas_objtypes.DryerOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=10673"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10691",
    browseName="ns=cas;ContinuousPosition",
    description="Actual valve stroke.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10700", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10701", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10702", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10703", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10704", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10688",
    browseName="ns=cas;RunningTimeToNextService",
    description="Running time left until the running time of the next service level is exceeded.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10689", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10690", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10693", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10694", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10706", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.StatisticsType(
    nodeId="ns=cas;i=5703",
    browseName="ns=di;Statistics",
    description="Data for statistics applications for the topology element.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8524",
                browseName="ns=ia;ResetCondition",
                description="The reason and context for the reset of the statistics, which is done without a trigger from an OPC UA Client, like calling the ResetStatistics Method. ResetCondition is a vendor-specific, human readable string. ResetCondition is non-localized and might contain an expression that can be parsed by certain clients. Examples are: “AFTER 4 HOURS”, “AFTER 1000 ITEMS”, “OPERATOR”. “OPERATOR” means, that an operator resets the statistics on a local HMI.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=8540",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8523"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=cas;i=8538", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time."
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=8539"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8585", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.ns["ns=cas;i=10665"]),
        o6.hasComponent(o6.ns["ns=cas;i=10688"]),
    ],
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=10695",
    browseName="ns=cas;OnOff",
    description="Actual OnOff state of the dryer. For membrane dryers this describes the state of the controller.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=10696", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("The dryer is switched off."))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10697", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("The dryer is switched on."))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10709", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10710", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Boolean,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=10698",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the dryer.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10711", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10712", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.DryerOperatingStateEnum,
)
cas_objtypes.DryerOperationalType(
    nodeId="ns=cas;i=5160",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=6452"]), o6.hasComponent(o6.ns["ns=cas;i=10695"]), o6.hasComponent(o6.ns["ns=cas;i=10698"])],
)
o6.reference(cas_objtypes.DryerType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5160"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=10699",
    browseName="ns=cas;PortUsed",
    description="Actual port used.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10713", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10714", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
cas_objtypes.ValveOperationalType(
    nodeId="ns=cas;i=5161",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=10691"]), o6.hasComponent(o6.ns["ns=cas;i=10699"])],
)
o6.reference(cas_objtypes.ValveType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5161"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=10715",
    browseName="ns=cas;HealthState",
    description="Actual health state of the component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10721", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10722", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.HealthStateEnum,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=10716",
    browseName="ns=cas;IntegratedState",
    description="Actual integrated state of the component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10723", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10724", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.IntegratedStateEnum,
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=10717",
    browseName="ns=cas;OnOff",
    description="Actual OnOff state of the component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=10718", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("The component is switched off and not able to operate.")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=10719",
                browseName="TrueState",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("The component is switched on and is in a specific operating state."),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10725", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10726", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Boolean,
)
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=10720",
    browseName="ns=cas;OperatingState",
    description="Actual operating state of the component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10727", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10728", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=cas_datypes.OperatingStateEnum,
)
cas_objtypes.OperationalType(
    nodeId="ns=cas;i=5036",
    browseName="ns=di;Operational",
    description="Data for normal operation of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6547", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.ns["ns=cas;i=10715"]),
        o6.hasComponent(o6.ns["ns=cas;i=10716"]),
        o6.hasComponent(o6.ns["ns=cas;i=10717"]),
        o6.hasComponent(o6.ns["ns=cas;i=10720"]),
    ],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5036"])
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=10851",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10852", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)


o6.call(nodeId="ns=cas;i=10856", browseName="Disable")
o6.reference(o6.ns["ns=cas;i=10856"], "i=3065", "i=2803")

o6.call(nodeId="ns=cas;i=10857", browseName="Enable")
o6.reference(o6.ns["ns=cas;i=10857"], "i=3065", "i=2803")

ns0.vartypes.TwoStateVariableType(
    nodeId="ns=cas;i=10858",
    browseName="EnabledState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10859", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=10862",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10863", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=cas;i=10865",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10866", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.objtypes.ConditionType(
    nodeId="ns=cas;i=5206",
    browseName="ns=cas;<Event>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10849", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10850", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10853", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10854", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10855", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10860", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10861", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10864", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10867", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10868", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10869", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10870", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10871", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10872", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=cas;i=9833"]),
        o6.hasComponent(o6.ns["ns=cas;i=10851"]),
        o6.hasComponent(o6.ns["ns=cas;i=10856"]),
        o6.hasComponent(o6.ns["ns=cas;i=10857"]),
        o6.hasComponent(o6.ns["ns=cas;i=10858"]),
        o6.hasComponent(o6.ns["ns=cas;i=10862"]),
        o6.hasComponent(o6.ns["ns=cas;i=10865"]),
    ],
    _allow_abstract=True,
)
cas_objtypes.EventsType(
    nodeId="ns=cas;i=5035",
    browseName="ns=cas;Events",
    description="Alarms and conditions of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5068"]),
        o6.hasComponent(o6.ns["ns=cas;i=5086"]),
        o6.hasComponent(o6.ns["ns=cas;i=5087"]),
        o6.hasComponent(o6.ns["ns=cas;i=5090"]),
        o6.hasComponent(o6.ns["ns=cas;i=5206"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=6548", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
o6.reference(cas_objtypes.CASComponentType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5035"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=11298",
    browseName="ns=cas;Dhcp",
    description="States if DHCP is enabled or disabled on the MCS.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11299", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("DHCP disabled"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11300", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("DHCP enabled"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11302", browseName="Definition", dataType=o6.String)),
    ],
    dataType=o6.Boolean,
)
o6.reference(cas_objtypes.CommunicationSettingsType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=11298"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=11304",
    browseName="ns=cas;Dhcp",
    description="States if DHCP is enabled or disabled on the MCS.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11305", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("DHCP disabled"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11306", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("DHCP enabled"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11327", browseName="Definition", dataType=o6.String)),
    ],
    dataType=o6.Boolean,
)
cas_objtypes.CommunicationSettingsType(
    nodeId="ns=cas;i=5026",
    browseName="ns=cas;CommunicationSettings",
    description="OPC UA communication settings of the MCS in a compressed air system.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6117", browseName="ns=cas;IpAddress", description="IP address of the MCS.", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6246", browseName="ns=cas;DomainName", description="Domain name the MCS is assigned to.", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=6247", browseName="ns=cas;Hostname", description="Host name of the MCS.", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=11303", browseName="ns=cas;DefaultGateway", description="IP Address of the default gateway used by the MCS.", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=11307", browseName="ns=cas;DnsServer", description="IP Address of the DNS server used by the MCS.", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=11308", browseName="ns=cas;IpVersion", description="Version of the internet protocol used for the MCS.", dataType=cas_datypes.IpVersionEnum
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11310", browseName="ns=cas;SubnetMask", description="Subnet mask of the MCS.", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=11304"]),
    ],
)
o6.reference(cas_objtypes.MCSConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5026"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=11312",
    browseName="ns=cas;Dhcp",
    description="States if DHCP is enabled or disabled on the MCS.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11313", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("DHCP disabled"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11314", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("DHCP enabled"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11328", browseName="Definition", dataType=o6.String)),
    ],
    dataType=o6.Boolean,
)
cas_objtypes.CommunicationSettingsType(
    nodeId="ns=cas;i=5071",
    browseName="ns=cas;CommunicationSettings",
    description="OPC UA communication settings of the MCS in a compressed air system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7868", browseName="ns=cas;IpAddress", description="IP address of the MCS.", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7869", browseName="ns=cas;DomainName", description="Domain name the MCS is assigned to.", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7870", browseName="ns=cas;Hostname", description="Host name of the MCS.", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=11311", browseName="ns=cas;DefaultGateway", description="IP Address of the default gateway used by the MCS.", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=11315", browseName="ns=cas;DnsServer", description="IP Address of the DNS server used by the MCS.", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=11316", browseName="ns=cas;IpVersion", description="Version of the internet protocol used for the MCS.", dataType=cas_datypes.IpVersionEnum
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11318", browseName="ns=cas;SubnetMask", description="Subnet mask of the MCS.", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=11312"]),
    ],
)
cas_objtypes.MCSConfigurationType(
    nodeId="ns=cas;i=5019",
    browseName="ns=di;Configuration",
    description="Configure the behavior of the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5071"]),
        o6.hasComponent(o6.ns["ns=cas;i=5125"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8066", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.call(nodeId="ns=cas;i=9928", browseName="ns=cas;LoadConfigurationFile", description="Loads the configuration stored in ConfigurationFile to the MCS.")),
        o6.hasComponent(
            o6.call(nodeId="ns=cas;i=10125", browseName="ns=cas;SaveConfigurationFile", description="Saves the current configuration of the MCS to the stored ConfigurationFile.")
        ),
    ],
)
o6.reference(cas_objtypes.MCSType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5019"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=cas;i=11320",
    browseName="ns=cas;Dhcp",
    description="States if DHCP is enabled or disabled on the MCS.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11321", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("No DHCP server expected"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11322", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("DHCP server expected"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11329", browseName="Definition", dataType=o6.String)),
    ],
    dataType=o6.Boolean,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=10226",
    browseName="ns=cas;RealTimeToNextService",
    description="Real time left until the sensor is scheduled for the next servicing.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=10306", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11331", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11332", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11333", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
cas_objtypes.MaintenanceType(
    nodeId="ns=cas;i=5149",
    browseName="ns=di;Maintenance",
    description="Servicing intervals for the sensor.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=cas;i=10224"]), o6.hasComponent(o6.ns["ns=cas;i=10226"])],
)
o6.reference(cas_objtypes.SensorType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5149"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=cas;i=6712",
    browseName="ns=cas;ContinuousPosition",
    description="Actual valve stroke.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7978", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=8149", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11340", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11341", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11342", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(cas_objtypes.ValveOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=6712"])
ns0.vartypes.DataItemType(
    nodeId="ns=cas;i=11343",
    browseName="ns=cas;PortUsed",
    description="Actual port used.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11344", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11345", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
o6.reference(cas_objtypes.ValveOperationalType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=11343"])


ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11347",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11346",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=11346", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=11347"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11349",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11348",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11350",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11348",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=11348", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=11349"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=11350"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11352",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11351",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11353",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11351",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=11351", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=11352"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=11353"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11356",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11355",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11357",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11355",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=11355", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=11356"]), outputArgs=o6.hasProperty(o6.ns["ns=cas;i=11357"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11359",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11358",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=11358", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=11359"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cas;i=11364",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cas;i=11363",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=cas;i=11363", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=cas;i=11364"]))

ns0.objtypes.FileType(
    nodeId="ns=cas;i=5027",
    browseName="ns=cas;<PrefabAnalysis>",
    description="Prefabricated analysis provided by the MCS.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11354", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11360", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11361", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11362", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11365", browseName="MimeType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=11346"]),
        o6.hasComponent(o6.ns["ns=cas;i=11348"]),
        o6.hasComponent(o6.ns["ns=cas;i=11351"]),
        o6.hasComponent(o6.ns["ns=cas;i=11355"]),
        o6.hasComponent(o6.ns["ns=cas;i=11358"]),
        o6.hasComponent(o6.ns["ns=cas;i=11363"]),
    ],
)
o6.reference(cas_objtypes.AnalysesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5027"])
ns0.objtypes.FileType(
    nodeId="ns=cas;i=5059",
    browseName="ns=cas;OutputFile",
    description="File containing the result of an analysis.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7908", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7914", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7915", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7916", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11366", browseName="MimeType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=7900"]),
        o6.hasComponent(o6.ns["ns=cas;i=7902"]),
        o6.hasComponent(o6.ns["ns=cas;i=7905"]),
        o6.hasComponent(o6.ns["ns=cas;i=7909"]),
        o6.hasComponent(o6.ns["ns=cas;i=7912"]),
        o6.hasComponent(o6.ns["ns=cas;i=7917"]),
    ],
)
o6.reference(cas_objtypes.AnalysisType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5059"])
ns0.objtypes.FileType(
    nodeId="ns=cas;i=5096",
    browseName="ns=cas;OutputFile",
    description="File containing the result of an analysis.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9757", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9763", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9764", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9765", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11367", browseName="MimeType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=7940"]),
        o6.hasComponent(o6.ns["ns=cas;i=7942"]),
        o6.hasComponent(o6.ns["ns=cas;i=8235"]),
        o6.hasComponent(o6.ns["ns=cas;i=9758"]),
        o6.hasComponent(o6.ns["ns=cas;i=9761"]),
        o6.hasComponent(o6.ns["ns=cas;i=9766"]),
    ],
)
cas_objtypes.AnalysisType(
    nodeId="ns=cas;i=5092",
    browseName="ns=cas;EnergyReportISO50001",
    description="Energy report according to ISO 50001.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5096"]),
        o6.hasComponent(o6.call(nodeId="ns=cas;i=7938", browseName="ns=cas;Trigger", description="Triggers the analysis on the MCS in a compressed air system.")),
    ],
)
o6.reference(cas_objtypes.AnalysesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5092"])
ns0.objtypes.FileType(
    nodeId="ns=cas;i=5094",
    browseName="ns=cas;OutputFile",
    description="File containing the result of an analysis.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7925", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7931", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7932", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=7933", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11368", browseName="MimeType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=7920"]),
        o6.hasComponent(o6.ns["ns=cas;i=7922"]),
        o6.hasComponent(o6.ns["ns=cas;i=7923"]),
        o6.hasComponent(o6.ns["ns=cas;i=7926"]),
        o6.hasComponent(o6.ns["ns=cas;i=7929"]),
        o6.hasComponent(o6.ns["ns=cas;i=7934"]),
    ],
)
cas_objtypes.AnalysisType(
    nodeId="ns=cas;i=5093",
    browseName="ns=cas;<Analysis>",
    description="Manufacturer or system specific analyses.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5094"]),
        o6.hasComponent(o6.call(nodeId="ns=cas;i=7936", browseName="ns=cas;Trigger", description="Triggers the analysis on the MCS in a compressed air system.")),
    ],
)
o6.reference(cas_objtypes.AnalysesType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5093"])
ns0.objtypes.FileType(
    nodeId="ns=cas;i=5120",
    browseName="ns=cas;OutputFile",
    description="File containing the result of an analysis.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9879", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9885", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9886", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9887", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11369", browseName="MimeType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=9871"]),
        o6.hasComponent(o6.ns["ns=cas;i=9873"]),
        o6.hasComponent(o6.ns["ns=cas;i=9876"]),
        o6.hasComponent(o6.ns["ns=cas;i=9880"]),
        o6.hasComponent(o6.ns["ns=cas;i=9883"]),
        o6.hasComponent(o6.ns["ns=cas;i=9888"]),
    ],
)
cas_objtypes.AnalysisType(
    nodeId="ns=cas;i=5112",
    browseName="ns=cas;EnergyReportISO50001",
    description="Energy report according to ISO 50001.",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5120"]),
        o6.hasComponent(o6.call(nodeId="ns=cas;i=9823", browseName="ns=cas;Trigger", description="Triggers the analysis on the MCS in a compressed air system.")),
    ],
)
cas_objtypes.AnalysesType(
    nodeId="ns=cas;i=5022",
    browseName="ns=cas;Analyses",
    description="Invokable analyses for the topology element.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5112"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8068", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
o6.reference(cas_objtypes.MCSType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5022"])
ns0.objtypes.FileType(
    nodeId="ns=cas;i=5121",
    browseName="ns=cas;OutputFile",
    description="File containing the result of an analysis.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9898", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9904", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9905", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=9906", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11372", browseName="MimeType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=9890"]),
        o6.hasComponent(o6.ns["ns=cas;i=9892"]),
        o6.hasComponent(o6.ns["ns=cas;i=9895"]),
        o6.hasComponent(o6.ns["ns=cas;i=9899"]),
        o6.hasComponent(o6.ns["ns=cas;i=9902"]),
        o6.hasComponent(o6.ns["ns=cas;i=9907"]),
    ],
)
cas_objtypes.AnalysisType(
    nodeId="ns=cas;i=5115",
    browseName="ns=cas;EnergyReportISO50001",
    description="Energy report according to ISO 50001.",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5121"]),
        o6.hasComponent(o6.call(nodeId="ns=cas;i=9829", browseName="ns=cas;Trigger", description="Triggers the analysis on the MCS in a compressed air system.")),
    ],
)
cas_objtypes.AnalysesType(
    nodeId="ns=cas;i=5701",
    browseName="ns=cas;Analyses",
    description="Invokable analyses for the topology element.",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5115"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8069", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
    ],
)
compressorZ = cas_objtypes.CASComponentType(
    nodeId="ns=cas;i=5414",
    browseName="ns=cas;CompressorZ",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=12503",
                browseName="ns=cas;ActiveAirnet",
                description="Indicates which airnet is currently using this component.",
                dataType=o6.NodeId,
                value=o6.NodeId("ns=cas;i=5392"),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=cas;i=5073"]),
        o6.hasComponent(o6.ns["ns=cas;i=5170"]),
        o6.hasComponent(cas_objtypes.ConfigurationType(nodeId="ns=cas;i=5415", browseName="ns=di;Configuration", description="Configure the behavior of the topology element.")),
    ],
)
cas_objtypes.CommunicationSettingsType(
    nodeId="ns=cas;i=5705",
    browseName="ns=cas;CommunicationSettings",
    description="OPC UA communication settings of the MCS in a compressed air system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=11319", browseName="ns=cas;DefaultGateway", description="IP Address of the default gateway used by the MCS.", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cas;i=11323", browseName="ns=cas;DnsServer", description="IP Address of the DNS server used by the MCS.", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cas;i=11324", browseName="ns=cas;IpVersion", description="Version of the internet protocol used for the MCS.", dataType=cas_datypes.IpVersionEnum
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=11326", browseName="ns=cas;SubnetMask", description="Subnet mask of the MCS.", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=18629", browseName="ns=cas;DomainName", description="Domain name the MCS is assigned to.", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=18630", browseName="ns=cas;Hostname", description="Host name of the MCS.", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cas;i=18631", browseName="ns=cas;IpAddress", description="IP address of the MCS.", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=cas;i=11320"]),
    ],
)
cas_objtypes.MCSConfigurationType(
    nodeId="ns=cas;i=5702",
    browseName="ns=di;Configuration",
    description="Configure the behavior of the topology element.",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5126"]),
        o6.hasComponent(o6.ns["ns=cas;i=5705"]),
        o6.hasComponent(
            di.vartypes.UIElementType(nodeId="ns=cas;i=8067", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True)
        ),
        o6.hasComponent(o6.call(nodeId="ns=cas;i=9949", browseName="ns=cas;LoadConfigurationFile", description="Loads the configuration stored in ConfigurationFile to the MCS.")),
        o6.hasComponent(
            o6.call(nodeId="ns=cas;i=10127", browseName="ns=cas;SaveConfigurationFile", description="Saves the current configuration of the MCS to the stored ConfigurationFile.")
        ),
    ],
)
cas_objtypes.MCSType(
    nodeId="ns=cas;i=5387",
    browseName="ns=cas;MCS",
    description="Representation of the MCS in a compressed air system.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=cas;i=5081"]),
        o6.hasComponent(o6.ns["ns=cas;i=5141"]),
        o6.hasComponent(o6.ns["ns=cas;i=5700"]),
        o6.hasComponent(o6.ns["ns=cas;i=5701"]),
        o6.hasComponent(o6.ns["ns=cas;i=5702"]),
        o6.hasComponent(o6.ns["ns=cas;i=5703"]),
        o6.hasComponent(o6.ns["ns=cas;i=5704"]),
    ],
)
o6.reference(cas_objtypes.CASType, ns0.reftypes.HasComponent, o6.ns["ns=cas;i=5387"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, cas_datypes, cas_objtypes
