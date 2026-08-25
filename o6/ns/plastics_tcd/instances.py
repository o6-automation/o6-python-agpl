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

"""Generated OPC UA plastics_tcd namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_tcd_datypes
from . import objtypes as plastics_tcd_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6001",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6002", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6019", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6020",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6021", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6022", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6032",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6033", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6034", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6003",
    browseName="ns=plastics_tcd;TemperatureMainLine",
    description="Actual temperature in the main line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6004", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6045", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6003"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6005",
    browseName="ns=plastics_tcd;TemperatureReturnLine",
    description="Actual temperature in the return line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6006", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6047", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6005"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6007",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6008", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6049", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6050",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6051", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6052", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6062",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6063", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6064", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6009",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6010", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6076",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6077", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6078", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6017",
    browseName="ns=plastics_tcd;ControlMode",
    description="Defines to which setpoint the external channel is controlled",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6018", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6084", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6017"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6097",
    browseName="ns=plastics_tcd;TemperatureMainLine",
    description="Actual temperature in the main line",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6046", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6098", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6099",
    browseName="ns=plastics_tcd;TemperatureReturnLine",
    description="Actual temperature in the return line",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6048", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6100", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6133",
    browseName="ns=plastics_tcd;Sink",
    description="Defines where the medium is to be emptied",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6134", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6135", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.MouldEvacuationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6133"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6136",
    browseName="ns=plastics_tcd;Mode",
    description="Defines how the medium is to be emptied",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6137", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6138", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.MouldEvacuationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6136"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6095",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6096", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6139", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6011",
    browseName="ns=plastics_tcd;PressureMainLine",
    description="Actual value of the pressure in the main line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6012", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6150", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6011"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6089",
    browseName="ns=plastics_tcd;PressureMainLine",
    description="Actual value of the pressure in the main line",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6090", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6151", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6013",
    browseName="ns=plastics_tcd;PressureReturnLine",
    description="Actual value of the pressure in the return line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6014", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6152", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6013"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6091",
    browseName="ns=plastics_tcd;PressureReturnLine",
    description="Actual value of the pressure in the return line",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6092", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6153", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6054",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6055", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6154", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6056",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6057", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6058",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6059", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6156", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6060",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6061", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6157", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6065",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6158", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6067",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6068", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6159", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6069",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6160", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6071",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6072", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6161", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6073",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6074", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6162", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6129",
    browseName="ns=plastics_tcd;TemperatureLimit",
    description="Temperature Limitation of the mould evacuation. TCD is cooled to this temperature first if necessary.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6130", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.MouldEvacuationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6129"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6131",
    browseName="ns=plastics_tcd;Time",
    description="Duration of the mould evacuation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6132", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6186",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.MouldEvacuationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6131"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6015",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6016", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6192", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6193",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6194", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6195", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6083",
    browseName="ns=plastics_tcd;ControlMode",
    description="Defines to which setpoint the external channel is controlled",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6202", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6203", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6204",
    browseName="ns=plastics_tcd;ActualValue",
    description="Actual value of external temperature sensor",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6189", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6205", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.ExternalSensorType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6204"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6207",
    browseName="ns=plastics_tcd;ThermocoupleType",
    description="Type of connected external temperature sensor",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6208", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6209", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.ExternalSensorType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6207"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6214",
    browseName="ns=plastics_tcd;InternalMeasuringPoint",
    description="Determines whether the temperature of the main or the return is to be controlled",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6215", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6216", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6214"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6249",
    browseName="ns=plastics_tcd;PumpControlMode",
    description="Defines to which setpoint or function the pump is controlled",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6250", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6251", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6249"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6252",
    browseName="ns=plastics_tcd;ActualValue",
    description="Actual value of external temperature sensor",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6190", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6253", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6254",
    browseName="ns=plastics_tcd;ThermocoupleType",
    description="Type of connected external temperature sensor",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6255", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6256", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_tcd_objtypes.ExternalChannelsType(
    nodeId="ns=plastics_tcd;i=5028",
    browseName="ns=plastics_tcd;ExternalChannels",
    description="Container for the external channel(s)",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6262", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5028"])
o6.reference(o6.ns["ns=plastics_tcd;i=5028"], "i=41", "i=2133")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6268",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6269", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6270", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6288",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6289", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6290", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6294",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6295", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6296", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6197",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6198", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6307", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6199",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6200", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6308", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6201",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6291", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6309", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6292",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6293", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6310", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6297",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6298", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6311", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6299",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6300", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6312", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6301",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6302", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6313", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6314",
    browseName="ns=plastics_tcd;Mode",
    description="Defines how the medium is to be emptied",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6315", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6316", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6317",
    browseName="ns=plastics_tcd;Sink",
    description="Defines where the medium is to be emptied",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6318", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6319", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6320",
    browseName="ns=plastics_tcd;TemperatureLimit",
    description="Temperature Limitation of the mould evacuation. TCD is cooled to this temperature first if necessary.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6184", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6321", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6322",
    browseName="ns=plastics_tcd;Time",
    description="Duration of the mould evacuation",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6187",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6323", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6303",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6304", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6324", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6305",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6306", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6325", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6024",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6025", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6326", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6026",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6027", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6327", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6028",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6029", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6328", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6030",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6031", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6329", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6035",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6036", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6037",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6038", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6331", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6039",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6040", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6332", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6041",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6042", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6333", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6043",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6044", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6334", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6339",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6341", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6342", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6352",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6353", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6354", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6367",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6368", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6369", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6383",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6384", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6385", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6217",
    browseName="ns=plastics_tcd;StandbyTemperature",
    description="The standby value temperature is approached with the Method ReduceToStandByOn. The TCD switches off.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6218", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6392", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6217"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6219",
    browseName="ns=plastics_tcd;SwitchingOffTemperature",
    description="Defines the temperature to which the TCD must be cooled down before it switches off",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6220", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6394", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6219"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6221",
    browseName="ns=plastics_tcd;TemperatureLimitation",
    description="This setpoint is for temperature limitation of the mould circuit e.g. to protect the connected tubes or the downstream water distribution system",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6222", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6396", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6221"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6223",
    browseName="ns=plastics_tcd;TemperatureMainLine",
    description="Actual temperature in the main line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6224", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6398", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6223"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6225",
    browseName="ns=plastics_tcd;TemperatureReturnLine",
    description="Actual temperature in the return line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6226", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6400", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6225"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6404",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6405", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6406", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6416",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6417", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6418", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6439",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6440", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6441", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6453",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6454", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6455", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6468",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6469", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6470", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6231",
    browseName="ns=plastics_tcd;PressureMainLine",
    description="Actual pressure in the main line (Pressure return line + pump pressure)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6232", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6480", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6231"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6483",
    browseName="ns=plastics_tcd;Mode",
    description="Defines how the medium is to be emptied",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6484", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6485", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6486",
    browseName="ns=plastics_tcd;Sink",
    description="Defines where the medium is to be emptied",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6487", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6488", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6233",
    browseName="ns=plastics_tcd;PressureReturnLine",
    description="Actual pressure in the return line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6234", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6489", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6233"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6490",
    browseName="ns=plastics_tcd;TemperatureLimit",
    description="Temperature Limitation of the mould evacuation. TCD is cooled to this temperature first if necessary.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6491", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6492", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6481",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6482", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6495", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6493",
    browseName="ns=plastics_tcd;Time",
    description="Duration of the mould evacuation",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6494",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6497", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
oPC40082_1 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_tcd;i=6504",
    browseName="ns=plastics_tcd;OPC40082_1",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/TCD/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6505",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/TCD/",
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/TCD/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/TCD/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="OperatingModeEnumeration">\n  <opc:Documentation>Actual operating mode of the TCD</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="READY_TO_OPERATE" Value="1"/>\n  <opc:EnumeratedValue Name="NORMAL_OPERATION" Value="2"/>\n  <opc:EnumeratedValue Name="LEAK_STOPPER" Value="3"/>\n  <opc:EnumeratedValue Name="MOULD_EVACUATION" Value="4"/>\n  <opc:EnumeratedValue Name="PRESSURE_RELIEF" Value="5"/>\n  <opc:EnumeratedValue Name="COOLING" Value="6"/>\n  <opc:EnumeratedValue Name="SAFETY_COOLING" Value="7"/>\n  <opc:EnumeratedValue Name="ECO" Value="8"/>\n  <opc:EnumeratedValue Name="BOOST" Value="9"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
oPC40082_1_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_tcd;i=6506",
    browseName="ns=plastics_tcd;OPC40082_1",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/TCD/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6507",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/TCD/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/TCD/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/TCD/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="OperatingModeEnumeration">\n  <xs:annotation>\n   <xs:documentation>Actual operating mode of the TCD</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="READY_TO_OPERATE_1"/>\n   <xs:enumeration value="NORMAL_OPERATION_2"/>\n   <xs:enumeration value="LEAK_STOPPER_3"/>\n   <xs:enumeration value="MOULD_EVACUATION_4"/>\n   <xs:enumeration value="PRESSURE_RELIEF_5"/>\n   <xs:enumeration value="COOLING_6"/>\n   <xs:enumeration value="SAFETY_COOLING_7"/>\n   <xs:enumeration value="ECO_8"/>\n   <xs:enumeration value="BOOST_9"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:OperatingModeEnumeration" name="OperatingModeEnumeration"/>\n <xs:complexType name="ListOfOperatingModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OperatingModeEnumeration" name="OperatingModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOperatingModeEnumeration" name="ListOfOperatingModeEnumeration" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6512",
    browseName="ns=plastics_tcd;HoursOfOperation",
    description="Actual hours of operation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6167",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4740434, displayName=o6.LocalizedText("h"), description=o6.LocalizedText("hour")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6513", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6512"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6514",
    browseName="ns=plastics_tcd;MaxTemperature",
    description="Defines the maximum working temperature of the TCD",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6173", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6515", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
    value=0,
)
o6.reference(plastics_tcd_objtypes.TCDSpecificationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6514"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6516",
    browseName="ns=plastics_tcd;PowerValue",
    description="Power value, defines the heating capacity of the TCD with the rated voltage",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6179",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6517", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.TCDSpecificationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6516"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6518",
    browseName="ns=plastics_tcd;ConnectedLoad",
    description="Connected load, defines the connections of the TCD (pump performance, heating capacity and performance of the remaining components)",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6168",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6519", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.TCDSpecificationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6518"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6520",
    browseName="ns=plastics_tcd;NominalFlowRate",
    description="Nominal flow rate, defines the maximum achievable flow rate of the TCD",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6175", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6521", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.TCDSpecificationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6520"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6522",
    browseName="ns=plastics_tcd;CoolingCapacity",
    description="Power value for cooling, defines the power value for cooling at temperature difference 60 K between cooling water and heat transfer medium",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6170",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6523", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(plastics_tcd_objtypes.TCDSpecificationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6522"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6230",
    browseName="ns=plastics_tcd;HoursOfOperation",
    description="Actual hours of operation",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6235", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6526",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4740434, displayName=o6.LocalizedText("h"), description=o6.LocalizedText("hour")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6530",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6531", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6532", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6538",
    browseName="ns=plastics_tcd;ConnectedLoad",
    description="Connected load, defines the connections of the TCD (pump performance, heating capacity and performance of the remaining components)",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6169",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6539", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6540",
    browseName="ns=plastics_tcd;MaxTemperature",
    description="Defines the maximum working temperature of the TCD",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6174", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6541", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6542",
    browseName="ns=plastics_tcd;NominalFlowRate",
    description="Nominal flow rate, defines the maximum achievable flow rate of the TCD",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6176", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6543", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6544",
    browseName="ns=plastics_tcd;PowerValue",
    description="Power value, defines the heating capacity of the TCD with the rated voltage",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6180",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6545", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6266",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6267", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6554", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6272",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6273", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6555", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6274",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6275", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6556", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6559",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6560", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6561", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6574",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6575", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6576", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6237",
    browseName="ns=plastics_tcd;ActualProcessPower",
    description="Actual calculated process performance (from the view of the TCD: heating = positive value, cooling = negative value)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6238", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6582",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6237"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6239",
    browseName="ns=plastics_tcd;ActualRegulationRatio",
    description="Actual Regulation Ratio (heating = positive value, cooling = negative value)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6240", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6584",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6239"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6241",
    browseName="ns=plastics_tcd;DelayTimeAfterCooling",
    description="Delay Time after cooling before switching off the TCD",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6242", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6586",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5065038,
                    displayName=o6.LocalizedText("min"),
                    description=o6.LocalizedText("minute [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6241"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6589",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6590", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6591", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6602",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6603", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6604", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6245",
    browseName="ns=plastics_tcd;ActualPumpSpeedRPM",
    description="Actual speed of the pump in revolutions per minute",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6246", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6616",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min&#8315;&#185;"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6245"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6614",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6615", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6617", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6247",
    browseName="ns=plastics_tcd;ActualPumpPower",
    description="Actual power of the pump in kW",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6248", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6618",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6247"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6335",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6336", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6635", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6344",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6345", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6636", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6346",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6347", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6637", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6348",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6349", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6638", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6350",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6351", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6639", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6355",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6356", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6640", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6357",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6358", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6641", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6359",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6360", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6642", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6361",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6362", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6643", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6363",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6364", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6644", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6365",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6553", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6645", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6606",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6607", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6646", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6608",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6609", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6647", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6610",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6611", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6648", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6612",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6613", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6649", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6619",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6620", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6650", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6621",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6622", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6651", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6623",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6624", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6652", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6625",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6626", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6653", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6627",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6628", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6654", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6656",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6657", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6658", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6080",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6081", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6665", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6085",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6086", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6666", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6087",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6088", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6667", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6093",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6094", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6668", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6140",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6141", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6669", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6142",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6143", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6670", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6144",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6145", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6671", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6146",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6147", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6672", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6148",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6149", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6673", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6181",
    browseName="ns=plastics_tcd;CoolingCapacity",
    description="Power value for cooling, defines the power value for cooling at temperature difference 60 K between cooling water and heat transfer medium",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6182", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6674",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
    ],
    dataType=o6.UInt32,
    value=0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6678",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6679", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6680", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6528",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6529", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6692",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6534",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6535", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6693", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6536",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6537", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6694", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6546",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6547", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6695", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6548",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6549", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6696", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6562",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6563", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6697", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6564",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6565", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6698", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6566",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6567", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6568",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6569", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6700", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6570",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6571", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6701", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6572",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6573", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6702",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6578",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6579", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6703", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6580",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6581", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6706", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6583",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6585", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6707", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6587",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6588", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6708", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6592",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6593", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6709", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6594",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6595", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6710", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6596",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6597", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6711", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6598",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6599", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6712", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6600",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6601", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6713", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6337",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6338", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6715", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6340",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6366", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6716", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6370",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6371", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6720", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6372",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6373", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6721", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6374",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6375", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6722", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6376",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6377", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6723", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6379",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6380", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6724", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6381",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6382", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6725", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6387",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6431", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6729", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6433",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6434", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6730", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6435",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6436", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6731", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6437",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6438", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6732", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6442",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6443", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6733", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6444",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6445", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6734", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6446",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6447", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6738", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6448",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6449", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6739", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6450",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6451", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6740", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6171",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6172", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6800", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6801",
    browseName="ns=plastics_tcd;ActualProcessPower",
    description="Actual calculated process performance (from the view of the TCD: heating = positive value, cooling = negative value)",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6123",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6802", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6803",
    browseName="ns=plastics_tcd;ActualPumpPower",
    description="Actual power of the pump in kW",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6124",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4937556, displayName=o6.LocalizedText("kW"), description=o6.LocalizedText("kilowatt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6804", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6805",
    browseName="ns=plastics_tcd;ActualPumpSpeedRPM",
    description="Actual speed of the pump in revolutions per minute",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6185",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min&#8315;&#185;"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6806", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6807",
    browseName="ns=plastics_tcd;ActualRegulationRatio",
    description="Actual Regulation Ratio (heating = positive value, cooling = negative value)",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6188",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6808", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6809",
    browseName="ns=plastics_tcd;DelayTimeAfterCooling",
    description="Delay Time after cooling before switching off the TCD",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6191",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5065038,
                    displayName=o6.LocalizedText("min"),
                    description=o6.LocalizedText("minute [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6810", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_tcd_objtypes.ExternalChannelsType(
    nodeId="ns=plastics_tcd;i=5051",
    browseName="ns=plastics_tcd;ExternalChannels",
    description="Container for the external channel(s)",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6811", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(o6.ns["ns=plastics_tcd;i=5051"], "i=41", "i=2133")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6814",
    browseName="ns=plastics_tcd;ThermocoupleType",
    description="Type of connected external temperature sensor",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6815", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6816", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6773",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6774", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6818", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6795",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6796", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6819", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6820",
    browseName="ns=plastics_tcd;InternalMeasuringPoint",
    description="Determines whether the temperature of the main or the return is to be controlled",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6821", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6822", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6117",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6118", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6823", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6735",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6736", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6824", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6825",
    browseName="ns=plastics_tcd;PressureMainLine",
    description="Actual pressure in the main line (Pressure return line + pump pressure)",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6704", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6826", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6827",
    browseName="ns=plastics_tcd;PressureReturnLine",
    description="Actual pressure in the return line",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6705", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6828", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6829",
    browseName="ns=plastics_tcd;PumpControlMode",
    description="Defines to which setpoint or function the pump is controlled",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6830", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6831", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6776",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6777", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6832", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6119",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6120", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6833", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6737",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6771", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6838", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6778",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6779", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6839", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6108",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6113", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6846", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6163",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6164", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6847", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6388",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6503", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6848", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6718",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6719", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6849", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6741",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6742", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6850", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6743",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6747", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6851", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6749",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6750", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6852", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6751",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6752", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6853", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6789",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6790", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6854", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6110",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6111", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6855", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6112",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6114", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6856", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6834",
    browseName="ns=plastics_tcd;StandbyTemperature",
    description="The standby value temperature is approached with the Method ReduceToStandByOn. The TCD switches off.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6835", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6857", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6836",
    browseName="ns=plastics_tcd;SwitchingOffTemperature",
    description="Defines the temperature to which the TCD must be cooled down before it switches off",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6837", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6858", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6165",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6166", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6859", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6726",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6727", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6860", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6728",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6762", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6861", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6764",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6765", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6862", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6767",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6768", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6863", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6286",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6287", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6864", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6393",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6395", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6865", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6397",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6399", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6866", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6401",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6425", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6867", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6432",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6452", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6868", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6456",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6457", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6869", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6458",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6459", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6870", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6460",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6461", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6871", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6462",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6463", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6872", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6464",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6465", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6873", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6466",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6467", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6874", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6472",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6473", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6875", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6474",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6475", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6876", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6476",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6477", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6877", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6478",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6479", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6878", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6496",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6498", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6879", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6499",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6500", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6880", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6501",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6502", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6881", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6508",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6524", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6882", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6525",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6527", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6883", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6402",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6403", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6884", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6408",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6409", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6885", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6410",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6411", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6886", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6412",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6413", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6887", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6414",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6415", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6888", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6419",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6420", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6889", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6421",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6422", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6890", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6423",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6424", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6891", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6426",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6427", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6892", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6840",
    browseName="ns=plastics_tcd;TemperatureLimitation",
    description="This setpoint is for temperature limitation of the mould circuit e.g. to protect the connected tubes or the downstream water distribution system",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6841", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6893", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6842",
    browseName="ns=plastics_tcd;TemperatureMainLine",
    description="Actual temperature in the main line",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6843", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6894", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6844",
    browseName="ns=plastics_tcd;TemperatureReturnLine",
    description="Actual temperature in the return line",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6845", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6895", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6812",
    browseName="ns=plastics_tcd;ActualValue",
    description="Actual value of external temperature sensor",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6813", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6896", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6428",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6429", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6897", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6430",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6655", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6898", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6660",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6661", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6899", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6662",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6663", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6900", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6664",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6675", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6901", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6676",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6677", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6902", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6681",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6682", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6903", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6683",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6684", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6904", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6685",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6686", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6905", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6687",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6688", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6906", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6689",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6690", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6907", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6758",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6759", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6910", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6911",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6912", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6913", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6915",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6916", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6917", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6918",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6919", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6920", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6921",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6922", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6923", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6924",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6925", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6926", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6927",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6928", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6929", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6930",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6931", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6932", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6933",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6934", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6935", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6936",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6937", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6938", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6939",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6940", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6941", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6942",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6943", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6944", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6760",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6761", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6945", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6946",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6947", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6948", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6950",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6951", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6952", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6953",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6954", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6955", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6956",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6957", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6958", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6959",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6960", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6961", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6962",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6963", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6964", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6965",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6966", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6967", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6968",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6969", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6970", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6971",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6972", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6973", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6974",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6975", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6976", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6977",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6978", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6979", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6753",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6754", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6980", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6981",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6982", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6983", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6985",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6986", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6987", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6988",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6989", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6990", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6991",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6992", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6993", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6994",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6995", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6996", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6997",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6998", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6999", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5011",
    browseName="ns=plastics_tcd;Cooling",
    description="Information on the maintenance status of the cooling",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6102",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6107",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6108"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6163"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6388"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7001", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.MaintenanceInformationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5011"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5013",
    browseName="ns=plastics_tcd;Fluid",
    description="Information on the maintenance status of the fluid",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6104",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6109",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6110"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6112"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6165"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7002", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.MaintenanceInformationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5013"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5010",
    browseName="ns=plastics_tcd;Heating",
    description="Information on the maintenance status of the heating",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6101",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6115",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6117"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6119"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6171"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7003", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.MaintenanceInformationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5010"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5016",
    browseName="ns=plastics_tcd;Heating",
    description="Information on the maintenance status of the heating",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6390",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6772",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6735"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6737"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6773"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7004", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5009",
    browseName="ns=plastics_tcd;Cooling",
    description="Information on the maintenance status of the cooling",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6105",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6717",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6718"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6741"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6743"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7005", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5015",
    browseName="ns=plastics_tcd;Fluid",
    description="Information on the maintenance status of the fluid",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6389",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6763",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6726"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6728"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6764"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7007", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_tcd;i=5007",
    browseName="ns=plastics_tcd;ClosedLoopControl",
    description="Settings for the closed loop control for the sensor",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6261",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6264",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6265",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7011",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7012", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_tcd_objtypes.LeakStopperType(
    nodeId="ns=plastics_tcd;i=5021",
    browseName="ns=plastics_tcd;LeakStopper",
    description="Used for switching the leak stopper mode",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7019", browseName="ns=plastics_tcd;Off", description="Deactivate the leak stopper mode")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7020", browseName="ns=plastics_tcd;On", description="Activate the leak stopper mode (emergency operation in case of leaks in the system)"
            )
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5021"])
plastics_tcd_objtypes.MouldEvacuationType(
    nodeId="ns=plastics_tcd;i=5022",
    browseName="ns=plastics_tcd;MouldEvacuation",
    description="Iincludes parameters and nodes for mould evacuation",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6314"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6317"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6320"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6322"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7021", browseName="ns=plastics_tcd;Off", description="Deactivate evacuation mode")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7022", browseName="ns=plastics_tcd;On", description="Activate evacuation mode")),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5022"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5029",
    browseName="ns=plastics_tcd;FlowRate",
    description="Setting and/or monitoring of the flow rate",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6271",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6266"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6268"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6272"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6274"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6337"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6340"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6367"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6370"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6372"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6374"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6376"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6379"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7024",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5029"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5019",
    browseName="ns=plastics_tcd;Cooling",
    description="Information on the maintenance status of the cooling",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6106",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6748",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6749"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6751"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6789"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7025", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_tcd;i=6213",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_tcd;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DateTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="TimeZoneOffset", dataType=ns0.datatypes.TimeZoneDataType, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_tcd;i=7026",
    browseName="ns=plastics_rubber;SetMachineTime",
    description="Method for setting the server time together with TimeZoneOffset",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_tcd;i=6213"]),
)

plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_tcd;i=5014",
    browseName="ns=plastics_tcd;ClosedLoopControl",
    description="Settings for the closed loop control for the sensor",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6211",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6236",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6243",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7023",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7027", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
o6.reference(plastics_tcd_objtypes.ExternalSensorType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5014"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_tcd;i=5018",
    browseName="ns=plastics_tcd;ClosedLoopControl",
    description="Settings for the closed loop control for the sensor",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6244",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6258",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6259",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7028",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7029", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5025",
    browseName="ns=plastics_tcd;Heating",
    description="Information on the maintenance status of the heating",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6775",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6794",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6776"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6778"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6795"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7031", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_tcd;i=6229",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_tcd;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VisualisationUnit", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_tcd;i=6282",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_tcd;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_tcd;i=7032",
    browseName="ns=plastics_rubber;GetCurrentPage",
    description="Method for retrieving a screenshot of the control system with the currently shown contents",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_tcd;i=6229"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_tcd;i=6282"]),
)

plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5030",
    browseName="ns=plastics_tcd;PressureDifference",
    description="Setting and/or monitoring of the pressure difference between main and return line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6378",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6286"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6288"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6393"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6397"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6401"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6432"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6453"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6456"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6458"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6460"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6462"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6464"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7034",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5030"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5032",
    browseName="ns=plastics_tcd;PumpSpeed",
    description="Setting and/or monitoring the speed of the pump in percent of maximum speed",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6533",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6528"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6530"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6534"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6536"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6546"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6548"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6559"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6562"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6564"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6566"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6568"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6570"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7035",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5032"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5027",
    browseName="ns=plastics_tcd;TemperatureDifference",
    description="Setting and/or monitoring of the temperature difference between return and main line. Positive if temperature in return line is higher than in main line.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6407",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6402"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6404"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6408"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6410"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6412"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6414"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6416"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6419"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6421"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6423"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6426"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6428"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7036",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5027"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5041",
    browseName="ns=plastics_tcd;Temperature",
    description="Setting and/or monitoring of the temperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6914", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6758"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6911"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6915"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6918"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6921"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6924"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6927"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6930"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6933"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6936"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6939"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6942"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7041", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5042",
    browseName="ns=plastics_tcd;TemperatureDifference",
    description="Setting and/or monitoring of the temperature difference between return and main line. Positive if temperature in return line is higher than in main line.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6949", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6760"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6946"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6950"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6953"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6956"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6959"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6962"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6965"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6968"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6971"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6974"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6977"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7042", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_tcd;i=6283",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_tcd;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_tcd;i=6284",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_tcd;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_tcd;i=7049",
    browseName="ns=plastics_rubber;GetPage",
    description="Method for retrieving the image of a page of the control system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_tcd;i=6283"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_tcd;i=6284"]),
)

plastics_rubber.objtypes.MachineConfigurationType(
    nodeId="ns=plastics_tcd;i=5049",
    browseName="ns=plastics_tcd;MachineConfiguration",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6212",
                browseName="ns=plastics_rubber;LocationName",
                description="Description of the location of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6227",
                browseName="ns=plastics_rubber;TimeZoneOffset",
                description="Difference of the local time to Coordinated Universal Time (UTC) given by the machine operator or OPC client",
                dataType=ns0.datatypes.TimeZoneDataType,
                value=ns0.datatypes.TimeZoneDataType(offset=0, daylightSavingInOffset=False),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6228",
                browseName="ns=plastics_rubber;UserMachineName",
                description="Description of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6285",
                browseName="ns=plastics_rubber;PageDirectory",
                description="List of the pages that are implemented in the machine control system and are shown on the screen of the machine",
                dataType=plastics_rubber.datatypes.PageEntryDataType,
                valueRank=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7026"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7032"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7049"]),
    ],
)
o6.reference(plastics_tcd_objtypes.TCD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5049"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5057",
    browseName="ns=plastics_tcd;PressureDifference",
    description="Setting and/or monitoring of the pressure difference between main and return line",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6471",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6466"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6468"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6472"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6474"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6476"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6478"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6481"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6496"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6499"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6501"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6508"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6525"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7052",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5053",
    browseName="ns=plastics_tcd;FlowRate",
    description="Setting and/or monitoring of the flow rate",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6386",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6381"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6383"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6387"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6433"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6435"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6437"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6439"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6442"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6444"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6446"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6448"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6450"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7053",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5058",
    browseName="ns=plastics_tcd;PumpSpeed",
    description="Setting and/or monitoring the speed of the pump in percent of maximum speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6577",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6572"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6574"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6578"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6580"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6583"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6587"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6589"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6592"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6594"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6596"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6598"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6600"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7054",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7000",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7058", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7060", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5059",
    browseName="ns=plastics_tcd;TemperatureDifference",
    description="Setting and/or monitoring of the temperature difference between return and main line. Positive if temperature in return line is higher than in main line.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6659",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6430"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6656"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6660"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6662"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6664"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6676"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6678"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6681"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6683"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6685"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6687"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6689"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7061",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5003",
    browseName="ns=plastics_tcd;FlowRate",
    description="Setting and/or monitoring of the flow rate",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6079", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6009"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6076"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6080"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6085"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6087"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6093"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6095"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6140"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6142"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6144"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6146"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6148"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7062", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5003"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5004",
    browseName="ns=plastics_tcd;PressureDifference",
    description="Setting and/or monitoring of the pressure difference between main and return line",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6196", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6015"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6193"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6197"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6199"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6201"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6292"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6294"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6297"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6299"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6301"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6303"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6305"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7063", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5004"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5001",
    browseName="ns=plastics_tcd;Temperature",
    description="Setting and/or monitoring of the temperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6023", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6001"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6020"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6024"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6026"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6028"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6030"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6032"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6035"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6037"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6039"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6041"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6043"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7064", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5001"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5002",
    browseName="ns=plastics_tcd;TemperatureDifference",
    description="Setting and/or monitoring of the temperature difference between return and main line. Positive if temperature in return line is higher than in main line.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6053", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6007"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6050"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6054"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6056"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6058"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6060"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6062"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6065"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6067"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6069"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6071"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6073"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7065", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_tcd_objtypes.ExternalChannelType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5002"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_tcd;i=5008",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6629",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6630",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6631",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7059",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7070", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_tcd;i=5006",
    browseName="ns=plastics_tcd;Temperature",
    description="Setting and/or monitoring of the temperature in the main or return line (see InternalMeasuringPoint) or active external Sensor (ExternalSensorModeOn)",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6343",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5008"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6335"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6339"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6344"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6346"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6348"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6350"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6352"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6355"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6357"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6359"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6361"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6363"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7055",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5006"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_tcd;i=5031",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6632",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6633",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6634",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7071",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7072", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_tcd;i=5045",
    browseName="ns=plastics_tcd;Temperature",
    description="Setting and/or monitoring of the temperature in the main or return line (see InternalMeasuringPoint) or active external Sensor (ExternalSensorModeOn)",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6605",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5031"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6365"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6602"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6606"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6608"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6610"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6612"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6614"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6619"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6621"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6623"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6625"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6627"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7056",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_tcd_objtypes.LeakStopperType(
    nodeId="ns=plastics_tcd;i=5054",
    browseName="ns=plastics_tcd;LeakStopper",
    description="Used for switching the leak stopper mode",
    references=[
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7075", browseName="ns=plastics_tcd;Off", description="Deactivate the leak stopper mode")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7076", browseName="ns=plastics_tcd;On", description="Activate the leak stopper mode (emergency operation in case of leaks in the system)"
            )
        ),
    ],
)
plastics_tcd_objtypes.MouldEvacuationType(
    nodeId="ns=plastics_tcd;i=5056",
    browseName="ns=plastics_tcd;MouldEvacuation",
    description="Iincludes parameters and nodes for mould evacuation",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6483"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6486"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6490"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6493"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7077", browseName="ns=plastics_tcd;Off", description="Deactivate evacuation mode")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7078", browseName="ns=plastics_tcd;On", description="Activate evacuation mode")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7079",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7080", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7081", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7082",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7083", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7084", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7085",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7086", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7087", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7088",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7089", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7090", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5039",
    browseName="ns=plastics_tcd;FlowRate",
    description="Setting and/or monitoring of the flow rate",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6984", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6753"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6981"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6985"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6988"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6991"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6994"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6997"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7000"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7057", browseName="ns=plastics_rubber;ResetMonitoring")),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7079"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7082"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7085"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7088"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6755",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6756", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7091", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=7092",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7093", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7094", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7096",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7097", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7098", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7099",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7100", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7101", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7102",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7103", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7104", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7105",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7106", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7107", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=7108",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7109", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7110", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7112",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7114", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7115",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7116", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7117", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7118",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7119", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7120", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7121",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7122", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7123", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=7124",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7125", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7126", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_tcd;i=5040",
    browseName="ns=plastics_tcd;PressureDifference",
    description="Setting and/or monitoring of the pressure difference between main and return line",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=7095", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6755"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7092"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7096"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7099"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7102"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7105"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7108"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7111", browseName="ns=plastics_rubber;ResetMonitoring")),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7112"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7115"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7118"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7121"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7124"]),
    ],
)
plastics_tcd_objtypes.ExternalChannelType(
    nodeId="ns=plastics_tcd;i=5005",
    browseName="ns=plastics_tcd;ExternalChannel_<Nr>",
    description="Includes information for monitoring or controlling of an external temperature, flow rate or pressure channel",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6757",
                browseName="ns=plastics_tcd;SwitchedOn",
                description="Information if the external channel is switched on",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5039"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5040"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5041"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5042"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6083"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6089"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6091"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6097"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6099"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7068", browseName="ns=plastics_tcd;SwitchOff", description="Switch method of the external channel for switching off")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7069", browseName="ns=plastics_tcd;SwitchOn", description="Switch method of the external channel for switching on")),
    ],
)
o6.reference(plastics_tcd_objtypes.ExternalChannelsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5005"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_tcd;i=6714",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_tcd;i=7128",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Id of the error, listed in ActiveErrors, that shall be reset"))],
)
o6.call(nodeId="ns=plastics_tcd;i=7128", browseName="ns=plastics_tcd;ResetErrorById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_tcd;i=6714"]))

plastics_tcd_objtypes.OperationType(
    nodeId="ns=plastics_tcd;i=5050",
    browseName="ns=plastics_tcd;Operation",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6122",
                browseName="ns=plastics_tcd;HighestActiveAlarmSeverity",
                description="Indication of the severity of the highest active alarm (0 = no active alarm – 1000 = possible error)",
                dataType=o6.UInt16,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6550",
                browseName="ns=plastics_tcd;DeviceMappingNumber",
                description="Unique identifier/address/number for devices of the same DeviceType within a local network",
                dataType=o6.UInt32,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6552",
                browseName="ns=plastics_tcd;OperatingMode",
                description="Actual operating mode of the TCD",
                dataType=plastics_tcd_datypes.OperatingModeEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6230"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_tcd;i=6691",
                browseName="ns=plastics_tcd;ActiveErrors",
                description="List of the active errors of the device",
                dataType=plastics_rubber.datatypes.ActiveErrorDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7037", browseName="ns=plastics_tcd;ResetAllErrors", description="Method to reset all errors of the device")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7038",
                browseName="ns=plastics_tcd;IdentifyDevice",
                description="The TCD on which this method is called shows itself by e.g. activation of a LED",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7039",
                browseName="ns=plastics_tcd;ReduceToStandByOff",
                description="Deactivate the cooling down function on the TCD. If it is already in progress, it will be interrupted and the device changes back to the last selected operating mode.",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7040",
                browseName="ns=plastics_tcd;ReduceToStandByOn",
                description="Activate the cooling down function on the TCD followed by switching off",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7050", browseName="ns=plastics_tcd;SwitchOff", description="Main switch method of the TCD for switching off")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7051", browseName="ns=plastics_tcd;SwitchOn", description="Main switch method of the TCD for switching on")),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7128"]),
    ],
)
o6.reference(plastics_tcd_objtypes.TCD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5050"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=6908",
    browseName="ns=plastics_tcd;CommunicationProtocolType",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7129", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7130", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_tcd_objtypes.ExternalSensorType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=6908"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=7131",
    browseName="ns=plastics_tcd;CommunicationProtocolType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7132", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7133", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_tcd_objtypes.ExternalSensorType(
    nodeId="ns=plastics_tcd;i=5020",
    browseName="ns=plastics_tcd;ExternalSensor",
    description="Variables for the operation with an external temperature sensor",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6257",
                browseName="ns=plastics_tcd;Used",
                description="Return whether an external temperature sensor is used for control",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6263",
                browseName="ns=plastics_tcd;AutomaticModeSwitch",
                description="Setting whether switching to external sensor is performed automatically (TRUE) or manually (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5018"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6252"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6254"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7017",
                browseName="ns=plastics_tcd;ExternalSensorModeOff",
                description="Deactivate the mode where the external temperature sensor is used for temperature control",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7018",
                browseName="ns=plastics_tcd;ExternalSensorModeOn",
                description="Activate the mode where the external temperature sensor is used for temperature control",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7131"]),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5020"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_tcd;i=7134",
    browseName="ns=plastics_tcd;CommunicationProtocolType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7135", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7136", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_tcd_objtypes.ExternalSensorType(
    nodeId="ns=plastics_tcd;i=5052",
    browseName="ns=plastics_tcd;ExternalSensor",
    description="Variables for the operation with an external temperature sensor",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6260",
                browseName="ns=plastics_tcd;AutomaticModeSwitch",
                description="Setting whether switching to external sensor is performed automatically (TRUE) or manually (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6817",
                browseName="ns=plastics_tcd;Used",
                description="Return whether an external temperature sensor is used for control",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5007"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6812"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6814"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7073",
                browseName="ns=plastics_tcd;ExternalSensorModeOff",
                description="Deactivate the mode where the external temperature sensor is used for temperature control",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_tcd;i=7074",
                browseName="ns=plastics_tcd;ExternalSensorModeOn",
                description="Activate the mode where the external temperature sensor is used for temperature control",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=7134"]),
    ],
)
plastics_tcd_objtypes.TCDSpecificationType(
    nodeId="ns=plastics_tcd;i=5048",
    browseName="ns=plastics_tcd;TCDSpecification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7139", browseName="ns=plastics_tcd;DeviceZoneId", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6181"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6538"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6540"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6542"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6544"]),
    ],
)
o6.reference(plastics_tcd_objtypes.TCD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5048"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashTCDSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_tcd;i=5033",
    browseName="ns=plastics_tcd;http://opcfoundation.org/UA/PlasticsRubber/TCD/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7140", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7141", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2020-06-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7142", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/TCD/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7143", browseName="NamespaceVersion", dataType=o6.String, value="1.01")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=7144",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7145", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7146", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_tcd;i=7147",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_tcd;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Operating mode of the TCD is unknown")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("READY_TO_OPERATE"), description=o6.LocalizedText("TCD is ready to operate (heating, pump and cooling are switched off)")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("NORMAL_OPERATION"), description=o6.LocalizedText("TCD is running in normal operating mode")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("LEAK_STOPPER"), description=o6.LocalizedText("TCD is running in leak stopper operating mode")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("MOULD_EVACUATION"), description=o6.LocalizedText("TCD is carrying out a mould evacuation process")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("PRESSURE_RELIEF"), description=o6.LocalizedText("TCD is carrying out a pressure relief process")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("COOLING"), description=o6.LocalizedText("TCD is cooling down to StandbyTemperature and switch off")),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("SAFETY_COOLING"), description=o6.LocalizedText("TCD is cooling down to SwitchingOffTemperature and switch off")
        ),
        ns0.datatypes.EnumValueType(
            value=8, displayName=o6.LocalizedText("ECO"), description=o6.LocalizedText("TCD is running in Eco operating mode (energy is saved via the reduced pump speed)")
        ),
        ns0.datatypes.EnumValueType(
            value=9, displayName=o6.LocalizedText("BOOST"), description=o6.LocalizedText("TCD is running in Boost operating mode (pump runs at maximum possible speed)")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6769",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6770", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7148", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6792",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6793", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7149", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5024",
    browseName="ns=plastics_tcd;Fluid",
    description="Information on the maintenance status of the fluid",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6766",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6791",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6767"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6769"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6792"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7030", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6125",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6126", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7150", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6127",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6128", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7151", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6177",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6178", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7152", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5012",
    browseName="ns=plastics_tcd;Pump",
    description="Information on the maintenance status of the pump",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6103",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6116",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6125"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6127"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6177"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7006", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.MaintenanceInformationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5012"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6744",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6745", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7153", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6746",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6780", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7154", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6782",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6783", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5017",
    browseName="ns=plastics_tcd;Pump",
    description="Information on the maintenance status of the pump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6391",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6781",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6744"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6746"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6782"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7010", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_tcd_objtypes.MaintenanceInformationType(
    nodeId="ns=plastics_tcd;i=5023",
    browseName="ns=plastics_tcd;MaintenanceInformation",
    description="Information on the maintenance status of heating, cooling, pump and fluid",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5009"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5015"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5016"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5017"]),
    ],
)
o6.reference(plastics_tcd_objtypes.DeviceZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5023"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6785",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6786", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7156", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6787",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6788", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7157", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_tcd;i=6798",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6799", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7158", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_tcd;i=5026",
    browseName="ns=plastics_tcd;Pump",
    description="Information on the maintenance status of the pump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6784",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6797",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6785"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6787"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6798"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_tcd;i=7033", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_tcd_objtypes.MaintenanceInformationType(
    nodeId="ns=plastics_tcd;i=5055",
    browseName="ns=plastics_tcd;MaintenanceInformation",
    description="Information on the maintenance status of heating, cooling, pump and fluid",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5019"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5024"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5025"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5026"]),
    ],
)
plastics_tcd_objtypes.DeviceZoneType(
    nodeId="ns=plastics_tcd;i=5044",
    browseName="ns=plastics_tcd;DeviceZone",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5045"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5051"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5052"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5053"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5054"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5055"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5056"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5057"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5058"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=5059"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6801"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6803"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6805"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6807"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6809"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6820"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6825"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6827"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6829"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6834"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6836"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6840"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6842"]),
        o6.hasComponent(o6.ns["ns=plastics_tcd;i=6844"]),
    ],
)
o6.reference(plastics_tcd_objtypes.TCD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5044"])
plastics_rubber.objtypes.IdentificationType(
    nodeId="ns=plastics_tcd;i=5047",
    browseName="ns=plastics_tcd;Identification",
    description="Identification of the device",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6276",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose a certain device is used",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6277", browseName="ns=di;Manufacturer", description="Provides the name of the manufacturer of the machine", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6278", browseName="ns=di;Model", description="Represents the name of the machine type", dataType=o6.LocalizedText)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=6279",
                browseName="ns=di;SerialNumber",
                description="Represents the serial number of the machine (unique ID given by the manufacturer)",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6280", browseName="ns=di;AssetId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6281", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6909", browseName="ns=di;DeviceManual", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7159", browseName="ns=di;DeviceRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7160", browseName="ns=di;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7161", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7162", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7163", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7164", browseName="ns=di;RevisionCounter", dataType=o6.Int32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7165", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_tcd;i=7166",
                browseName="ns=plastics_rubber;YearOfConstruction",
                description="Represents the year of construction of the machine",
                dataType=o6.UInt16,
            )
        ),
    ],
)
o6.reference(plastics_tcd_objtypes.TCD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_tcd;i=5047"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_tcd_datypes, plastics_tcd_objtypes
