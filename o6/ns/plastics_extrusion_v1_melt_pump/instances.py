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

"""Generated OPC UA plastics_extrusion_v1_melt_pump namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion_v1 as plastics_extrusion_v1
import o6.ns.plastics_rubber as plastics_rubber
from . import objtypes as plastics_extrusion_v1_melt_pump_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5001",
    browseName="ns=plastics_extrusion_v1_melt_pump;MeltPressures",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6001", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_v1_melt_pump_objtypes.MeltPump_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5001"])
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5003",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6002", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5003"], "i=41", "i=2133")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6009",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6010", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6011",
    browseName="ns=plastics_extrusion_v1_melt_pump;FeedRate",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_melt_pump_objtypes.MeltPump_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6011"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6018",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6019", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6020",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5004",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6009"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6018"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6020"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6022", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6024",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6025", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6026", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6027",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6028", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6029", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6030",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6031", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6032", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6035",
    browseName="ns=plastics_rubber;Interval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6036", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6037", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6038",
    browseName="ns=plastics_rubber;RemainingInterval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6039", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6040", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6033",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6041", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6042", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6044",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6045", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6046", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6047",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6048", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6049", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6050",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6051", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6052", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6053",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6054", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6055", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6056",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6057", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6058", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6059",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6060", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6061", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6062",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6064", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6065",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6066", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6067", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6068",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6071",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6073", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6075",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6076", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6077", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6079",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6080", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6081", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6082",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6083", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6084", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6085",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6086", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6087", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6088",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6089", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6090", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6091",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6092", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6093", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6094",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6095", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6096", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6097",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6098", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6099", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6100",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6102", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6103",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6104", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6105", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6107",
    browseName="ns=plastics_rubber;TotalOperation",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6108", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6109", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6106",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6110", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6111", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6004",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6005", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6112", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=6007",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6008", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusionSlashMeltPumpSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5010",
    browseName="ns=plastics_extrusion_v1_melt_pump;http://opcfoundation.org/UA/PlasticsRubber/Extrusion/MeltPump/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6013", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6017", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2020-06-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6116",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/MeltPump/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6117", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6118",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6119", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6120", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5009",
    browseName="ns=plastics_extrusion_v1;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6015",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6034", browseName="ns=plastics_rubber;AdditionalInformation", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6035"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6038"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6107"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_melt_pump;i=7001", browseName="ns=plastics_rubber;Reset")),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5007",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6003",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6023",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6024"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6027"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6030"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=7002",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5008",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6043",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6033"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6044"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6047"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6050"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6053"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6056"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6059"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6062"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6065"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6068"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6071"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=7003",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5011",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6006",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6074", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_melt_pump;i=7004", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_melt_pump;i=7005", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5012",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6078",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6007"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6075"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6079"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6082"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6085"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6088"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6091"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6094"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6097"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6100"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6103"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=6106"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=7006",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5002",
    browseName="ns=plastics_extrusion_v1_melt_pump;Drive",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5003"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5007"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5008"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5011"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5012"]),
    ],
)
o6.reference(plastics_extrusion_v1_melt_pump_objtypes.MeltPump_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5002"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5006",
    browseName="ns=plastics_extrusion_v1;StartTempering",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6016",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_melt_pump;i=6114", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_melt_pump;i=7007", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_melt_pump;i=7008", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_extrusion_v1.objtypes.ExtrusionTemperatureZonesType(
    nodeId="ns=plastics_extrusion_v1_melt_pump;i=5005",
    browseName="ns=plastics_extrusion_v1_melt_pump;TemperatureZones",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_melt_pump;i=6014", browseName="NodeVersion", dataType=o6.Double, value=0.0)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5006"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5009"]),
    ],
)
o6.reference(plastics_extrusion_v1_melt_pump_objtypes.MeltPump_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_melt_pump;i=5005"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_rubber, plastics_extrusion_v1_melt_pump_objtypes
