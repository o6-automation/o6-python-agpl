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

"""Generated OPC UA ecm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0
from . import datatypes as ecm_datypes
from . import vartypes as ecm_vartypes
from . import objtypes as ecm_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5002", browseName="Default XML")
o6.hasEncoding(ecm_datypes.StandbyModeTransitionDataType, o6.ns["ns=ecm;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5003", browseName="Default JSON")
o6.hasEncoding(ecm_datypes.StandbyModeTransitionDataType, o6.ns["ns=ecm;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5005", browseName="Default XML")
o6.hasEncoding(ecm_datypes.EnergyStateInformationDataType, o6.ns["ns=ecm;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5006", browseName="Default JSON")
o6.hasEncoding(ecm_datypes.EnergyStateInformationDataType, o6.ns["ns=ecm;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5008", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5010", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5011", browseName="Default XML")
o6.hasEncoding(ecm_datypes.AcPeDataType, o6.ns["ns=ecm;i=5011"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5012", browseName="Default JSON")
o6.hasEncoding(ecm_datypes.AcPeDataType, o6.ns["ns=ecm;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5014", browseName="Default XML")
o6.hasEncoding(ecm_datypes.AcPpDataType, o6.ns["ns=ecm;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5015", browseName="Default JSON")
o6.hasEncoding(ecm_datypes.AcPpDataType, o6.ns["ns=ecm;i=5015"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5022", browseName="Default XML")
o6.hasEncoding(ecm_datypes.MeasurementPeriodDataType, o6.ns["ns=ecm;i=5022"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ecm;i=5023", browseName="Default JSON")
o6.hasEncoding(ecm_datypes.MeasurementPeriodDataType, o6.ns["ns=ecm;i=5023"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ecm;i=6005", browseName="ns=ecm;StandbyModeTransitionDataType", dataType=o6.String, value="StandbyModeTransitionDataType")
o6.reference(o6.ns["ns=ecm;i=5001"], "i=39", o6.ns["ns=ecm;i=6005"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ecm;i=6006", browseName="ns=ecm;StandbyModeTransitionDataType", dataType=o6.String, value="//xs:element[@name='StandbyModeTransitionDataType']"
)
o6.reference(o6.ns["ns=ecm;i=5002"], "i=39", o6.ns["ns=ecm;i=6006"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ecm;i=6007", browseName="ns=ecm;EnergyStateInformationDataType", dataType=o6.String, value="EnergyStateInformationDataType")
o6.reference(o6.ns["ns=ecm;i=5004"], "i=39", o6.ns["ns=ecm;i=6007"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ecm;i=6008", browseName="ns=ecm;EnergyStateInformationDataType", dataType=o6.String, value="//xs:element[@name='EnergyStateInformationDataType']"
)
o6.reference(o6.ns["ns=ecm;i=5005"], "i=39", o6.ns["ns=ecm;i=6008"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ecm;i=6011", browseName="ns=ecm;AcPeDataType", dataType=o6.String, value="AcPeDataType")
o6.reference(o6.ns["ns=ecm;i=5010"], "i=39", o6.ns["ns=ecm;i=6011"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ecm;i=6012", browseName="ns=ecm;AcPeDataType", dataType=o6.String, value="//xs:element[@name='AcPeDataType']")
o6.reference(o6.ns["ns=ecm;i=5011"], "i=39", o6.ns["ns=ecm;i=6012"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ecm;i=6013", browseName="ns=ecm;AcPpDataType", dataType=o6.String, value="AcPpDataType")
o6.reference(o6.ns["ns=ecm;i=5013"], "i=39", o6.ns["ns=ecm;i=6013"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ecm;i=6014", browseName="ns=ecm;AcPpDataType", dataType=o6.String, value="//xs:element[@name='AcPpDataType']")
o6.reference(o6.ns["ns=ecm;i=5014"], "i=39", o6.ns["ns=ecm;i=6014"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6032",
    browseName="ns=ecm;ModePowerConsumption",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6033", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(ecm_objtypes.EnergySavingModeType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6032"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6034",
    browseName="ns=ecm;EnergyConsumptionToPause",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6035", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(ecm_objtypes.EnergySavingModeType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6034"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6036",
    browseName="ns=ecm;EnergyConsumptionToOperate",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6037", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(ecm_objtypes.EnergySavingModeType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6036"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ecm;i=6016",
    browseName="ns=ecm;StandbyManagementStatus",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6038",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    o6.LocalizedText("Energy saving disabled"),
                    o6.LocalizedText("Power Off"),
                    o6.LocalizedText("Ready to operate"),
                    o6.LocalizedText("Moving to Energy Saving Mode"),
                    o6.LocalizedText("Energy saving mode"),
                    o6.LocalizedText("Moving to ready to operate"),
                    o6.LocalizedText("Moving to Sleep mode WOL"),
                    o6.LocalizedText("Sleep mode WOL"),
                    o6.LocalizedText("Wake up WOL"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(ecm_objtypes.EnergyStandbyManagementType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6016"])
ecm_objtypes.EnergySavingModeStatusType(
    nodeId="ns=ecm;i=5017",
    browseName="ns=ecm;EnergySavingModeStatus",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ecm;i=6039",
                browseName="ns=ecm;StateInformation",
                dataType=ecm_datypes.EnergyStateInformationDataType,
                value=ecm_datypes.EnergyStateInformationDataType(iDSource=0, iDDestination=0, regularTimeToOperate=0.0, modePowerConsumption=0.0),
            )
        )
    ],
)
o6.reference(ecm_objtypes.EnergyStandbyManagementType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=5017"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6020",
    browseName="ns=ecm;AccuracyClass",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6057", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6061", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
o6.reference(ecm_vartypes.EnergyMeasurementValueType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6020"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6065",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6069", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6073", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6077",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6083", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6087", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6091",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6095", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6103", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6017",
    browseName="ns=ecm;Resource",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6111",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[24],
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
                    ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("Hydraulic Oil")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6113", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_vartypes.EnergyMeasurementValueType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6017"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6122",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6125", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6128", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6131",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6134", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6137", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6141",
    browseName="ns=ecm;EnergyConsumptionToOperate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6142", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6143",
    browseName="ns=ecm;EnergyConsumptionToPause",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6145",
    browseName="ns=ecm;ModePowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6146", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6130",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6169",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6171", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6056",
    browseName="ns=ecm;<MeasurementValue>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6058", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6059",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6112", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6152", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=ecm;i=6065"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6130"]),
    ],
    valueRank=-2,
)
o6.reference(ecm_objtypes.EnergyMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6056"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6173",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6175",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6177", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6060",
    browseName="ns=ecm;AcCurrentPe",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6062", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6063",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4279632, displayName=o6.LocalizedText("A"), description=o6.LocalizedText("ampere")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6114", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6153", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1218)),
        o6.hasComponent(o6.ns["ns=ecm;i=6077"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6173"]),
    ],
    dataType=ecm_datypes.AcPeDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE0Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6060"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6179",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6181",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6183", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6064",
    browseName="ns=ecm;AcActivePowerTotal",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6066", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6067",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6154", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1412)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6170", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6091"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6179"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE1Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6064"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6185",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6187",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6189", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6068",
    browseName="ns=ecm;AcActivePowerTotal",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6070", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6071",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6155", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1412)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6172", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6122"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6185"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE2Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6068"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6191",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6193",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6195", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6072",
    browseName="ns=ecm;AcActiveEnergyTotalImportLp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6074", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6075",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6156", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1001)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6174", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6131"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6191"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE2Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6072"])
ecm_objtypes.EnergySavingModeType(
    nodeId="ns=ecm;i=5016",
    browseName="ns=ecm;<EnergySavingModes>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6140", browseName="ns=ecm;DynamicData", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6200", browseName="ns=ecm;ID", dataType=o6.Byte)),
        o6.hasComponent(o6.ns["ns=ecm;i=6141"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6143"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6145"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6147", browseName="ns=ecm;RegularTimeToOperate", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6148", browseName="ns=ecm;TimeMaxLengthOfStay", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6149", browseName="ns=ecm;TimeMinLengthOfStay", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6150", browseName="ns=ecm;TimeMinPause", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6151", browseName="ns=ecm;TimeToPause", dataType=ns0.datatypes.Duration)),
    ],
)
o6.reference(ecm_objtypes.EnergySavingModesContainerType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=5016"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6202",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6203", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6204", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6205",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6206", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6207", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6208",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6209", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6210", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6211",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6212", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6213", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6214",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6215", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6216", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6217",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6218", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6219", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6220",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6221", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6222", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6223",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6224", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6225", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6226",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6227", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6228", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6229",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6230", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6231", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6232",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6233", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6234", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6235",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6236", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6237", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6197",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6199",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6238", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6076",
    browseName="ns=ecm;AcActiveEnergyTotalExportLp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6078", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6079",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6157", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1004)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6176", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6197"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6202"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE2Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6076"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6239",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6240",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6241", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6080",
    browseName="ns=ecm;AcActivePowerPe",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6123", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6124",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6158", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1409)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6178", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6205"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6239"]),
    ],
    dataType=ecm_datypes.AcPeDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6080"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6242",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6243",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6244", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6081",
    browseName="ns=ecm;AcReactivePowerPe",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6132", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6133",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4469812, displayName=o6.LocalizedText("var"), description=o6.LocalizedText("var")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6159", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1618)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6180", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6208"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6242"]),
    ],
    dataType=ecm_datypes.AcPeDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6081"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6245",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6246",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6247", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6082",
    browseName="ns=ecm;AcActiveEnergyTotalImportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6084", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6085",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6160", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1002)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6182", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6211"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6245"]),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6082"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6248",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6249",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6250", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6086",
    browseName="ns=ecm;AcActiveEnergyTotalExportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6088", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6089",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6161", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1005)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6184", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6214"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6248"]),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6086"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6251",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6252",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6253", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6090",
    browseName="ns=ecm;AcReactiveEnergyTotalImportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6092", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6093",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://opcfoundation.org/UA/ECM/", unitId=1, displayName=o6.LocalizedText("var&#183;h"), description=o6.LocalizedText("volt ampere reactive hour")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6162", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1011)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6186", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6217"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6251"]),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6090"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6254",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6255",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6256", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6094",
    browseName="ns=ecm;AcReactiveEnergyTotalExportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6096", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6097",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://opcfoundation.org/UA/ECM/", unitId=1, displayName=o6.LocalizedText("var&#183;h"), description=o6.LocalizedText("volt ampere reactive hour")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6163", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1014)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6188", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6220"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6254"]),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6094"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6257",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6258",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6259", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6098",
    browseName="ns=ecm;AcVoltagePe",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6135", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6136",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5655636, displayName=o6.LocalizedText("V"), description=o6.LocalizedText("volt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6164", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1118)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6190", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6223"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6257"]),
    ],
    dataType=ecm_datypes.AcPeDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6098"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6260",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6261",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6262", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6099",
    browseName="ns=ecm;AcVoltagePp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6138", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6139",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5655636, displayName=o6.LocalizedText("V"), description=o6.LocalizedText("volt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6165", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1145)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6192", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6226"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6260"]),
    ],
    dataType=ecm_datypes.AcPpDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6099"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6263",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6264",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6265", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6100",
    browseName="ns=ecm;AcCurrentPe",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6126", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6127",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4279632, displayName=o6.LocalizedText("A"), description=o6.LocalizedText("ampere")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6166", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1218)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6194", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6229"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6263"]),
    ],
    dataType=ecm_datypes.AcPeDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6100"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6266",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6267",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6268", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6101",
    browseName="ns=ecm;AcPowerFactorPe",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6129", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6167", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1709)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6196", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6232"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6266"]),
    ],
    dataType=ecm_datypes.AcPeDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6101"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6269",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6270",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6271", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6102",
    browseName="ns=ecm;DcCurrent",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6104", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6105",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4279632, displayName=o6.LocalizedText("A"), description=o6.LocalizedText("ampere")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6168", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1033)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6198", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=ecm;i=6235"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6269"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileD0Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6102"])
aCCURACY_DOMAIN_PERCENT_FULL_SCALE = ecm_objtypes.AccuracyDomainType(
    nodeId="ns=ecm;i=5019",
    browseName="ns=ecm;ACCURACY_DOMAIN_PERCENT_FULL_SCALE",
    description="The accuracy is given as percent of the full-scale reading.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6272",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[16],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ACCURACY_CLASS_0"), description=o6.LocalizedText("reserved")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ACCURACY_CLASS_1"), description=o6.LocalizedText("0,01%")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ACCURACY_CLASS_2"), description=o6.LocalizedText("0,02%")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ACCURACY_CLASS_3"), description=o6.LocalizedText("0,05%")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ACCURACY_CLASS_4"), description=o6.LocalizedText("0,1%")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("ACCURACY_CLASS_5"), description=o6.LocalizedText("0,2%")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("ACCURACY_CLASS_6"), description=o6.LocalizedText("0,5%")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ACCURACY_CLASS_7"), description=o6.LocalizedText("1%")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ACCURACY_CLASS_8"), description=o6.LocalizedText("1,5%")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("ACCURACY_CLASS_9"), description=o6.LocalizedText("2%")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("ACCURACY_CLASS_10"), description=o6.LocalizedText("2,5%")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("ACCURACY_CLASS_11"), description=o6.LocalizedText("3%")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("ACCURACY_CLASS_12"), description=o6.LocalizedText("5%")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("ACCURACY_CLASS_13"), description=o6.LocalizedText("10%")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("ACCURACY_CLASS_14"), description=o6.LocalizedText("20%")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("ACCURACY_CLASS_15"), description=o6.LocalizedText(";20%")),
                ],
            )
        )
    ],
)
aCCURACY_DOMAIN_PERCENT_ACTUAL_READING = ecm_objtypes.AccuracyDomainType(
    nodeId="ns=ecm;i=5024",
    browseName="ns=ecm;ACCURACY_DOMAIN_PERCENT_ACTUAL_READING",
    description="The accuracy is given as percent of the actual reading.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6273",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[16],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ACCURACY_CLASS_0"), description=o6.LocalizedText("reserved")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ACCURACY_CLASS_1"), description=o6.LocalizedText("0,01%")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ACCURACY_CLASS_2"), description=o6.LocalizedText("0,02%")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ACCURACY_CLASS_3"), description=o6.LocalizedText("0,05%")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ACCURACY_CLASS_4"), description=o6.LocalizedText("0,1%")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("ACCURACY_CLASS_5"), description=o6.LocalizedText("0,2%")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("ACCURACY_CLASS_6"), description=o6.LocalizedText("0,5%")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ACCURACY_CLASS_7"), description=o6.LocalizedText("1%")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ACCURACY_CLASS_8"), description=o6.LocalizedText("1,5%")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("ACCURACY_CLASS_9"), description=o6.LocalizedText("2%")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("ACCURACY_CLASS_10"), description=o6.LocalizedText("2,5%")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("ACCURACY_CLASS_11"), description=o6.LocalizedText("3%")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("ACCURACY_CLASS_12"), description=o6.LocalizedText("5%")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("ACCURACY_CLASS_13"), description=o6.LocalizedText("10%")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("ACCURACY_CLASS_14"), description=o6.LocalizedText("20%")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("ACCURACY_CLASS_15"), description=o6.LocalizedText(";20%")),
                ],
            )
        )
    ],
)
aCCURACY_DOMAIN_IEC = ecm_objtypes.AccuracyDomainType(
    nodeId="ns=ecm;i=5027",
    browseName="ns=ecm;ACCURACY_DOMAIN_IEC",
    description="The accuracy is given according to IEC 61557-12.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6274",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[14],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ACCURACY_CLASS_0"), description=o6.LocalizedText("reserved")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ACCURACY_CLASS_1"), description=o6.LocalizedText("0,02")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ACCURACY_CLASS_2"), description=o6.LocalizedText("0,05")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ACCURACY_CLASS_3"), description=o6.LocalizedText("0,1")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ACCURACY_CLASS_4"), description=o6.LocalizedText("0,2")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("ACCURACY_CLASS_5"), description=o6.LocalizedText("0,5")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("ACCURACY_CLASS_6"), description=o6.LocalizedText("1")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ACCURACY_CLASS_7"), description=o6.LocalizedText("1,5")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ACCURACY_CLASS_8"), description=o6.LocalizedText("2")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("ACCURACY_CLASS_9"), description=o6.LocalizedText("2,5")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("ACCURACY_CLASS_10"), description=o6.LocalizedText("3")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("ACCURACY_CLASS_11"), description=o6.LocalizedText("5")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("ACCURACY_CLASS_12"), description=o6.LocalizedText("10")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("ACCURACY_CLASS_13"), description=o6.LocalizedText("20")),
                ],
            )
        )
    ],
)
aCCURACY_DOMAIN_EN = ecm_objtypes.AccuracyDomainType(
    nodeId="ns=ecm;i=5030",
    browseName="ns=ecm;ACCURACY_DOMAIN_EN",
    description="The accuracy is given as specified in the EN 50470-3.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6275",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ACCURACY_CLASS_0"), description=o6.LocalizedText("reserved")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ACCURACY_CLASS_1"), description=o6.LocalizedText("0,5")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ACCURACY_CLASS_2"), description=o6.LocalizedText("1,0")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ACCURACY_CLASS_3"), description=o6.LocalizedText("1,5")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ACCURACY_CLASS_4"), description=o6.LocalizedText("2,0")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("ACCURACY_CLASS_5"), description=o6.LocalizedText("2,5")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("ACCURACY_CLASS_6"), description=o6.LocalizedText("3,0")),
                ],
            )
        )
    ],
)
accuracyDomains = ns0.objtypes.FolderType(
    nodeId="ns=ecm;i=5009",
    browseName="ns=ecm;AccuracyDomains",
    references=[
        o6.organizes(aCCURACY_DOMAIN_PERCENT_FULL_SCALE),
        o6.organizes(aCCURACY_DOMAIN_PERCENT_ACTUAL_READING),
        o6.organizes(aCCURACY_DOMAIN_IEC),
        o6.organizes(aCCURACY_DOMAIN_EN),
    ],
    parent="i=2268",
    referenceType=ns0.reftypes.Organizes,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6279",
    browseName="ns=ecm;EnergyConsumptionToOperate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6280", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6281",
    browseName="ns=ecm;EnergyConsumptionToPause",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6282", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=ecm;i=6284",
    browseName="ns=ecm;ModePowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6285", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ecm_objtypes.EnergySavingModeType(
    nodeId="ns=ecm;i=5007",
    browseName="ns=ecm;EnergySavingModes",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6278", browseName="ns=ecm;DynamicData", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6283", browseName="ns=ecm;ID", dataType=o6.Byte)),
        o6.hasComponent(o6.ns["ns=ecm;i=6279"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6281"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6284"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6286", browseName="ns=ecm;RegularTimeToOperate", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6287", browseName="ns=ecm;TimeMaxLengthOfStay", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6288", browseName="ns=ecm;TimeMinLengthOfStay", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6289", browseName="ns=ecm;TimeMinPause", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6290", browseName="ns=ecm;TimeToPause", dataType=ns0.datatypes.Duration)),
    ],
)
ecm_objtypes.EnergySavingModesContainerType(
    nodeId="ns=ecm;i=5018", browseName="ns=ecm;EnergySavingModes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=ecm;i=5007"])]
)
o6.reference(ecm_objtypes.EnergyStandbyManagementType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=5018"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6292",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6293", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6294", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6296",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6297",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6298", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6300",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6301", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6302", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6304",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6305",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6306", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6308",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6309", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6310", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6312",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6313",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6314", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6316",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6317", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6318", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6320",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6321",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6322", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6324",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6325", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6326", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6328",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6329",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6330", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6332",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6333", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6334", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6336",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6337",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6338", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6340",
    browseName="ns=ecm;AccuracyClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6341", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6342", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=ecm;i=6344",
    browseName="ns=ecm;Resource",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6345",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6346", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    value=1,
    accessLevel=3,
    userAccessLevel=1,
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6291",
    browseName="ns=ecm;DcCurrent",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6295", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6347",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4279632, displayName=o6.LocalizedText("A"), description=o6.LocalizedText("ampere")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6348", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1033)),
        o6.hasComponent(o6.ns["ns=ecm;i=6292"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6296"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileD1Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6291"])
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6299",
    browseName="ns=ecm;DcVoltage",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6303", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6349",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5655636, displayName=o6.LocalizedText("V"), description=o6.LocalizedText("volt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6350", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1034)),
        o6.hasComponent(o6.ns["ns=ecm;i=6300"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6304"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileD1Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6299"])
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6307",
    browseName="ns=ecm;DcActivePower",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6311", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6351",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6352", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1032)),
        o6.hasComponent(o6.ns["ns=ecm;i=6308"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6312"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileD1Type, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=6307"])
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6315",
    browseName="ns=ecm;DcEnergyTotalImportLp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6319", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6353",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6354", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1022)),
        o6.hasComponent(o6.ns["ns=ecm;i=6316"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6320"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileD1Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6315"])
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6331",
    browseName="ns=ecm;DcElectricalCharge",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6335", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6355",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4279624,
                    displayName=o6.LocalizedText("A&#183;h"),
                    description=o6.LocalizedText("ampere hour"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6356", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1030)),
        o6.hasComponent(o6.ns["ns=ecm;i=6332"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6336"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileD1Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6331"])
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6339",
    browseName="ns=ecm;DcRelativeCharge",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6343", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6357",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6358", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1031)),
        o6.hasComponent(o6.ns["ns=ecm;i=6340"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6344"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileD1Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6339"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ecm;i=6359", browseName="ns=ecm;MeasurementPeriodDataType", dataType=o6.String, value="MeasurementPeriodDataType")
o6.reference(o6.ns["ns=ecm;i=5008"], "i=39", o6.ns["ns=ecm;i=6359"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ecm;i=6001",
    browseName="ns=ecm;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/ECM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ECM/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6276",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=ecm;i=6005"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6007"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6011"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6013"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6359"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:opc="http://opcfoundation.org/BinarySchema/" TargetNamespace="http://opcfoundation.org/UA/ECM/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ua="http://opcfoundation.org/UA/" DefaultByteOrder="LittleEndian" xmlns:tns="http://opcfoundation.org/UA/ECM/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType Name="AcPeDataType" BaseType="ua:ExtensionObject">\n  <opc:Field TypeName="opc:Float" Name="L1"/>\n  <opc:Field TypeName="opc:Float" Name="L2"/>\n  <opc:Field TypeName="opc:Float" Name="L3"/>\n </opc:StructuredType>\n <opc:StructuredType Name="AcPpDataType" BaseType="ua:ExtensionObject">\n  <opc:Field TypeName="opc:Float" Name="L1L2"/>\n  <opc:Field TypeName="opc:Float" Name="L2L3"/>\n  <opc:Field TypeName="opc:Float" Name="L3L1"/>\n </opc:StructuredType>\n <opc:StructuredType Name="EnergyStateInformationDataType" BaseType="ua:ExtensionObject">\n  <opc:Field TypeName="opc:Byte" Name="IDSource"/>\n  <opc:Field TypeName="opc:Byte" Name="IDDestination"/>\n  <opc:Field TypeName="opc:Double" Name="RegularTimeToOperate"/>\n  <opc:Field TypeName="opc:Float" Name="ModePowerConsumption"/>\n </opc:StructuredType>\n <opc:StructuredType Name="MeasurementPeriodDataType" BaseType="ua:ExtensionObject">\n  <opc:Field TypeName="opc:Double" Name="Duration"/>\n  <opc:Field TypeName="tns:MeasurementPeriodEnum" Name="Definition"/>\n </opc:StructuredType>\n <opc:StructuredType Name="StandbyModeTransitionDataType" BaseType="ua:ExtensionObject">\n  <opc:Field TypeName="opc:Byte" Name="IDDestination"/>\n  <opc:Field TypeName="opc:Double" Name="CurrentTimeToDestination"/>\n  <opc:Field TypeName="opc:Double" Name="CurrentTimeToOperate"/>\n  <opc:Field TypeName="opc:Float" Name="EnergyConsumptionToDestination"/>\n </opc:StructuredType>\n <opc:EnumeratedType Name="MeasurementPeriodEnum" LengthInBits="32">\n  <opc:EnumeratedValue Value="0" Name="SlidingDemand"/>\n  <opc:EnumeratedValue Value="1" Name="FixedBlockCompleted"/>\n  <opc:EnumeratedValue Value="2" Name="FixedBlockInstantaneous"/>\n  <opc:EnumeratedValue Value="3" Name="FixedBlockPredicted"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ecm;i=6360", browseName="ns=ecm;MeasurementPeriodDataType", dataType=o6.String, value="//xs:element[@name='MeasurementPeriodDataType']"
)
o6.reference(o6.ns["ns=ecm;i=5022"], "i=39", o6.ns["ns=ecm;i=6360"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ecm;i=6003",
    browseName="ns=ecm;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/ECM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6004", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ECM/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6277",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=ecm;i=6006"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6008"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6012"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6014"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6360"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema targetNamespace="http://opcfoundation.org/UA/ECM/Types.xsd" elementFormDefault="qualified" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/ECM/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="MeasurementPeriodEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="SlidingDemand_0"/>\n   <xs:enumeration value="FixedBlockCompleted_1"/>\n   <xs:enumeration value="FixedBlockInstantaneous_2"/>\n   <xs:enumeration value="FixedBlockPredicted_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="MeasurementPeriodEnum" type="tns:MeasurementPeriodEnum"/>\n <xs:complexType name="ListOfMeasurementPeriodEnum">\n  <xs:sequence>\n   <xs:element nillable="true" minOccurs="0" name="MeasurementPeriodEnum" type="tns:MeasurementPeriodEnum" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" name="ListOfMeasurementPeriodEnum" type="tns:ListOfMeasurementPeriodEnum"/>\n <xs:complexType name="AcPeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" name="L1" maxOccurs="1" type="xs:float"/>\n   <xs:element minOccurs="0" name="L2" maxOccurs="1" type="xs:float"/>\n   <xs:element minOccurs="0" name="L3" maxOccurs="1" type="xs:float"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="AcPeDataType" type="tns:AcPeDataType"/>\n <xs:complexType name="ListOfAcPeDataType">\n  <xs:sequence>\n   <xs:element nillable="true" minOccurs="0" name="AcPeDataType" type="tns:AcPeDataType" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" name="ListOfAcPeDataType" type="tns:ListOfAcPeDataType"/>\n <xs:complexType name="AcPpDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" name="L1L2" maxOccurs="1" type="xs:float"/>\n   <xs:element minOccurs="0" name="L2L3" maxOccurs="1" type="xs:float"/>\n   <xs:element minOccurs="0" name="L3L1" maxOccurs="1" type="xs:float"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="AcPpDataType" type="tns:AcPpDataType"/>\n <xs:complexType name="ListOfAcPpDataType">\n  <xs:sequence>\n   <xs:element nillable="true" minOccurs="0" name="AcPpDataType" type="tns:AcPpDataType" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" name="ListOfAcPpDataType" type="tns:ListOfAcPpDataType"/>\n <xs:complexType name="EnergyStateInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" name="IDSource" maxOccurs="1" type="xs:unsignedByte"/>\n   <xs:element minOccurs="0" name="IDDestination" maxOccurs="1" type="xs:unsignedByte"/>\n   <xs:element minOccurs="0" name="RegularTimeToOperate" maxOccurs="1" type="xs:double"/>\n   <xs:element minOccurs="0" name="ModePowerConsumption" maxOccurs="1" type="xs:float"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="EnergyStateInformationDataType" type="tns:EnergyStateInformationDataType"/>\n <xs:complexType name="ListOfEnergyStateInformationDataType">\n  <xs:sequence>\n   <xs:element nillable="true" minOccurs="0" name="EnergyStateInformationDataType" type="tns:EnergyStateInformationDataType" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" name="ListOfEnergyStateInformationDataType" type="tns:ListOfEnergyStateInformationDataType"/>\n <xs:complexType name="MeasurementPeriodDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" name="Duration" maxOccurs="1" type="xs:double"/>\n   <xs:element minOccurs="0" name="Definition" maxOccurs="1" type="tns:MeasurementPeriodEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="MeasurementPeriodDataType" type="tns:MeasurementPeriodDataType"/>\n <xs:complexType name="ListOfMeasurementPeriodDataType">\n  <xs:sequence>\n   <xs:element nillable="true" minOccurs="0" name="MeasurementPeriodDataType" type="tns:MeasurementPeriodDataType" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" name="ListOfMeasurementPeriodDataType" type="tns:ListOfMeasurementPeriodDataType"/>\n <xs:complexType name="StandbyModeTransitionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" name="IDDestination" maxOccurs="1" type="xs:unsignedByte"/>\n   <xs:element minOccurs="0" name="CurrentTimeToDestination" maxOccurs="1" type="xs:double"/>\n   <xs:element minOccurs="0" name="CurrentTimeToOperate" maxOccurs="1" type="xs:double"/>\n   <xs:element minOccurs="0" name="EnergyConsumptionToDestination" maxOccurs="1" type="xs:float"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="StandbyModeTransitionDataType" type="tns:StandbyModeTransitionDataType"/>\n <xs:complexType name="ListOfStandbyModeTransitionDataType">\n  <xs:sequence>\n   <xs:element nillable="true" minOccurs="0" name="StandbyModeTransitionDataType" type="tns:StandbyModeTransitionDataType" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" name="ListOfStandbyModeTransitionDataType" type="tns:ListOfStandbyModeTransitionDataType"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6361",
    browseName="EnumValues",
    parent="ns=ecm;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("SlidingDemand"), description=o6.LocalizedText("The measurement period is interpreted to consider the last measurement period.")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("FixedBlockCompleted"),
            description=o6.LocalizedText("The measurement period is interpreted to take the last completed measurement period aligned to the full hour."),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("FixedBlockInstantaneous"),
            description=o6.LocalizedText(
                "The measurement period is interpreted to take the current measurement period aligned to the full hour. That means, if for example only have of the measurement period has passed, only that half is considered."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("FixedBlockPredicted"),
            description=o6.LocalizedText(
                "The measurement period is interpreted to take the current measurement period aligned to the full hour and predicts the duration that has not been passed. That means, if for example only have of the measurement period has passed, the first half of the considered values is based on real measurements while the second half takes predicted values."
            ),
        ),
    ],
)
ecm_vartypes.EnergyMeasurementValueType(
    nodeId="ns=ecm;i=6323",
    browseName="ns=ecm;DcEnergyTotalExportLp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6327", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6362",
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
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6363", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16, value=1025)),
        o6.hasComponent(o6.ns["ns=ecm;i=6324"]),
        o6.hasComponent(o6.ns["ns=ecm;i=6328"]),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ecm_objtypes.IEnergyProfileD1Type, ia.reftypes.HasStatisticComponent, o6.ns["ns=ecm;i=6323"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashECMSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=ecm;i=5021",
    browseName="ns=ecm;http://opcfoundation.org/UA/ECM/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6115", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6116", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-09-01T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6117", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ECM/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6118", browseName="NamespaceVersion", dataType=o6.String, value="1.0.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6119", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ecm;i=6120", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6121", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6364", browseName="ModelVersion", dataType=ns0.datatypes.SemanticVersionString, value="1.0.1")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6041",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=ecm;i=7001", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6041"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=ecm;i=7002", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6042"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6044",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=ecm;i=7003", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6043"]), outputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6044"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6049",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=ecm;i=7004", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6049"]))

di.objtypes.LockingServicesType(
    nodeId="ns=ecm;i=5020",
    browseName="ns=di;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6045", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6046", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6047", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6048", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=ecm;i=7001"]),
        o6.hasComponent(o6.ns["ns=ecm;i=7002"]),
        o6.hasComponent(o6.ns["ns=ecm;i=7003"]),
        o6.hasComponent(o6.ns["ns=ecm;i=7004"]),
    ],
)
o6.reference(ecm_objtypes.EnergyStandbyManagementType, ns0.reftypes.HasComponent, o6.ns["ns=ecm;i=5020"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0, ecm_datypes, ecm_vartypes, ecm_objtypes
