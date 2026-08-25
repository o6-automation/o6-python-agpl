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

"""Generated OPC UA plastics_extrusion_calibrator namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion as plastics_extrusion
import o6.ns.plastics_rubber as plastics_rubber
from . import objtypes as plastics_extrusion_calibrator_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5002",
    browseName="ns=plastics_extrusion_calibrator;VacuumPumps",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6009", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5002"])
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5002"], "i=41", "i=2133")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6008",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6010", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6011", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6022",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6023", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6024", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5017",
    browseName="ns=plastics_extrusion_calibrator;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6040", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5017"], "i=41", "i=2133")
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5020",
    browseName="ns=plastics_extrusion_calibrator;VacuumPumps",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6053", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5020"], "i=41", "i=2133")
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5006",
    browseName="ns=plastics_extrusion_calibrator;WaterPumps",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6061", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5006"])
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5006"], "i=41", "i=2133")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6070",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6071", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6044",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6045", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6073", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5009",
    browseName="ns=plastics_extrusion_calibrator;AdditionalMeasuringDevices",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6074", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5009"])
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5009"], "i=41", "i=2133")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6075",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6076", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6077", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6088",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6089", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6090", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6104",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6105", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6106", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6117",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6118", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6119", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5023",
    browseName="ns=plastics_extrusion_calibrator;WaterPumps",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6128", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5023"], "i=41", "i=2133")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6065",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6130", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6132",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6133", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6134", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6145",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6146", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6147", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6079",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6080", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6169", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6081",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6082", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6170", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6172",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6179", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6180", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6181",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6182", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6183", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6184",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6185", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6186", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6084",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6085", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6187", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6086",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6087", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6188", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6093",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6094", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6189", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6095",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6096", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6190", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6097",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6098", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6191", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6100",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6101", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6192", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6102",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6103", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6193", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6108",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6109", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6197", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6110",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6111", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6198", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6200",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6201", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6202", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6203",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6204", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6205", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6206",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6207", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6208", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6113",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6114", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6209", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6115",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6116", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6210", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6122",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6123", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6212",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6213", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6214", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6219",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6221", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6222",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6223", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6224", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6006",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6007", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6231", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6013",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6014", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6235", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6015",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6016", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6236", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6238",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6239", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6240", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6241",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6242", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6243", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6244",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6245", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6246", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6018",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6019", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6247", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6020",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6021", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6248", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6027",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6028", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6249", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6029",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6030", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6250", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6031",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6032", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6251", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6034",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6035", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6252", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6036",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6037", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6253", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6256",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6257", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6258", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6259",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6260", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6261", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6262",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6263", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6264", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6267",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6268", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6269", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6270",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6271", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6272", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6273",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6274", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6275", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6277",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6278", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6279", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6280",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6281", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6282", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6283",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6284", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6285", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6290",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6291", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6292", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6293",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6294", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6295", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6304",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6305", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6306", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6307",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6308", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6309", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5033",
    browseName="ns=plastics_extrusion_calibrator;PositionsX",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6316", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_calibrator_objtypes.Calibrator_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5033"])
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5033"], "i=41", "i=2133")
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5034",
    browseName="ns=plastics_extrusion_calibrator;PositionsY",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6317", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_calibrator_objtypes.Calibrator_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5034"])
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5034"], "i=41", "i=2133")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6314",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6315", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6318", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6319",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6320", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6321", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5035",
    browseName="ns=plastics_extrusion_calibrator;PositionsPipeSupport",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6323", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_calibrator_objtypes.Calibrator_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5035"])
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5035"], "i=41", "i=2133")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6336",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6337", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6338", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6349",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6350", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6351", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6365",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6366", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6367", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6370",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6371", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6372", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6373",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6374", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6375", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6376",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6377", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6378", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6390",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6391", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6392", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6381",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6382", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6408", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6383",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6384", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6409", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6411",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6412", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6413", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6414",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6415", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6416", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6417",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6418", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6419", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6386",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6387", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6420", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6388",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6389", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6421", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6394",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6395", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6422", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6396",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6397", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6423", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6398",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6399", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6424", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6401",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6402", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6425", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6403",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6404", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6426", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6380",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6427", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6428", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6429",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6430", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6431", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6432",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6433", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6434", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6334",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6335", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6439", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6441",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6442", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6443", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6454",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6455", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6456", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6440",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6470", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6471", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6472",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6473", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6474", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6483",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6484", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6485", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6506",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6507", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6508", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6519",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6520", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6521", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6537",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6538", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6539", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6553",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6554", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6555", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6494",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6495", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6563", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6558",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6559", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6564", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6565",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6566", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6567", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6578",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6579", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6580", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6594",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6595", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6596", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6607",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6608", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6609", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6610",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6611", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6612", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6623",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6624", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6625", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6641",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6642", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6643", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6657",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6658", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6659", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6662",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6663", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6664", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6675",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6676", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6677", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6693",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6694", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6695", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6709",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6710", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6711", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusion_v2SlashCalibratorSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_calibrator;i=5064",
    browseName="ns=plastics_extrusion_calibrator;http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Calibrator/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6714", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6715", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-05-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6716",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Calibrator/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6717", browseName="NamespaceVersion", dataType=o6.String, value="2.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6718",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6719", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6720", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6721",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6722", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6723", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6724",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6725", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6726", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6729",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6730", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6731", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6732",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6733", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6734", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6735",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6736", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6737", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6328",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6330", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6738", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6340",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6341", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6742", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6342",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6343", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6743", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6745",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6746", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6747", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6748",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6749", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6750", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6751",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6752", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6753", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6345",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6346", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6754", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6347",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6348", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6755", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6354",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6355", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6756", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6356",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6357", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6757", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6358",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6359", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6758", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6361",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6362", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6759", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6363",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6364", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6760", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6762",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6763", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6764", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6765",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6766", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6767", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6768",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6769", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6770", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6775",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6776", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6777", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6778",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6779", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6780", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6789",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6790", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6791", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6445",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6446", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6795", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6447",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6448", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6796", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6798",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6799", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6800", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6801",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6802", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6803", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6804",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6805", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6806", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6450",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6451", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6807", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6452",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6453", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6808", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6459",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6460", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6809", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6461",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6462", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6810", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6463",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6464", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6811", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6466",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6467", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6812", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6468",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6469", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6813", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6814",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6815", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6816", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_calibrator;i=6817",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6818", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6819", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6822",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6823", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6824", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6825",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6826", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6827", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6828",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6829", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6830", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6832",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6833", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6834", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6136",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6137", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6839", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6138",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6139", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6840", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6842",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6843", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6844", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6845",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6846", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6847", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6848",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6849", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6850", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6141",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6142", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6851", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6143",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6144", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6852", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6150",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6151", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6853", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6152",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6153", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6854", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6154",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6173", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6855", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6175",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6176", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6856", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6177",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6178", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6857", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6835",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6858", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6859", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6124",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6125", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6860", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6048",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6049", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6861", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6054",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6055", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6862", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6059",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6060", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6863", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6129",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6131", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6864", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6159",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6160", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6865", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6162",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6163", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6866", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6164",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6165", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6867", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6226",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6227", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6868", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6228",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6229", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6869", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6254",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6255", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6870", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6297",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6298", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6871", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6299",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6300", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6872", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6302",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6303", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6873", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6476",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6477", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6874", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6478",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6479", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6875", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6481",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6482", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6876", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6782",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6783", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6877", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6784",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6785", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6878", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6787",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6788", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6879", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6489",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6490", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6906", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6510",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6511", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6910", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6512",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6513", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6911", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6913",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6914", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6915", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6916",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6917", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6918", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6919",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6920", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6921", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6515",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6516", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6922", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6517",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6518", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6923", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6524",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6525", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6924", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6526",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6527", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6925", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6528",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6529", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6926", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6531",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6532", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6927", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6533",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6534", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6928", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6535",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6536", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6929", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6544",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6545", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6933", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6546",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6547", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6934", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6936",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6937", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6938", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6939",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6940", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6941", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6942",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6943", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6944", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6549",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6550", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6945", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6551",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6552", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6946", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6880",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6881", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6947", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6882",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6883", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6948", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6884",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6900", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6949", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6902",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6903", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6950", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6904",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6905", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6951", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6569",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6570", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6963", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6571",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6572", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6964", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6966",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6967", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6968", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6969",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6970", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6971", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6972",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6973", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6974", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6574",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6575", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6975", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6576",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6577", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6976", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6583",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6584", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6977", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6585",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6586", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6978", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6587",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6588", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6979", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6590",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6591", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6980", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6592",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6593", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6981", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6598",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6599", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6985", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6600",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6601", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6986", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6988",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6989", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6990", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6991",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6992", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6993", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6994",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6995", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6996", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6603",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6604", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6997", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6605",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6606", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6998", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6887",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6888", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6999", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6889",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6952", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7000", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5004",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6017",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6237",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6238"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6241"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6244"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7001",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5011",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6083",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6171",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6172"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6181"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6184"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7003",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5003",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6232",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6233",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6234",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7005",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7006", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5026",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6112",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6199",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6200"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6203"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6206"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7007",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5010",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6166",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6167",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6168",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7009",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7010", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5014",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6140",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6841",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6842"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6845"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6848"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7013",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5025",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6194",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6195",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6196",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7015",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7016", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5028",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6216",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6217",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6218",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7019",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7020", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5029",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6225",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6230",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6226"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6228"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6254"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7023",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5031",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6287",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6288",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6289",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7027",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7028", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5043",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6344",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6744",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6745"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6748"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6751"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7029",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5065",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6296",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6301",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6297"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6299"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6302"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7031",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5039",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6739",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6740",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6741",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7033",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7034", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5041",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6385",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6410",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6411"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6414"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6417"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7035",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5040",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6405",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6406",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6407",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7037",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7038", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5046",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6449",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6797",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6798"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6801"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6804"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7041",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5045",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6792",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6793",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6794",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7045",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7046", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5053",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6514",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6912",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6913"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6916"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6919"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7047",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5078",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6548",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6935",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6936"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6939"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6942"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7049",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5052",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6907",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6908",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6909",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7051",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7052", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5056",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6573",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6965",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6966"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6969"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6972"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7053",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5081",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6602",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6987",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6988"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6991"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6994"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7055",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5055",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6960",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6961",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6962",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7057",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7058", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5067",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6436",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6437",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6438",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7073",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7074", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5068",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6475",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6480",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6476"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6478"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6481"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7075",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5070",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6772",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6773",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6774",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7081",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7082", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5013",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6836",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6837",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6838",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7083",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7084", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5071",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6781",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6786",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6782"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6784"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6787"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7087",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5077",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6930",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6931",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6932",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7093",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7094", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5080",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6982",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6983",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6984",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7099",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7100", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6953",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6954", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6956",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6957", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7104", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6958",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6959", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7105", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6499",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6500", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7110", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5058",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7111",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7114",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7115",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7112",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7113", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6614",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6615", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7116", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6616",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6617", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7117", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7119",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7120", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7121", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7122",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7123", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7124", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7125",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7126", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7127", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5059",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6618",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7118",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7059",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7119"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7122"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7125"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6619",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6620", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7128", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6621",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6622", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6628",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6629", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7130", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6630",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6631", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7131", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6632",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6633", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7132", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6635",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6636", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7135", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6637",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6638", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7136", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6639",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6640", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7137", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5083",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7138",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7139",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7142",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7140",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7141", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6648",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6649", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7143", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6650",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6651", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7146",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7147", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7148", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7149",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7150", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7151", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7152",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7153", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7154", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5084",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6652",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7145",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7061",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7146"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7149"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7152"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6653",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6654", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6655",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6656", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7156", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6890",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6891", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7157", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6892",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6893", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7158", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6894",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7063", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7159", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7106",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7107", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7162", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7108",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7109", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7163", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6504",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6505", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7168", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5061",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7169",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7172",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7173",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7170",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7171", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6666",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6667", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7174", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6668",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6669", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7175", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7177",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7178", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7179", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7180",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7181", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7182", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7183",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7184", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7185", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5062",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6670",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7176",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7065",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7177"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7180"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7183"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6671",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6672", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7186", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6673",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6674", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7187", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6680",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6681", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7188", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6682",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6683", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7189", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6684",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6685", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7190", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6687",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6688", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7193", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6689",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6690", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7194", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6691",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6692", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7195", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_calibrator;i=5086",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7196",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7197",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7200",
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
                nodeId="ns=plastics_extrusion_calibrator;i=7198",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7199", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6700",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6701", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7201", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6702",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6703", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7202", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7204",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7205", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7206", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7207",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7209", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7210",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7212", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5087",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6704",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7203",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7067",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7204"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7207"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7210"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6705",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6706", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7213", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6707",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6708", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7214", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6895",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6896", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7215", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6897",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6898", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7216", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=6899",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7069", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7217", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7164",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7165", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_calibrator;i=7166",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7167", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=7221", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5012",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6099",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7222", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7011", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7012", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5008",
    browseName="ns=plastics_extrusion_calibrator;AirShowerPressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6046",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6068", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6069", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6078",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6091", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6092", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5010"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5011"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5012"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6070"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6075"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6079"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6081"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6084"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6086"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6088"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6093"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6095"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6097"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6100"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6102"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7004",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5008"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5027",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6161",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7223", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7017", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7018", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5018",
    browseName="ns=plastics_extrusion_calibrator;AirShowerPressure",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6041",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6042", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6043", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6107",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6120", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6121", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5025"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5026"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5027"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6044"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6104"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6108"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6110"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6113"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6115"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6117"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6122"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6124"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6159"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6162"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6164"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7008",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5005",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6033",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7224", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7021", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7022", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5001",
    browseName="ns=plastics_extrusion_calibrator;Vacuum",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6003",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6004", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6005", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6012",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6025", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6026", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5003"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5005"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6006"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6008"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6013"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6018"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6020"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6022"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6027"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6029"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6031"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6034"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6036"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7002",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5001"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5030",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6276",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7225", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7025", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7026", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5019",
    browseName="ns=plastics_extrusion_calibrator;Vacuum",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6050",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6051", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6052", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6215",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6265", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6266", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5028"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5029"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5030"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6048"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6212"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6219"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6222"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6256"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6259"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6262"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6267"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6270"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6273"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6277"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6280"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7024",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5044",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6360",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7226", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7071", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7072", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5037",
    browseName="ns=plastics_extrusion_calibrator;WaterFlow",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6325",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6326", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6327", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6339",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6352", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6353", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5039"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5043"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5044"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6328"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6336"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6340"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6342"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6345"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6347"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6349"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6354"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6356"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6358"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6361"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6363"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7030",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5037"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5066",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6379",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7227", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7043", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7044", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5021",
    browseName="ns=plastics_extrusion_calibrator;WaterFlow",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6056",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6057", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6058", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6286",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6368", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6369", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5031"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5065"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5066"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6054"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6283"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6290"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6293"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6304"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6307"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6365"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6370"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6373"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6376"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6380"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6429"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7032",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5047",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6465",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7228", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7077", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7078", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5038",
    browseName="ns=plastics_extrusion_calibrator;WaterLevel",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6331",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6332", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6333", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6444",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6457", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6458", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5045"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5046"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5047"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6334"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6441"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6445"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6447"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6450"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6452"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6454"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6459"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6461"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6463"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6466"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6468"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7042",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5038"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5069",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6761",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7229", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7079", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7080", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5022",
    browseName="ns=plastics_extrusion_calibrator;WaterLevel",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6067",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6126", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6127", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6435",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6727", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6728", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5067"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5068"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5069"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6059"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6432"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6440"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6472"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6483"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6721"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6724"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6729"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6732"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6735"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6762"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6765"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7076",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5015",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6174",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7230", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7085", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7086", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5007",
    browseName="ns=plastics_extrusion_calibrator;WaterTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6062",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6063", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6064", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6135",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6148", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6149", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5013"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5014"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6065"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6132"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6136"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6138"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6141"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6143"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6145"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6150"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6152"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6154"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6175"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6177"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7014",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5007"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5072",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6831",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7231", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7089", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7090", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5024",
    browseName="ns=plastics_extrusion_calibrator;WaterTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6156",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6157", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6158", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6771",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6820", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6821", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5070"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5071"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5072"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6129"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6768"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6775"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6778"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6789"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6814"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6817"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6822"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6825"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6828"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6832"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6835"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7088",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_extrusion_calibrator_objtypes.CalibrationZoneType(
    nodeId="ns=plastics_extrusion_calibrator;i=5016",
    browseName="ns=plastics_extrusion_calibrator;CalibrationZone_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6038", browseName="ns=plastics_extrusion_calibrator;IsPresent", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6039", browseName="ns=plastics_extrusion_calibrator;Name", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6047", browseName="ns=plastics_extrusion_calibrator;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5017"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5018"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5020"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5021"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5022"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5023"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5024"]),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5016"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5057",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6589",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7232", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7097", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7098", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5049",
    browseName="ns=plastics_extrusion_calibrator;WaterFlowOut",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6491",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6492", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6493", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6568",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6581", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6582", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5055"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5056"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5057"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6494"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6565"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6569"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6571"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6574"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6576"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6578"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6583"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6585"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6587"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6590"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6592"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7054",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5049"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5082",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6955",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7233", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7102", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7103", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5074",
    browseName="ns=plastics_extrusion_calibrator;WaterFlowOut",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6560",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6561", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6562", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6597",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6885", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6886", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5080"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5081"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5082"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6558"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6594"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6598"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6600"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6603"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6605"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6607"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6887"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6889"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6953"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6956"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6958"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7056",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5060",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6634",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7234", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7133", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7134", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5050",
    browseName="ns=plastics_extrusion_calibrator;WaterTemperatureIn",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6496",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6497", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6498", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6613",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6626", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6627", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5058"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5059"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5060"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6499"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6610"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6614"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6616"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6619"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6621"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6623"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6628"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6630"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6632"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6635"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6637"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7060",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5050"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5085",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7064",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7235", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7160", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7161", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5075",
    browseName="ns=plastics_extrusion_calibrator;WaterTemperatureIn",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6644",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6645",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6646", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6647", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6660", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6661", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5083"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5084"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5085"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6639"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6641"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6648"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6650"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6653"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6655"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6657"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6890"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6892"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6894"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7062",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7106"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7108"]),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5054",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6530",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7236", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7091", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7092", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5048",
    browseName="ns=plastics_extrusion_calibrator;WaterFlowIn",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6486",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6487", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6488", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6509",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6522", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6523", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5052"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5053"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5054"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6489"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6506"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6510"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6512"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6515"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6517"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6519"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6524"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6526"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6528"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6531"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6533"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7048",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5048"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5079",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6901",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7237", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7095", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7096", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5073",
    browseName="ns=plastics_extrusion_calibrator;WaterFlowIn",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6540",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6541",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6542", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6543", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6556", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6557", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5077"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5078"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5079"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6535"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6537"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6544"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6546"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6549"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6551"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6553"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6880"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6882"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6884"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6902"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6904"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7050",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5063",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6686",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7238", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7191", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7192", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5051",
    browseName="ns=plastics_extrusion_calibrator;WaterTemperatureOut",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6501",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6502", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6503", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6665",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6678", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6679", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5061"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5062"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5063"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6504"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6662"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6666"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6668"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6671"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6673"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6675"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6680"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6682"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6684"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6687"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6689"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7066",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.CalibrationZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5051"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5088",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7070",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7239", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7218", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7219", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5076",
    browseName="ns=plastics_extrusion_calibrator;WaterTemperatureOut",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6696",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6697",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6698", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6699", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6712", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6713", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5086"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5087"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5088"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6691"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6693"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6700"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6702"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6705"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6707"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6709"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6895"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6897"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6899"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7068",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7164"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=7166"]),
    ],
)
plastics_extrusion_calibrator_objtypes.CalibrationZonesType(
    nodeId="ns=plastics_extrusion_calibrator;i=5036",
    browseName="ns=plastics_extrusion_calibrator;CalibrationZones",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6329", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5073"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5074"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5075"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5076"]),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.Calibrator_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5036"])
o6.reference(o6.ns["ns=plastics_extrusion_calibrator;i=5036"], "i=41", "i=2133")
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5042",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6400",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=7240", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7039", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_calibrator;i=7040", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_calibrator;i=5032",
    browseName="ns=plastics_extrusion_calibrator;PositionZ",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6310",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6311", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6312", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6313", browseName="ns=plastics_rubber;Position", dataType=o6.String, value="")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_calibrator;i=6322",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calibrator;i=6393", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5040"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5041"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=5042"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6314"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6319"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6381"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6383"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6386"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6388"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6390"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6394"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6396"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6398"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6401"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_calibrator;i=6403"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_calibrator;i=7036",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_calibrator_objtypes.Calibrator_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_calibrator;i=5032"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_extrusion, plastics_rubber, plastics_extrusion_calibrator_objtypes
