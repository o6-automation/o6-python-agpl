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

"""Generated OPC UA plastics_extrusion_v1_extruder namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion_v1 as plastics_extrusion_v1
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_v1_extruder_datypes
from . import objtypes as plastics_extrusion_v1_extruder_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6010",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6011", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6012", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6013",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6014", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6015", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6025",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6026", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6027", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5003",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6038", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5003"], "i=41", "i=2133")
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6039",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_extruder;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("ONLY_CONVEYING"),
        o6.LocalizedText("OTHER"),
        o6.LocalizedText("GRAVIMETRIC"),
        o6.LocalizedText("VOLUMETRIC"),
        o6.LocalizedText("LIQUID"),
        o6.LocalizedText("BATCH"),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6043",
    browseName="ns=plastics_rubber;Density",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6044", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MaterialType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5009",
    browseName="ns=plastics_extrusion_v1_extruder;Material",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6046", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="\n      ")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6047", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6043"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6059",
    browseName="ns=plastics_rubber;Interval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6060", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6061", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6062",
    browseName="ns=plastics_rubber;RemainingInterval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6064", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6065",
    browseName="ns=plastics_rubber;TotalOperation",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6066", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6067", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6049",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6053", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6054",
    browseName="ns=plastics_rubber;Density",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6073", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MaterialType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5008",
    browseName="ns=plastics_extrusion_v1_extruder;Material",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6075", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="\n      ")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6076", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6054"]),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.HopperType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5008"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6078",
    browseName="ns=plastics_extrusion_v1_extruder;Weight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6079", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.HopperType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=6078"])
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5021",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6088", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5021"], "i=41", "i=2133")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6071",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6072", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6094", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6104",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6105", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6106", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6096",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6097", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6117", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6098",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6099", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6118", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6100",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6101", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6119", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6102",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6103", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6120", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6107",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6108", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6121", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6109",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6110", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6122", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6111",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6112", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6123", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6113",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6114", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6124", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6115",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6116", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6125", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6132",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6133", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6134",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6135", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6136",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6137", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5023",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6132"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6134"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6136"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_extruder;i=6138", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6140",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6141", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6142", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6143",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6145", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6146",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6147", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6148", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6149",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6150", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6151", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6153",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6154", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6155", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6156",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6157", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6158", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6159",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6160", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6161", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6162",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6163", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6164", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6165",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6166", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6167", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6168",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6169", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6170", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6092",
    browseName="ns=plastics_extrusion_v1_extruder;Weight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6173", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6171",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6172", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6175", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6176",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6177", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6178", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6179",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6180", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6181", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6182",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6184", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6189",
    browseName="ns=plastics_rubber;Interval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6190", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6191", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6192",
    browseName="ns=plastics_rubber;RemainingInterval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6193", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6194", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6197",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6198", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6199", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6201",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6202", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6203", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6204",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6205", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6206", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5031",
    browseName="ns=plastics_extrusion_v1_extruder;MeltTemperatureZones",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6209", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5031"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5031"], "i=41", "i=2133")
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5032",
    browseName="ns=plastics_extrusion_v1_extruder;MeltPressureZones",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6210", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5032"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5032"], "i=41", "i=2133")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6207",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6211", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6212",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6213", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6214", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6215",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6216", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6217", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6218",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6219", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6220", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6221",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6222", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6223", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6224",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6225", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6226", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6227",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6228", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6229", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6230",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6231", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6232", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6174",
    browseName="ns=plastics_rubber;Density",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6233", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MaterialType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5015",
    browseName="ns=plastics_extrusion_v1_extruder;Material",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6234", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="\n      ")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6235", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6174"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6093",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6128", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6236", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6130",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6131", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6237", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6238",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6239", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6240", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6242",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6243", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6244", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6246",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6247", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6248",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6249", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6250",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6251", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5006",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6246"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6248"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6250"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_extruder;i=6252", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6257",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6258", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6259", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6269",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6270", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6271", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6282",
    browseName="ns=plastics_extrusion_v1_extruder;Weight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6283", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6285",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6286", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6287", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6288",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6289", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6290", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6291",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6292", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6293", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6294",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6295", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6296", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6298",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6299", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6300", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6301",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6302", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6303", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6304",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6305", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6306", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6307",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6308", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6309", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6310",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6311", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6312", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6313",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6314", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6315", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6316",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6317", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6318", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6319",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6320", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6321", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6322",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6323", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6324", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6325",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6326", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6327", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6329",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6330", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6331", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6333",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6334", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6335", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6336",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6337", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6338", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6339",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6340", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6341", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5037",
    browseName="ns=plastics_extrusion_v1_extruder;AdditionalDrives",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6343", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5037"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5037"], "i=41", "i=2133")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6245",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6344", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6345", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6346",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6347", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6348", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6349",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6350", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6351", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6352",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6353", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6354", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6355",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6356", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6357", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6358",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6359", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6360", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6361",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6362", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6363", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6364",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6365", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6366", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6367",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6368", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6369", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6126",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6127", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6370", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6342",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6371", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6372", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6373",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6374", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6375", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6376",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6377", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6378", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6379",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6380", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6381", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6382",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6383", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6384", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6385",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6386", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6387", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6388",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6389", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6390", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6391",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6392", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6393", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6395",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6396", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6397", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6398",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6399", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6400", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6401",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6402", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6403", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusionSlashExtruderSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5022",
    browseName="ns=plastics_extrusion_v1_extruder;http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6074", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6407", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2020-06-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6408",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6409", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6410",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6411", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6412", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6404",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6405", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6413", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6414",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6415", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6416", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6417",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6418", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6419", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6420",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6421", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6422", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6423",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6424", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6425", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6426",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6427", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6428", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6429",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6430", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6431", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6051",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6068", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6432", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6082",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6084", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6433", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6086",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6087", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6434", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6255",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6256", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6435", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6261",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6262", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6436", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6263",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6437", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6265",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6266", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6438", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6267",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6268", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6439", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6272",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6273", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6440", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6274",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6275", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6441", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6276",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6277", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6442", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6278",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6279", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6443", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6280",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6281", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6444", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6195",
    browseName="ns=plastics_rubber;TotalOperation",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6196", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6445", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
oPC40084_3 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6516",
    browseName="ns=plastics_extrusion_v1_extruder;OPC40084_3",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6517",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/",
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="FeedingModeEnumeration">\n  <opc:EnumeratedValue Name="ONLY_CONVEYING" Value="0"/>\n  <opc:EnumeratedValue Name="OTHER" Value="1"/>\n  <opc:EnumeratedValue Name="GRAVIMETRIC" Value="2"/>\n  <opc:EnumeratedValue Name="VOLUMETRIC" Value="3"/>\n  <opc:EnumeratedValue Name="LIQUID" Value="4"/>\n  <opc:EnumeratedValue Name="BATCH" Value="5"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
oPC40084_3_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6518",
    browseName="ns=plastics_extrusion_v1_extruder;OPC40084_3",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6519",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Extruder/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="FeedingModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ONLY_CONVEYING_0"/>\n   <xs:enumeration value="OTHER_1"/>\n   <xs:enumeration value="GRAVIMETRIC_2"/>\n   <xs:enumeration value="VOLUMETRIC_3"/>\n   <xs:enumeration value="LIQUID_4"/>\n   <xs:enumeration value="BATCH_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FeedingModeEnumeration" name="FeedingModeEnumeration"/>\n <xs:complexType name="ListOfFeedingModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FeedingModeEnumeration" name="FeedingModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFeedingModeEnumeration" name="ListOfFeedingModeEnumeration" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6525",
    browseName="ns=plastics_extrusion_v1_extruder;SpecificOutput",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6406", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=6525"])
plastics_rubber.objtypes.UsersType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5029",
    browseName="ns=plastics_rubber;Users",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6551", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5029"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5029"], "i=41", "i=2133")
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5033",
    browseName="ns=plastics_extrusion_v1_extruder;VacuumZones",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6555", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5033"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5033"], "i=41", "i=2133")
plastics_extrusion_v1_extruder_objtypes.FeedersType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5036",
    browseName="ns=plastics_extrusion_v1_extruder;Feeders",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6558", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5036"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5036"], "i=41", "i=2133")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6523",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6524", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6577", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6578",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6579", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6580", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6590",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6591", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6592", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6582",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6583", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6684", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6584",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6585", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6685", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6586",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6587", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6686", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6588",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6589", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6687", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6593",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6594", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6688", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6595",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6596", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6689", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6597",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6598", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6690", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6599",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6600", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6691", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6601",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6602", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6692", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6017",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6018", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6693", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6019",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6020", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6694", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6021",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6022", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6695", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6023",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6024", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6696", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6028",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6029", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6697", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6030",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6031", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6698", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6032",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6033", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6034",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6035", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6700", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=6036",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6037", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6701", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5004",
    browseName="ns=plastics_extrusion_v1;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6185",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6188", browseName="ns=plastics_rubber;AdditionalInformation", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6189"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6192"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6195"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7001", browseName="ns=plastics_rubber;Reset")),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5038",
    browseName="ns=plastics_extrusion_v1;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6056",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6058", browseName="ns=plastics_rubber;AdditionalInformation", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6059"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6062"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6065"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7002", browseName="ns=plastics_rubber;Reset")),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5010",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6050",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6284",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6285"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6288"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6291"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7004",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5018",
    browseName="ns=plastics_extrusion_v1_extruder;MaterialTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6095",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6049"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6071"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6096"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6098"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6100"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6102"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6104"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6107"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6109"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6111"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6113"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6115"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7005",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.HopperType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5018"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5024",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6089",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6139",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6140"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6143"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6146"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7006",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5025",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6152",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6093"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6149"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6153"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6156"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6159"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6162"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6165"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6168"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6171"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6176"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6179"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6182"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7007",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5027",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6129",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6186", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7008", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7009", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5028",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6200",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6130"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6197"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6201"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6204"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6207"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6212"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6215"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6218"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6221"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6224"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6227"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6230"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7010",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5019",
    browseName="ns=plastics_extrusion_v1_extruder;MainDrive",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5021"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5023"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5024"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5025"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5027"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5028"]),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5019"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5034",
    browseName="ns=plastics_extrusion_v1_extruder;MaterialTemperature",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6260",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6255"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6257"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6261"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6263"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6265"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6267"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6269"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6272"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6274"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6276"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6278"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6280"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7011",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_extrusion_v1_extruder_objtypes.HopperType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5007",
    browseName="ns=plastics_extrusion_v1_extruder;Hopper",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6042", browseName="ns=plastics_extrusion_v1_extruder;Id", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6254", browseName="ns=plastics_extrusion_v1_extruder;MaterialLot", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5009"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5034"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_extruder;i=6253", browseName="ns=plastics_extrusion_v1_extruder;MaterialLevel", dataType=o6.Double)
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6282"]),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5011",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6297",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6051"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6294"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6298"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6301"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6304"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6307"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6310"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6313"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6316"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6319"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6322"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6325"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7012",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5020",
    browseName="ns=plastics_extrusion_v1_extruder;MaterialTemperature",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6241",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6126"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6238"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6242"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6245"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6346"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6349"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6352"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6355"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6358"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6361"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6364"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6367"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7014",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_extrusion_v1_extruder_objtypes.HopperType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5014",
    browseName="ns=plastics_extrusion_v1_extruder;Hopper",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6052", browseName="ns=plastics_extrusion_v1_extruder;Id", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6091", browseName="ns=plastics_extrusion_v1_extruder;MaterialLot", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5020"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_extruder;i=6090", browseName="ns=plastics_extrusion_v1_extruder;MaterialLevel", dataType=o6.Double)
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6092"]),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.FeederType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5014"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5013",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6081",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6328", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7013", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7015", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5016",
    browseName="ns=plastics_extrusion_v1_extruder;Throughput",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6332", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6082"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6329"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6333"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6336"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6339"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6342"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6373"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6376"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6379"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6382"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6385"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6388"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7016", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5017",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6394",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6086"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6391"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6395"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6398"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6401"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6404"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6414"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6417"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6420"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6423"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6426"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6429"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_extruder;i=7017",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_extrusion_v1_extruder_objtypes.FeederType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5002",
    browseName="ns=plastics_extrusion_v1_extruder;Feeder_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6003", browseName="ns=plastics_extrusion_v1_extruder;Id", dataType=o6.String)),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6006", browseName="ns=plastics_extrusion_v1_extruder;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6007",
                browseName="ns=plastics_extrusion_v1_extruder;Mode",
                dataType=plastics_extrusion_v1_extruder_datypes.FeedingModeEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6008", browseName="ns=plastics_extrusion_v1_extruder;Name", dataType=o6.LocalizedText, value=o6.LocalizedText()
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6009", browseName="ns=plastics_extrusion_v1_extruder;Target", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6048", browseName="ns=plastics_extrusion_v1_extruder;IsControlled", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5003"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5006"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5007"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5010"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5011"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5013"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5016"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5017"]),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.FeedersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5002"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5035",
    browseName="ns=plastics_extrusion_v1;StartTempering",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6057",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6447", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7003", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7018", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_extrusion_v1.objtypes.ExtrusionTemperatureZonesType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5012",
    browseName="ns=plastics_extrusion_v1_extruder;ScrewTemperatures",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6055", browseName="NodeVersion", dataType=o6.Double, value=0.0)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5035"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5038"]),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5012"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5012"], "i=41", "i=2133")
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5026",
    browseName="ns=plastics_extrusion_v1_extruder;Throughput",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6581", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6523"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6578"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6582"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6584"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6586"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6588"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6590"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6593"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6595"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6597"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6599"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6601"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7019", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5026"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5001",
    browseName="ns=plastics_extrusion_v1_extruder;Throughput",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6016", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6010"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6013"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6017"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6021"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6023"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6025"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6028"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6030"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6032"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6034"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=6036"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7020", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.FeederType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5001"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5005",
    browseName="ns=plastics_extrusion_v1;StartTempering",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6187",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_extruder;i=6446", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7021", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_extruder;i=7022", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_extrusion_v1.objtypes.ExtrusionTemperatureZonesType(
    nodeId="ns=plastics_extrusion_v1_extruder;i=5030",
    browseName="ns=plastics_extrusion_v1_extruder;TemperatureZones",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_extruder;i=6045", browseName="NodeVersion", dataType=o6.String, value="0")),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_extruder;i=5005"]),
    ],
)
o6.reference(plastics_extrusion_v1_extruder_objtypes.Extruder_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_extruder;i=5030"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_extruder;i=5030"], "i=41", "i=2133")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_rubber, plastics_extrusion_v1_extruder_datypes, plastics_extrusion_v1_extruder_objtypes
