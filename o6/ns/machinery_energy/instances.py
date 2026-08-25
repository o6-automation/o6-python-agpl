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

"""Generated OPC UA machinery_energy namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ecm as ecm
import o6.ns.ia as ia
import o6.ns.ns0 as ns0
from . import reftypes as machinery_energy_reftypes
from . import objtypes as machinery_energy_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6002",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6003", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6004", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6006",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6007",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[23],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Not specified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Natural Gas")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Compressed Air")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Steam, Saturated")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Steam, Superheated")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Chilled Water")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Hot Water")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Hot Hot Water")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Crude Oil")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Fuel Oil #2")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Fuel Oil #5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Fuel Oil #6")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Diesel Oil")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Gasoline")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Propane")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Biogas")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Coal, Anthracite")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Coal, Bituminous")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Coal, Sub-bituminous")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Coal, Lignite")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Tallow")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Cooling Lubricant")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6008", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6010",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6011", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6012", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6014",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6015",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[23],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Not specified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Natural Gas")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Compressed Air")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Steam, Saturated")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Steam, Superheated")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Chilled Water")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Hot Water")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Hot Hot Water")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Crude Oil")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Fuel Oil #2")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Fuel Oil #5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Fuel Oil #6")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Diesel Oil")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Gasoline")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Propane")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Biogas")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Coal, Anthracite")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Coal, Bituminous")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Coal, Sub-bituminous")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Coal, Lignite")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Tallow")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Cooling Lubricant")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6016", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ecm.vartypes.EnergyMeasurementValueType(
    nodeId="ns=machinery_energy;i=6009",
    browseName="ns=ecm;NeEnergyExportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6013", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6017",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5720146,
                    displayName=o6.LocalizedText("W&#183;h"),
                    description=o6.LocalizedText("watt hour"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6018", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=2005)),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6010"]),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6014"]),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_energy_objtypes.INonElectricalEnergyType, ia.reftypes.HasStatisticComponent, o6.ns["ns=machinery_energy;i=6009"])
ecm.vartypes.EnergyMeasurementValueType(
    nodeId="ns=machinery_energy;i=6001",
    browseName="ns=ecm;NeEnergyImportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6005", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6019",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5720146,
                    displayName=o6.LocalizedText("W&#183;h"),
                    description=o6.LocalizedText("watt hour"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6020", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=2002)),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6002"]),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6006"]),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_energy_objtypes.INonElectricalEnergyType, ia.reftypes.HasStatisticComponent, o6.ns["ns=machinery_energy;i=6001"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6022",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6023", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6024", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6026",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6027",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[23],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Not specified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Natural Gas")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Compressed Air")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Steam, Saturated")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Steam, Superheated")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Chilled Water")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Hot Water")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Hot Hot Water")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Crude Oil")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Fuel Oil #2")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Fuel Oil #5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Fuel Oil #6")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Diesel Oil")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Gasoline")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Propane")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Biogas")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Coal, Anthracite")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Coal, Bituminous")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Coal, Sub-bituminous")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Coal, Lignite")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Tallow")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Cooling Lubricant")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6028", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6030",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6031", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6032", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6034",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6035",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[23],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Not specified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Natural Gas")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Compressed Air")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Steam, Saturated")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Steam, Superheated")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Chilled Water")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Hot Water")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Hot Hot Water")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Crude Oil")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Fuel Oil #2")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Fuel Oil #5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Fuel Oil #6")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Diesel Oil")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Gasoline")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Propane")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Biogas")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Coal, Anthracite")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Coal, Bituminous")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Coal, Sub-bituminous")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Coal, Lignite")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Tallow")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Cooling Lubricant")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6036", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ecm.vartypes.EnergyMeasurementValueType(
    nodeId="ns=machinery_energy;i=6021",
    browseName="ns=ecm;Pressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6025", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6037",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5259596, displayName=o6.LocalizedText("Pa"), description=o6.LocalizedText("pascal")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6038", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=28683)),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6022"]),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6026"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_energy_objtypes.IBaseFlowType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_energy;i=6021"])
ecm.vartypes.EnergyMeasurementValueType(
    nodeId="ns=machinery_energy;i=6029",
    browseName="ns=ecm;Temperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6033", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6039", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=28684)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6040",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4932940, displayName=o6.LocalizedText("K"), description=o6.LocalizedText("kelvin")
                ),
            )
        ),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6030"]),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6034"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_energy_objtypes.IBaseFlowType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_energy;i=6029"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6042",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6043", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6044", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6046",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6047",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[23],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Not specified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Natural Gas")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Compressed Air")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Steam, Saturated")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Steam, Superheated")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Chilled Water")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Hot Water")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Hot Hot Water")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Crude Oil")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Fuel Oil #2")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Fuel Oil #5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Fuel Oil #6")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Diesel Oil")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Gasoline")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Propane")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Biogas")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Coal, Anthracite")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Coal, Bituminous")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Coal, Sub-bituminous")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Coal, Lignite")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Tallow")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Cooling Lubricant")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6048", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6050",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6051", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6052", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6054",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6055",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[23],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Not specified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Natural Gas")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Compressed Air")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Steam, Saturated")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Steam, Superheated")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Chilled Water")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Hot Water")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Hot Hot Water")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Crude Oil")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Fuel Oil #2")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Fuel Oil #5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Fuel Oil #6")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Diesel Oil")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Gasoline")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Propane")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Biogas")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Coal, Anthracite")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Coal, Bituminous")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Coal, Sub-bituminous")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Coal, Lignite")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Tallow")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Cooling Lubricant")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6056", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ecm.vartypes.EnergyMeasurementValueType(
    nodeId="ns=machinery_energy;i=6041",
    browseName="ns=ecm;Volume",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6045", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6057",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5067857,
                    displayName=o6.LocalizedText("m&#179;"),
                    description=o6.LocalizedText("cubic metre"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6058", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=28686)),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6042"]),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6046"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_energy_objtypes.IVolumeFlowType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_energy;i=6041"])
ecm.vartypes.EnergyMeasurementValueType(
    nodeId="ns=machinery_energy;i=6049",
    browseName="ns=ecm;VolumeFlowRate",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6053", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6059",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5067091,
                    displayName=o6.LocalizedText("m&#179;/s"),
                    description=o6.LocalizedText("cubic metre per second"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6060", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=2100)),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6050"]),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6054"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_energy_objtypes.IVolumeFlowType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_energy;i=6049"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6062",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6063", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6064", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6066",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6067",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[23],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Not specified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Natural Gas")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Compressed Air")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Steam, Saturated")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Steam, Superheated")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Chilled Water")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Hot Water")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Hot Hot Water")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Crude Oil")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Fuel Oil #2")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Fuel Oil #5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Fuel Oil #6")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Diesel Oil")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Gasoline")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Propane")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Biogas")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Coal, Anthracite")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Coal, Bituminous")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Coal, Sub-bituminous")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Coal, Lignite")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Tallow")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Cooling Lubricant")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6068", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6070",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6071", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6072", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_energy;i=6074",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6075",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[23],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Not specified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Electricity")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Natural Gas")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Compressed Air")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Steam, Saturated")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Steam, Superheated")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Chilled Water")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Hot Water")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Hot Hot Water")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Crude Oil")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Fuel Oil #2")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Fuel Oil #5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Fuel Oil #6")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Diesel Oil")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Gasoline")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Propane")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Biogas")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Coal, Anthracite")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Coal, Bituminous")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Coal, Sub-bituminous")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Coal, Lignite")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Tallow")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Cooling Lubricant")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6076", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ecm.vartypes.EnergyMeasurementValueType(
    nodeId="ns=machinery_energy;i=6069",
    browseName="ns=ecm;Mass",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6073", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6077",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4933453, displayName=o6.LocalizedText("kg"), description=o6.LocalizedText("kilogram")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6078", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=28685)),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6070"]),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6074"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_energy_objtypes.IMassFlowType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_energy;i=6069"])
ecm.vartypes.EnergyMeasurementValueType(
    nodeId="ns=machinery_energy;i=6061",
    browseName="ns=ecm;MassFlowRate",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6065", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6079",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4933459,
                    displayName=o6.LocalizedText("kg/s"),
                    description=o6.LocalizedText("kilogram per second"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6080", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=2101)),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6062"]),
        o6.hasComponent(o6.ns["ns=machinery_energy;i=6066"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_energy_objtypes.IMassFlowType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_energy;i=6061"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMachinerySlashEnergySlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=machinery_energy;i=5001",
    browseName="ns=machinery_energy;http://opcfoundation.org/UA/Machinery/Energy/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6081", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6082", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-11-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6083", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/Energy/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6084", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6085",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_energy;i=6086", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_energy;i=6087", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
electricity = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10001", browseName="ns=machinery_energy;Electricity")
compressedAir = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10002", browseName="ns=machinery_energy;CompressedAir")
coolingLubricant = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10003", browseName="ns=machinery_energy;CoolingLubricant")
naturalGas = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10004", browseName="ns=machinery_energy;NaturalGas")
steam_Saturated = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10005", browseName="ns=machinery_energy;Steam_Saturated")
steam_Superheated = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10006", browseName="ns=machinery_energy;Steam_Superheated")
chilledWater = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10007", browseName="ns=machinery_energy;ChilledWater")
hotWater = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10008", browseName="ns=machinery_energy;HotWater")
hotHotWater = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10009", browseName="ns=machinery_energy;HotHotWater")
crudeOil = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10010", browseName="ns=machinery_energy;CrudeOil")
fuelOil_2 = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10011", browseName="ns=machinery_energy;FuelOil_2")
fuelOil_5 = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10012", browseName="ns=machinery_energy;FuelOil_5")
fuelOil_6 = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10013", browseName="ns=machinery_energy;FuelOil_6")
dieselOil = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10014", browseName="ns=machinery_energy;DieselOil")
gasoline = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10015", browseName="ns=machinery_energy;Gasoline")
propane = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10016", browseName="ns=machinery_energy;Propane")
biogas = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10017", browseName="ns=machinery_energy;Biogas")
hydraulicOil = ns0.objtypes.FolderType(nodeId="ns=machinery_energy;i=10018", browseName="ns=machinery_energy;HydraulicOil")
main = ecm.objtypes.EnergyMeasurementType(nodeId="ns=machinery_energy;i=10019", browseName="ns=machinery_energy;Main")


del Any, TYPE_CHECKING, uuid, o6, di, ecm, ia, ns0, machinery_energy_reftypes, machinery_energy_objtypes
