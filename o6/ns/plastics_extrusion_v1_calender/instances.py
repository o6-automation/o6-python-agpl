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

"""Generated OPC UA plastics_extrusion_v1_calender namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion_v1 as plastics_extrusion_v1
import o6.ns.plastics_rubber as plastics_rubber
from . import objtypes as plastics_extrusion_v1_calender_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6002",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6003", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6007",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6008", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6009", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6019",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6020", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6021", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6011",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6012", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6032", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6013",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6014", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6033", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6015",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6016", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6034", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6017",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6018", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6035", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6022",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6023", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6036", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6024",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6025", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6037", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6026",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6027", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6038", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6028",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6029", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6039", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6030",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6031", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6040", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6004",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6005", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6041", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6042",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6043", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6044", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6054",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6055", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6056", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6046",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6047", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6067", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6048",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6049", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6068", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6050",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6051", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6052",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6053", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6070", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6057",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6058", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6071", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6059",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6060", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6061",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6062", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6073", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6063",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6064", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6074", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6065",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6077",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6078", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6079", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6080",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6081", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6082", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6084",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6085", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6086",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6087", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6088",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6089", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6090",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6091", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6092",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6093", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6094", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6095",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6096", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6097",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6098", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6099",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6100", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6101",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6102", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6103",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6104", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6106",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6107", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5004",
    browseName="ns=plastics_extrusion_v1_calender;CouplingProductTension_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6106"])],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.CouplingProductTensionsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5004"])
plastics_extrusion_v1_calender_objtypes.CouplingProductTensionsType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5054",
    browseName="ns=plastics_extrusion_v1_calender;CouplingProductTensions",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6108", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.Calender_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5054"])
plastics_extrusion_v1_calender_objtypes.CouplingProductForcesType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5005",
    browseName="ns=plastics_extrusion_v1_calender;CouplingProductForces",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6109", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.Calender_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5005"])
plastics_extrusion_v1.objtypes.RollsType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5055",
    browseName="ns=plastics_extrusion_v1_calender;Rolls",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6110", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.Calender_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5055"])
plastics_extrusion_v1.objtypes.GapsType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5056",
    browseName="ns=plastics_extrusion_v1_calender;Gaps",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6111", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.Calender_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5056"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6909",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6910", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6989", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6990",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6991", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6992", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5001",
    browseName="ns=plastics_extrusion_v1_calender;ProductForce",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=6010",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6002"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6007"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6011"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6013"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6017"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6022"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6024"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6026"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6028"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6030"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_calender;i=7001",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.Calender_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5001"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5002",
    browseName="ns=plastics_extrusion_v1_calender;ProductTension",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=6045",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6042"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6046"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6048"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6050"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6052"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6054"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6057"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6059"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6061"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6063"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6065"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_calender;i=7002",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.Calender_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5002"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5003",
    browseName="ns=plastics_extrusion_v1_calender;CouplingProductForce_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=6083",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6077"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6080"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6084"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6086"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6088"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6090"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6092"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6095"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6097"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6099"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6101"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6103"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_calender;i=7003",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.CouplingProductForcesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5003"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7062",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7063", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7064", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6994",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6995", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7076", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6996",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6997", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7077", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6998",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6999", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7078", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7000",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7061", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7079", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7066",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7067", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7080", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7068",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7069", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7070",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7071", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7082", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7072",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7073", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7083", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7074",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7075", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7084", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5051",
    browseName="ns=plastics_extrusion_v1_calender;HorizontalPosition",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=6993",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6909"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6990"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6994"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6996"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6998"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7000"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7062"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_calender;i=7065",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7066"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7068"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7070"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7072"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7074"]),
    ],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.Calender_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5051"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=6911",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6912", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7085", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7086",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7087", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7088", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7098",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7099", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7100", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7090",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7091", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7110", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7092",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7093", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7111", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7094",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7095", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7112", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7096",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7097", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7102",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7103", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7114", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7104",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7105", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7115", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7106",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7107", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7116", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7108",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7109", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7117", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_calender;i=7118",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=6001", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7119", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5052",
    browseName="ns=plastics_extrusion_v1_calender;VerticalPosition",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=7089",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=6911"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7086"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7090"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7092"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7094"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7096"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7098"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_calender;i=7101",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7102"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7104"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7106"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7108"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_calender;i=7118"]),
    ],
)
o6.reference(plastics_extrusion_v1_calender_objtypes.Calender_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_calender;i=5052"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusionSlashCalenderSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_v1_calender;i=5057",
    browseName="ns=plastics_extrusion_v1_calender;http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Calender/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7120", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=7121", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-04-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=7122",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/Calender/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7123", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=7124",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_calender;i=7125", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_calender;i=7126", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_rubber, plastics_extrusion_v1_calender_objtypes
