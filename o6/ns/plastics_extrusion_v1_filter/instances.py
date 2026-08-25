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

"""Generated OPC UA plastics_extrusion_v1_filter namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion_v1 as plastics_extrusion_v1
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_v1_filter_datypes
from . import objtypes as plastics_extrusion_v1_filter_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5001",
    browseName="ns=plastics_extrusion_v1_filter;MeltPressureZones",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6001", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5001"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_filter;i=5001"], "i=41", "i=2133")
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5004",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6002", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(o6.ns["ns=plastics_extrusion_v1_filter;i=5004"], "i=41", "i=2133")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6004",
    browseName="ns=plastics_extrusion_v1_filter;FiltrationFineness",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6005", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=6004"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6011",
    browseName="ns=plastics_extrusion_v1_filter;Area",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=6011"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6007",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6008", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6019", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6020",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6021", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6022", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6032",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6033", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6034", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6016",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6018", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6045", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6046",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6047", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6048", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6058",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6059", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6060", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6074",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6076",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6078", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6079",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5017",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6074"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6076"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6079"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_filter;i=6082", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6084",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6085", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6086", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6087",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6088", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6089", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6090",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6091", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6092", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6093",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6094", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6095", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6097",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6098", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6099", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6100",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6102", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6103",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6104", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6105", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6106",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6107", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6108", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6109",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6110", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6111", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6112",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6114", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6115",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6116", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6117", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6118",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6119", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6120", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6121",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6122", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6123", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6124",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6125", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6126", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6128",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6129", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6130", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6133",
    browseName="ns=plastics_rubber;Interval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6134", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6135", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6136",
    browseName="ns=plastics_rubber;RemainingInterval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6137", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6138", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6139",
    browseName="ns=plastics_extrusion_v1_filter;BackflushPressure",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=6139"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6140",
    browseName="ns=plastics_extrusion_v1_filter;Area",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6141", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6145",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6146", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6147", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5011",
    browseName="ns=plastics_extrusion_v1_filter;MeltTemperatureZones",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6149", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5011"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_filter;i=5011"], "i=41", "i=2133")
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5012",
    browseName="ns=plastics_extrusion_v1_filter;AdditionalMeasuringDevices",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6150", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5012"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6155",
    browseName="ns=plastics_extrusion_v1_filter;Area",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6156", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_filter_objtypes.ScreenPackageType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=6155"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6158",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_filter;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("NOT_ACTIVE"),
        o6.LocalizedText("ACTIVE"),
        o6.LocalizedText("CHANGE_REQUIRED"),
        o6.LocalizedText("IN_CHANGE_POSITION"),
        o6.LocalizedText("BACKFLUSH_ACTIVE"),
    ],
)
oPC40084_6 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6159",
    browseName="ns=plastics_extrusion_v1_filter;OPC40084_6",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6160", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/"
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="FilterPackageStatusEnumeration">\n  <opc:EnumeratedValue Name="NOT_ACTIVE" Value="0"/>\n  <opc:EnumeratedValue Name="ACTIVE" Value="1"/>\n  <opc:EnumeratedValue Name="CHANGE_REQUIRED" Value="2"/>\n  <opc:EnumeratedValue Name="IN_CHANGE_POSITION" Value="3"/>\n  <opc:EnumeratedValue Name="BACKFLUSH_ACTIVE" Value="4"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
oPC40084_6_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6161",
    browseName="ns=plastics_extrusion_v1_filter;OPC40084_6",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6162",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="FilterPackageStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NOT_ACTIVE_0"/>\n   <xs:enumeration value="ACTIVE_1"/>\n   <xs:enumeration value="CHANGE_REQUIRED_2"/>\n   <xs:enumeration value="IN_CHANGE_POSITION_3"/>\n   <xs:enumeration value="BACKFLUSH_ACTIVE_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FilterPackageStatusEnumeration" name="FilterPackageStatusEnumeration"/>\n <xs:complexType name="ListOfFilterPackageStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FilterPackageStatusEnumeration" name="FilterPackageStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFilterPackageStatusEnumeration" name="ListOfFilterPackageStatusEnumeration" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6166",
    browseName="ns=plastics_extrusion_v1_filter;Area",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6013", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_filter_objtypes.FilterPackageType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=6166"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6157",
    browseName="ns=plastics_extrusion_v1_filter;Area",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6167", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
plastics_extrusion_v1_filter_objtypes.ScreenPackageType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5013",
    browseName="ns=plastics_extrusion_v1_filter;ScreenPackage_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6152", browseName="ns=plastics_extrusion_v1_filter;Name", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6175", browseName="ns=plastics_extrusion_v1_filter;PackageSetup", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6176", browseName="ns=plastics_extrusion_v1_filter;SerialNr", dataType=o6.String, value="")
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6157"]),
    ],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.FilterPackageType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5013"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6188",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6189", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6190", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6143",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6144", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6204", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6163",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6164", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6170",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6171", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6209", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6211",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6212", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6213", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6214",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6215", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6216", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6217",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6218", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6219", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6178",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6185", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6186",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6187", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6221", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6050",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6051", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6222", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6052",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6053", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6223", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6054",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6055", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6224", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6056",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6057", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6225", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6061",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6062", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6226", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6063",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6064", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6227", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6065",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6228", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6067",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6068", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6229", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6069",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6230", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6231",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6232", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6233", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6234",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6235", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6236", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6237",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6238", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6239", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6240",
    browseName="ns=plastics_rubber;TotalOperation",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6241", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6242", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6024",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6025", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6243", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6026",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6027", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6244", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6028",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6029", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6245", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6030",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6031", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6246", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6035",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6036", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6247", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6037",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6038", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6248", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6039",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6040", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6249", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6041",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6042", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6250", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6043",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6044", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6251", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusionSlashFilterSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5023",
    browseName="ns=plastics_extrusion_v1_filter;http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6172", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6173", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2020-06-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6174", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Filter/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6180", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6181",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6184", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6252", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6253",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6254", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6255", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6256",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6257", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6258", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6259",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6260", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6261", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6262",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6263", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6265",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6266", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6267", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6268",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6269", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6270", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6193",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6194", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6273", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6271",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6272", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6274", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6009",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6010", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6275", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_extrusion_v1_filter_objtypes.FilterPackageType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5014",
    browseName="ns=plastics_extrusion_v1_filter;FilterPackage_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6179",
                browseName="ns=plastics_extrusion_v1_filter;Status",
                dataType=plastics_extrusion_v1_filter_datypes.FilterPackageStatusEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6182", browseName="ns=plastics_extrusion_v1_filter;BackflushCounter", dataType=o6.UInt32)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6183",
                browseName="ns=plastics_extrusion_v1_filter;BackflushTime",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6277", browseName="ns=plastics_extrusion_v1_filter;Name", dataType=o6.LocalizedText)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6140"]),
    ],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5014"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6195",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6196", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6278", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6197",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6198", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6279", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6200",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6201", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6280", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6202",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6203", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6281", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_filter;i=6072",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6073", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6282", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5009",
    browseName="ns=plastics_extrusion_v1;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6015",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6132", browseName="ns=plastics_rubber;AdditionalInformation", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6133"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6136"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6240"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7001", browseName="ns=plastics_rubber;Reset")),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5015",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6177",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6210",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6211"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6214"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6217"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_filter;i=7002",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5003",
    browseName="ns=plastics_extrusion_v1_filter;WasteOutput",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6023",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6007"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6020"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6024"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6026"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6028"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6030"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6032"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6035"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6037"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6039"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6041"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6043"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7003", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5003"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5006",
    browseName="ns=plastics_extrusion_v1_filter;SpecificWasteOutput",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6049",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6016"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6046"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6050"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6052"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6054"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6056"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6058"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6061"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6063"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6065"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6067"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6069"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7004", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5006"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5018",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6003",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6083",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6084"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6087"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6090"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_filter;i=7006",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5008",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6205",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6206",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6207",
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
                nodeId="ns=plastics_extrusion_v1_filter;i=7007",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7008", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5019",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6096",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6009"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6093"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6097"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6100"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6103"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6106"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6109"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6112"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6115"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6118"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6121"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6124"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_filter;i=7010",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5016",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6199",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6283", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7009", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7011", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5007",
    browseName="ns=plastics_extrusion_v1_filter;HydraulicPressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6077",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6080", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6142", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6148",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6191", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6192", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5008"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5016"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6143"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6145"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6163"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6170"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6178"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6186"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6188"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6193"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6195"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6197"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6200"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6202"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_filter;i=7005",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5007"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5020",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6071",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6127", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7012", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7013", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5021",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6131",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6072"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6128"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6231"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6234"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6237"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6253"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6256"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6259"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6262"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6265"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6268"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=6271"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_filter;i=7014",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5002",
    browseName="ns=plastics_extrusion_v1_filter;Drive",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5017"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5018"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5020"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5021"]),
    ],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5002"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5010",
    browseName="ns=plastics_extrusion_v1;StartTempering",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6017",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_filter;i=6284", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7015", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_filter;i=7016", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_extrusion_v1.objtypes.ExtrusionTemperatureZonesType(
    nodeId="ns=plastics_extrusion_v1_filter;i=5005",
    browseName="ns=plastics_extrusion_v1_filter;TemperatureZones",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_filter;i=6014", browseName="NodeVersion", dataType=o6.Double, value=0.0)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5009"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_filter;i=5010"]),
    ],
)
o6.reference(plastics_extrusion_v1_filter_objtypes.Filter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_filter;i=5005"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_filter;i=5005"], "i=41", "i=2133")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_rubber, plastics_extrusion_v1_filter_datypes, plastics_extrusion_v1_filter_objtypes
