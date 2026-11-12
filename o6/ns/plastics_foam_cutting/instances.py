# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA plastics_foam_cutting namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_foam_cutting_datypes
from . import objtypes as plastics_foam_cutting_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_foam_cutting;i=5073", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_foam_cutting;i=5074", browseName="Default XML")
o6.hasEncoding(plastics_foam_cutting_datypes.ActiveVacuumUnitsDataType, o6.ns["ns=plastics_foam_cutting;i=5074"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6001",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Off"), description=o6.LocalizedText("The grinding unit is switched off.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Standby"), description=o6.LocalizedText("The grinding unit is in standby mode.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Running"), description=o6.LocalizedText("The grinding unit is running.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6008",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("The machine has no bottom fixture.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Mechanical_Fixture"), description=o6.LocalizedText("The material is fixed to the bottom in a mechanical way.")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Vacuum_Fixture"), description=o6.LocalizedText("The material is fixed to the bottom by vacuum.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6009",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("The machine has no side fixture.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Right"), description=o6.LocalizedText("The material is fixed on the right side.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Left"), description=o6.LocalizedText("The material is fixed on the left side.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Both"), description=o6.LocalizedText("The material is fixed on both sides.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6010",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("The machine has no top fixture.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Pressure_Pad"), description=o6.LocalizedText("The top fixture is a pressure pad.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Pressure_Roller"), description=o6.LocalizedText("The top fixture is a pressure roller.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6011",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("The machine has no material support system, the material must be fed in accordingly.")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Fixed_Machine_Table"), description=o6.LocalizedText("The material support system is a fixed machine table.")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("Sliding_Machine_Table"), description=o6.LocalizedText("The material support system is a sliding machine table.")
        ),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Carousel"), description=o6.LocalizedText("The material support system is a carousel.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Conveyor_Belt"), description=o6.LocalizedText("The material support system is a conveyor belt.")),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("Turntable_90Degrees"), description=o6.LocalizedText("The material support system is a turntable, which can rotate 90 degrees.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6012",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Forwards"), description=o6.LocalizedText("The conveyor’s working direction is forwards.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Backwards"), description=o6.LocalizedText("The conveyor’s working direction is backwards.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Reversible"), description=o6.LocalizedText("The conveyor’s working direction is reversible.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Sidewards"), description=o6.LocalizedText("The conveyor’s working direction is sidewards.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Any"), description=o6.LocalizedText("Any conveyor direction is possible.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6013",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("No light barrier.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Infeed"), description=o6.LocalizedText("Light barrier is positioned infeed.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Outfeed"), description=o6.LocalizedText("Light barrier is positioned outfeed.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Safety"), description=o6.LocalizedText("Light barrier is a safety device.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("None of the other values fit.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6014",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("None of the other categories fit.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AlignmentBelt"), description=o6.LocalizedText("The conveyor is an alignment belt.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Turntable"), description=o6.LocalizedText("The conveyor is a turntable.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Seperator"), description=o6.LocalizedText("The conveyor is a separator.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Stacker"), description=o6.LocalizedText("The conveyor is a stacker.")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Destacker"), description=o6.LocalizedText("The conveyor is a destacker.")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("PopUp"), description=o6.LocalizedText("The conveyor is a pop-up conveyor.")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ScissorTable"), description=o6.LocalizedText("The conveyor is a scissor table.")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("CrossConveyor"), description=o6.LocalizedText("The conveyor is a cross-conveyor.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6015",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Loading"), description=o6.LocalizedText("Loading of material for processing.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Unloading"), description=o6.LocalizedText("Unloading of material after processing.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Transportation"), description=o6.LocalizedText("Transportation of material during processing.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6022",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Manual"), description=o6.LocalizedText("Machine is in manual mode")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("SemiAutomatic"), description=o6.LocalizedText("Machine is in semi-automatic mode")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Automatic"), description=o6.LocalizedText("Machine is in automatic mode")),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5002",
    browseName="ns=plastics_foam_cutting;JobInformation",
    description="The instances of this ObjectType provide information about the current job.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6024",
                browseName="ns=plastics_foam_cutting;JobName",
                description="Provides information about the current job name.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6025",
                browseName="ns=plastics_foam_cutting;FinishedParts",
                description="Provides a counter for finished parts, e.g. sheets.",
                dataType=o6.UInt32,
            )
        ),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5002"])
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5001",
    browseName="ns=plastics_foam_cutting;PeripheralDevices",
    description="Folder containing information about the active state of peripheral devices.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6026",
                browseName="ns=plastics_foam_cutting;<Device_Nr>",
                description="Provides information, if the peripheral device is active or not. Further information shall be provided in the Description NodeAttribute.",
                modellingRule="OptionalPlaceholder",
                dataType=o6.Boolean,
            )
        )
    ],
)
o6.reference(plastics_foam_cutting_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5001"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_foam_cutting;i=6030",
    browseName="EnumValues",
    parent="ns=plastics_foam_cutting;i=3030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Forward"), description=o6.LocalizedText("Transportation direction is forward.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Backward"), description=o6.LocalizedText("Transportation direction is backward.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Sideward"), description=o6.LocalizedText("Transportation direction is sideward.")),
    ],
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_foam_cutting;i=5005",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6033", browseName="NodeVersion", dataType=o6.String, value=""))],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6041",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6042", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6112", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6113", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6114", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6115", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6043",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6044", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6116", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6117", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6118", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6119", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6045",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6046", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6120", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6121", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6122", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6123", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5006",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6041"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6043"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6045"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6047", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6049",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6050", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6124", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6125", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6126", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6127", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6051",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6052", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6128", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6130", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6131", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6053",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6054", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6132", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6133", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6134", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6135", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6036",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6037", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6136", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6137", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6138", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6139", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6055",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6056", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6057", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6140", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6141", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6059",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6060", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6142", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6143", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6144", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6145", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6061",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6062", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6146", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6147", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6148", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6149", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6063",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6064", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6150", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6151", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6152", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6153", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6065",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6154", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6156", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6157", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6067",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6068", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6069", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6158", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6159", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6070",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6071", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6160", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6161", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6162", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6163", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6072",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6073", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6164", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6165", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6166", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6167", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6074",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6075", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6168", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6169", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6170", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6171", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6076",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6077", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6078", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6172", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6173", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6079",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6080", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6174", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6175", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6176", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6177", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6081",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6082", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6178", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6179", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6180", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6181", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6039",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6040", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6182", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6184", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6185", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6084",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6085", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6086", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6186", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6187", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6088",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6089", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6188", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6189", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6190", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6191", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6090",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6091", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6192", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6193", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6194", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6195", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6092",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6093", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6196", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6197", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6198", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6199", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6094",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6095", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6200", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6201", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6202", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6203", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6096",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6097", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6098", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6204", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6205", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6099",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6100", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6206", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6207", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6208", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6209", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6101",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6102", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6210", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6212", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6213", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6103",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6104", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6214", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6215", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6216", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6217", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6105",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6106", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6107", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6218", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6219", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6108",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6109", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6220", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6221", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6222", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6223", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6110",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6111", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6224", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6225", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6226", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6227", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6027",
    browseName="ns=plastics_foam_cutting;Speed",
    description="Linear speed in the direction of material flow.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6028", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6228", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6229", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6230", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6231", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_foam_cutting_objtypes.ConveyorProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=6027"])
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_foam_cutting;i=5020",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6233", browseName="NodeVersion", dataType=o6.String, value=""))],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6241",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6242", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6312", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6313", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6314", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6315", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6243",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6244", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6316", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6317", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6318", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6319", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6245",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6246", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6320", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6321", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6322", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6323", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5021",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6241"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6243"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6245"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6247", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6249",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6250", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6324", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6325", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6326", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6327", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6251",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6252", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6328", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6329", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6330", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6331", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6253",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6254", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6332", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6333", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6334", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6335", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6236",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6237", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6336", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6337", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6338", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6339", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6255",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6256", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6257", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6340", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6341", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6259",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6260", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6342", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6343", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6344", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6345", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6261",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6262", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6346", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6347", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6348", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6349", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6263",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6350", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6351", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6352", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6353", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6265",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6266", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6354", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6355", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6356", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6357", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6267",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6268", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6269", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6358", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6359", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6270",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6271", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6360", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6361", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6362", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6363", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6272",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6273", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6364", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6365", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6366", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6367", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6274",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6275", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6368", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6369", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6370", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6371", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6276",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6277", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6278", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6372", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6373", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6279",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6280", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6374", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6375", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6376", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6377", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6281",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6282", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6378", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6379", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6380", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6381", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6239",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6240", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6382", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6383", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6384", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6385", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6284",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6285", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6286", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6386", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6387", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6288",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6289", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6388", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6389", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6390", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6391", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6290",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6291", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6392", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6393", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6394", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6395", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6292",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6293", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6396", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6397", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6398", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6399", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6294",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6295", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6400", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6401", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6402", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6403", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6296",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6297", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6298", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6404", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6405", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6299",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6300", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6406", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6407", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6408", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6409", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6301",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6302", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6410", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6411", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6412", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6413", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6303",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6304", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6414", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6415", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6416", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6417", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6305",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6306", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6307", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6418", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6419", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6308",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6309", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6420", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6421", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6422", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6423", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6310",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6311", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6424", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6425", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6426", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6427", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5027",
    browseName="ns=plastics_foam_cutting;Drives",
    description="Drives is a container object for all drives of the conveyor.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6430", browseName="NodeVersion", dataType=o6.String))],
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5029",
    browseName="ns=plastics_foam_cutting;GrindDrives",
    description="Provides information about the grind drives including the grinding unit speed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6434", browseName="NodeVersion", dataType=o6.String))],
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5030",
    browseName="ns=plastics_foam_cutting;KnifeDrives",
    description="Provides information about the drives of the knife.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6436", browseName="NodeVersion", dataType=o6.String))],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6437",
    browseName="ns=plastics_foam_cutting;KnifeSpeed",
    description="Provides the set value of the knife.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6438", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6442", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6443", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6444", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6445", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6439",
    browseName="ns=plastics_foam_cutting;Readjustment",
    description="Provides information about the mechanical adjustment in the mounting position of the knife to compensate for wear.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6440", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6446", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6447", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6448", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6449", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6451",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6452", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6457", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6458", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6459", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6460", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6453",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6454", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6461", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6462", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6463", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6464", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6455",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6456", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6465", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6466", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6467", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6468", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_foam_cutting;i=5033",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6469", browseName="NodeVersion", dataType=o6.String, value=""))],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6477",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6478", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6548", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6549", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6550", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6551", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6479",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6480", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6552", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6553", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6554", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6555", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6481",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6482", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6556", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6557", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6558", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6559", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5034",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6477"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6479"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6481"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6483", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6485",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6486", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6560", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6561", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6562", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6563", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6487",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6488", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6564", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6565", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6566", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6567", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6489",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6490", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6568", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6569", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6570", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6571", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6472",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6473", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6572", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6573", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6574", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6575", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6491",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6492", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6493", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6576", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6577", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6495",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6496", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6578", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6579", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6580", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6581", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6497",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6498", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6582", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6583", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6584", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6585", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6499",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6500", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6586", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6587", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6588", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6589", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6501",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6502", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6590", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6591", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6592", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6593", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6503",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6504", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6505", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6594", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6595", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6506",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6507", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6596", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6597", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6598", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6599", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6508",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6509", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6600", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6601", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6602", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6603", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6510",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6511", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6604", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6605", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6606", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6607", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6512",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6513", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6514", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6608", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6609", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6515",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6516", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6610", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6611", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6612", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6613", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6517",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6518", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6614", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6615", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6616", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6617", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6475",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6476", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6618", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6619", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6620", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6621", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6520",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6521", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6522", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6622", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6623", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6524",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6525", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6624", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6625", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6626", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6627", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6526",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6527", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6628", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6629", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6630", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6631", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6528",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6529", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6632", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6633", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6634", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6635", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6530",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6531", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6636", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6637", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6638", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6639", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6532",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6533", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6534", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6640", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6641", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6535",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6536", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6642", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6643", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6644", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6645", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6537",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6538", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6646", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6647", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6648", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6649", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6539",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6540", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6650", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6651", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6652", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6653", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=6541",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6542", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6543", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6654", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6655", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6544",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6545", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6656", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6657", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6658", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6659", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6546",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6547", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6660", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6661", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6662", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6663", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6676",
    browseName="ns=plastics_foam_cutting;CurrentValue",
    description="Provides the current actual cutting speed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6677", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6678", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6679", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6680", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6681", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6668",
    browseName="ns=plastics_foam_cutting;MaxMachineLimit",
    description="The maximum mechanicaly achievable speed by the machine due to the drive, gears and other moving parts. The value applies for cutting and idle speed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6669", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6682", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6683", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6684", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6685", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6670",
    browseName="ns=plastics_foam_cutting;RecipeLimit",
    description="Provides the order (recipe) specific limit of the cutting speed when the knife is cutting material.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6671", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6686", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6687", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6688", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6689", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6672",
    browseName="ns=plastics_foam_cutting;RecipeLimitIdle",
    description="Provides the order (recipe) specific limit of the return speed of the knife to cut start position.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6673", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6690", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6691", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6692", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6693", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5013",
    browseName="ns=plastics_foam_cutting;CuttingSpeedFeed",
    description="The rate at which the material is cut, which would depend e.g. on the feed of the material, the speed and sharpness of the knife.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6668"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6670"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6672"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6674",
                browseName="ns=plastics_foam_cutting;Override",
                description="Provides the current override value in percent (e.g. 50 %), which is manually adjusted by the machine operator. The cutting speed setpoint calculates as follows: Setpoint = Override x RecipeLimit.",
                dataType=o6.Double,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6675", browseName="ns=plastics_foam_cutting;OverrideIdle", description="Same as override but for idle speed.", dataType=o6.Double
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6676"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.ProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5013"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6696",
    browseName="ns=plastics_foam_cutting;CuttingAngle",
    description="Provides the current cutting angle in degrees (°).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6697", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6702", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6703", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6704", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6705", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6694",
    browseName="ns=plastics_foam_cutting;CuttingThickness",
    description="Provides the set value of the cutting thickness.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6695", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6706", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6707", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6708", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6709", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6698",
    browseName="ns=plastics_foam_cutting;CuttingUnitPosition",
    description="Provides the current position of the cutting unit relative to a machine-specific reference point and range, where both zero and maximum values are machine-specific.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6710", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6711", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6712", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6713", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6700",
    browseName="ns=plastics_foam_cutting;PressureRollerOffset",
    description="Provides the offset of the pressure roller. Positive values mean offset inside the material.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6701", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6714", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6715", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6716", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6717", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6721",
    browseName="ns=plastics_foam_cutting;Orientation",
    description="Provides information about the actual orientation in degrees (°) of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6722", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6723", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6724", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6725", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6726", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5015",
    browseName="ns=plastics_foam_cutting;MaterialSupport",
    description="Provides the process values of the material support system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6718",
                browseName="ns=plastics_foam_cutting;ActiveVacuumUnits",
                description="Information about the activity of the vacuum units. The array length shall match the total number of vacuum units given in the VacuumUnitsQuantity Property in the MachineConfigurationType.",
                dataType=plastics_foam_cutting_datypes.ActiveVacuumUnitsDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6719",
                browseName="ns=plastics_foam_cutting;SideFixtureActive",
                description="Indicates if the side fixture is active (true) or not (false).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6720",
                browseName="ns=plastics_foam_cutting;TopFixtureActive",
                description="Indicates if the top fixture is active (true) or not (false).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6721"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.ProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5015"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6727",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6728", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6734", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6735", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6736", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6737", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6729",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6730", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6738", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6739", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6740", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6741", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6731",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6732", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6742", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6743", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6744", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6745", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5036",
    browseName="ns=plastics_foam_cutting;CompressedAir",
    description="Provides information about the compressed air consumption of the machine.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6727"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6729"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6731"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6733", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6746",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6747", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6753", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6754", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6755", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6756", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6748",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6749", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6757", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6758", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6759", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6760", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6750",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6751", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6761", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6762", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6763", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6764", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5037",
    browseName="ns=plastics_foam_cutting;Electricity",
    description="Provides information about the electrical energy consumption of the machine.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6746"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6748"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6750"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6752", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5016",
    browseName="ns=plastics_foam_cutting;Supply",
    description="Provides information about the energy consumption of the machine.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5036"]), o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5037"])],
)
o6.reference(plastics_foam_cutting_objtypes.ProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5016"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6767",
    browseName="ns=plastics_foam_cutting;ActualFoilLength",
    description="Provides the actual foil length.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6768", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6773", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6774", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6775", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6776", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6771",
    browseName="ns=plastics_foam_cutting;SpeedOffset",
    description="Provides the speed offset of the winder. Positive values mean the winder speed is higher than the material feed speed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6772", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6777", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6778", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6779", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6780", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6765",
    browseName="ns=plastics_foam_cutting;TargetFoilLength",
    description="Provides the set value (target) of the foil length.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6766", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6781", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6782", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6783", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6784", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5017",
    browseName="ns=plastics_foam_cutting;WindingSystem",
    description="Provides information about a winding system installed on the machine.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6765"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6767"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6769",
                browseName="ns=plastics_foam_cutting;RollCounter",
                description="Provides the total number of wound rolls.",
                dataType=o6.UInt32,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6770",
                browseName="ns=plastics_foam_cutting;RollStop",
                description="Provides the time stamp of the last finished roll.",
                dataType=ns0.datatypes.UtcTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6771"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.ProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5017"])
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5038",
    browseName="ns=plastics_foam_cutting;Fixture",
    description="Fixture is an instance declaration of the 0:FolderType. It provides a folder to organize the child nodes that represent the different material fixture systems for the material top, bottom and sides.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6787",
                browseName="ns=plastics_foam_cutting;TopFixture",
                description="Provides information about the type of material fixture for the material top.",
                dataType=plastics_foam_cutting_datypes.TopFixtureEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6788",
                browseName="ns=plastics_foam_cutting;SideFixture",
                description="Provides information about the type of material fixture for the material side.",
                dataType=plastics_foam_cutting_datypes.SideFixtureEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6789",
                browseName="ns=plastics_foam_cutting;BottomFixture",
                description="Provides information about the type of material fixture for the material bottom.",
                dataType=plastics_foam_cutting_datypes.BottomFixtureEnumeration,
            )
        ),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.MaterialSupportType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5038"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6796",
    browseName="ns=plastics_foam_cutting;Diameter",
    description="Provides the diameter of the material support system, e.g. for a turntable.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6797", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6798", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6799", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6800", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6801", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6794",
    browseName="ns=plastics_foam_cutting;Height",
    description="Provides the width of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6795", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6802", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6803", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6804", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6805", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6790",
    browseName="ns=plastics_foam_cutting;Length",
    description="Provides the lengths of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6791", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6806", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6807", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6808", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6809", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6792",
    browseName="ns=plastics_foam_cutting;Width",
    description="Provides the width of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6793", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6810", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6811", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6812", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6813", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5039",
    browseName="ns=plastics_foam_cutting;TableDimensions",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6790"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6792"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6794"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6796"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.MaterialSupportType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5039"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=plastics_foam_cutting;i=6818",
    browseName="ns=plastics_foam_cutting;ConveyorSpeed",
    description="This Variable provides information about the speed settings of the conveyor. If FixedSpeedConveyor is true, this Variable provides the set value. If FixedSpeedConveyor is false, this Variable provides the speed range of the conveyor.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6819", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6820", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6828", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6829", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6830", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_foam_cutting_objtypes.ConveyorConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=6818"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6821",
    browseName="ns=plastics_foam_cutting;Length",
    description="Length of the conveyor.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6822", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6831", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6832", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6833", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6834", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_foam_cutting_objtypes.ConveyorConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=6821"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6823",
    browseName="ns=plastics_foam_cutting;Width",
    description="Width of the conveyor.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6824", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6835", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6836", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6837", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6838", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_foam_cutting_objtypes.ConveyorConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=6823"])
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5042",
    browseName="ns=plastics_foam_cutting;Fixture",
    description="Fixture is an instance declaration of the 0:FolderType. It provides a folder to organize the child nodes that represent the different material fixture systems for the material top, bottom and sides.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6841",
                browseName="ns=plastics_foam_cutting;BottomFixture",
                description="Provides information about the type of material fixture for the material bottom.",
                dataType=plastics_foam_cutting_datypes.BottomFixtureEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6842",
                browseName="ns=plastics_foam_cutting;SideFixture",
                description="Provides information about the type of material fixture for the material side.",
                dataType=plastics_foam_cutting_datypes.SideFixtureEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6843",
                browseName="ns=plastics_foam_cutting;TopFixture",
                description="Provides information about the type of material fixture for the material top.",
                dataType=plastics_foam_cutting_datypes.TopFixtureEnumeration,
            )
        ),
    ],
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=plastics_foam_cutting;i=6846",
    browseName="ns=plastics_foam_cutting;ConveyorSpeed",
    description="This Variable provides information about the speed settings of the conveyor. If FixedSpeedConveyor is true, this Variable provides the set value. If FixedSpeedConveyor is false, this Variable provides the speed range of the conveyor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6847", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6848", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6859", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6860", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6861", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6852",
    browseName="ns=plastics_foam_cutting;Length",
    description="Length of the conveyor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6853", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6862", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6863", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6864", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6865", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6857",
    browseName="ns=plastics_foam_cutting;Width",
    description="Width of the conveyor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6858", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6866", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6867", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6868", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6869", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6870",
    browseName="ns=plastics_foam_cutting;Diameter",
    description="Provides the diameter of the material support system, e.g. for a turntable.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6871", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6878", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6879", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6880", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6881", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6872",
    browseName="ns=plastics_foam_cutting;Height",
    description="Provides the width of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6873", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6882", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6883", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6884", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6885", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6874",
    browseName="ns=plastics_foam_cutting;Length",
    description="Provides the lengths of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6875", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6886", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6887", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6888", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6889", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6876",
    browseName="ns=plastics_foam_cutting;Width",
    description="Provides the width of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6877", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6890", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6891", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6892", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6893", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5043",
    browseName="ns=plastics_foam_cutting;TableDimensions",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6870"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6872"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6874"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6876"]),
    ],
)
plastics_foam_cutting_objtypes.MaterialSupportType(
    nodeId="ns=plastics_foam_cutting;i=5041",
    browseName="ns=plastics_foam_cutting;MaterialSupport",
    description="An instance declaration of MaterialSupportType.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6844",
                browseName="ns=plastics_foam_cutting;MaterialSupportCategory",
                description="This Property provides information about the category of the material support system.",
                dataType=plastics_foam_cutting_datypes.MaterialSupportCategoryEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6894",
                browseName="ns=plastics_foam_cutting;VacuumUnitsQuantity",
                description="This Property provides information about the total number of vacuum units on the material support system.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5042"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5043"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.MachineConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5041"])
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5049",
    browseName="ns=plastics_foam_cutting;Fixture",
    description="Fixture is an instance declaration of the 0:FolderType. It provides a folder to organize the child nodes that represent the different material fixture systems for the material top, bottom and sides.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6900",
                browseName="ns=plastics_foam_cutting;BottomFixture",
                description="Provides information about the type of material fixture for the material bottom.",
                dataType=plastics_foam_cutting_datypes.BottomFixtureEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6901",
                browseName="ns=plastics_foam_cutting;SideFixture",
                description="Provides information about the type of material fixture for the material side.",
                dataType=plastics_foam_cutting_datypes.SideFixtureEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6902",
                browseName="ns=plastics_foam_cutting;TopFixture",
                description="Provides information about the type of material fixture for the material top.",
                dataType=plastics_foam_cutting_datypes.TopFixtureEnumeration,
            )
        ),
    ],
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=plastics_foam_cutting;i=5046",
    browseName="ns=di;Identification",
    description="The MachineIdentificationType is defined in OPC UA for Machinery (OPC 40001-1) and provides basic information on a machine/device.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6895",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6896",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6897",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6912",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6913",
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
                nodeId="ns=plastics_foam_cutting;i=6914",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6915",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6916",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6917",
                browseName="ns=machinery;Location",
                description="To be used by end users to store the location of the machine in a scheme specific to the end user. Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6918",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6919",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6920",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6921",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6922",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6924",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(
            di.vartypes.UIElementType(
                nodeId="ns=plastics_foam_cutting;i=6923", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True
            )
        ),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.FoamCuttingMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=plastics_foam_cutting;i=5046"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=plastics_foam_cutting;i=6925",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6926", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6929", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6930", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6931", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=plastics_foam_cutting;i=6934",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6935", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6936", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6937", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6938", browseName="Number", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6939", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=plastics_foam_cutting;i=5063",
    browseName="ns=machinery;MachineryItemState",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6925"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6932", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6933", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6934"]),
    ],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=plastics_foam_cutting;i=6940",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6941", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6942", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6943", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6944", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6431",
    browseName="ns=plastics_foam_cutting;Speed",
    description="Linear speed in the direction of material flow.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6432", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6927", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6928", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6945", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6946", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=plastics_foam_cutting;i=6967",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6968", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6969", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6970", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6971", browseName="Number", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6972", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=plastics_foam_cutting;i=5064",
    browseName="ns=machinery;MachineryOperationMode",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6940"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6965", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=6966", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6967"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5045",
    browseName="ns=machinery;MachineryBuildingBlocks",
    description="The Object MachineryBuildingBlocks contains building blocks from OPC UA for Machinery as defined in OPC 40001-1.",
    modellingRule="Mandatory",
    references=[o6.hasAddIn(o6.ns["ns=plastics_foam_cutting;i=5063"]), o6.hasAddIn(o6.ns["ns=plastics_foam_cutting;i=5064"])],
)
o6.reference(plastics_foam_cutting_objtypes.FoamCuttingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5045"])
o6.reference(o6.ns["ns=plastics_foam_cutting;i=5045"], "i=17604", o6.ns["ns=plastics_foam_cutting;i=5046"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=plastics_foam_cutting;i=6950",
    browseName="ns=plastics_foam_cutting;ConveyorSpeed",
    description="This Variable provides information about the speed settings of the conveyor. If FixedSpeedConveyor is true, this Variable provides the set value. If FixedSpeedConveyor is false, this Variable provides the speed range of the conveyor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6951", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6952", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6963", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6964", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6973", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6956",
    browseName="ns=plastics_foam_cutting;Length",
    description="Length of the conveyor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6957", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6974", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6975", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6976", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6977", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6961",
    browseName="ns=plastics_foam_cutting;Width",
    description="Width of the conveyor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6962", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6978", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6979", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6980", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6981", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
plastics_foam_cutting_objtypes.ErrorHandlingType(
    nodeId="ns=plastics_foam_cutting;i=5062",
    browseName="ns=plastics_foam_cutting;ErrorHandling",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6911",
                browseName="ns=plastics_foam_cutting;ActiveErrors",
                description="List of the active errors of the device.",
                dataType=plastics_rubber.datatypes.ActiveErrorDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6982",
                browseName="ns=plastics_foam_cutting;HighestActiveAlarmSeverity",
                description="Indication of the severity of the highest active alarm.",
                dataType=o6.UInt16,
            )
        ),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.FoamCuttingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5062"])
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5087",
    browseName="ns=plastics_foam_cutting;PeripheralDevices",
    description="Folder containing information about the active state of peripheral devices.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6983", browseName="ns=plastics_foam_cutting;<Device_Nr>", modellingRule="OptionalPlaceholder", dataType=o6.Boolean
            )
        )
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6908",
    browseName="ns=plastics_foam_cutting;Speed",
    description="Linear speed in the direction of material flow.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6909", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6984", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6985", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6986", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6987", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_foam_cutting;i=5067",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6988", browseName="NodeVersion", dataType=o6.String, value=""))],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6991",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6992", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5070", browseName="ns=plastics_rubber;Speed", references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6991"])]
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_foam_cutting;i=5071",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6993",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        )
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=6994",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6995", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5072", browseName="ns=plastics_rubber;Torque", references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6994"])]
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5022",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6234",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6248",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6249"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6251"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6253"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7001",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5023",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6258",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6236"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6255"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6259"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6261"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6263"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6265"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6267"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6270"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6272"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6274"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6276"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6279"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6281"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7002",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5007",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6034",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6048",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6049"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6051"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6053"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7003",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5008",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6058",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6036"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6055"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6059"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6061"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6063"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6065"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6067"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6070"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6072"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6074"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6076"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6079"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6081"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7004",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_foam_cutting;i=5009",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6038",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6083", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7005", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7006", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5010",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6087",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6039"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6084"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6088"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6090"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6092"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6094"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6096"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6099"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6101"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6103"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6105"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6108"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6110"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7007",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_foam_cutting;i=5004",
    browseName="ns=plastics_foam_cutting;<Drive_Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6035", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5005"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5006"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5007"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5008"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5009"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5010"]),
    ],
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5003",
    browseName="ns=plastics_foam_cutting;Drives",
    description="Drives is a container object for all drives of the conveyor.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6031", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5004"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.ConveyorProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5003"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_foam_cutting;i=5024",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6238",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6283", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7008", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7009", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5025",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6287",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6239"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6284"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6288"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6290"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6292"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6294"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6296"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6299"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6301"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6303"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6305"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6308"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6310"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7010",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_foam_cutting;i=5019",
    browseName="ns=plastics_foam_cutting;<Name>_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6235", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5020"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5021"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5022"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5023"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5024"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5025"]),
    ],
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5018",
    browseName="ns=plastics_foam_cutting;MainAxisDrives",
    description="Container object for all main axis drives of the machines.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6232", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5019"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.ProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5018"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5069",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6989",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7011",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_foam_cutting;i=5066",
    browseName="ns=plastics_foam_cutting;<Name>_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6990", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5067"]),
        o6.hasComponent(plastics_rubber.objtypes.EnergyType(nodeId="ns=plastics_foam_cutting;i=5068", browseName="ns=plastics_rubber;Energy")),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5069"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5070"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5071"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5072"]),
    ],
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5058",
    browseName="ns=plastics_foam_cutting;MainAxisDrives",
    description="Container object for all main axis drives of the machines.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6910", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5066"]),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5031",
    browseName="ns=plastics_foam_cutting;WearStatus",
    description="Provides information about the wear status of the knife.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6441",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6450",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6451"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6453"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6455"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7013",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_foam_cutting_objtypes.KnifeType(
    nodeId="ns=plastics_foam_cutting;i=5028",
    browseName="ns=plastics_foam_cutting;<Knife_Nr>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5029"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5030"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5031"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6433",
                browseName="ns=plastics_foam_cutting;KnifeRunning",
                description="Indicates if the knife is switched on (true) or off (false).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6435",
                browseName="ns=plastics_foam_cutting;GrindingUnitState",
                description="Provides information about the current state of the grinding unit.",
                dataType=plastics_foam_cutting_datypes.GrindingUnitStateEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6437"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6439"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5012",
    browseName="ns=plastics_foam_cutting;Knifes",
    description="This folder contains process values of the knife.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5028"])],
)
o6.reference(plastics_foam_cutting_objtypes.ProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5012"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5035",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6470",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6484",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6485"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6487"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6489"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7014",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5078",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6494",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6472"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6491"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6495"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6497"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6499"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6501"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6503"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6506"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6508"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6510"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6512"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6515"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6517"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7015",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_foam_cutting;i=5079",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6474",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6519", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7016", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7017", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5080",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6523",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6475"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6520"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6524"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6526"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6528"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6530"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6532"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6535"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6537"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6539"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6541"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6544"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6546"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7018",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_foam_cutting;i=5032",
    browseName="ns=plastics_foam_cutting;PressureRollerDrive",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6471", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5033"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5034"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5035"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5078"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5079"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5080"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5014",
    browseName="ns=plastics_foam_cutting;CuttingUnitParameters",
    description="This folder contains the cutting unit parameters.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5032"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6694"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6696"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6698"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6700"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.ProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5014"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=6999",
    browseName="ns=plastics_foam_cutting;Diameter",
    description="Provides the diameter of the material support system, e.g. for a turntable.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7000", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7027", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7028", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7029", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7030", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7021",
    browseName="ns=plastics_foam_cutting;Height",
    description="Provides the width of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7022", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7031", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7032", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7033", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7034", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7023",
    browseName="ns=plastics_foam_cutting;Length",
    description="Provides the lengths of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7024", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7035", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7036", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7037", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7038", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7025",
    browseName="ns=plastics_foam_cutting;Width",
    description="Provides the width of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7026", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7039", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7040", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7041", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7042", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5050",
    browseName="ns=plastics_foam_cutting;TableDimensions",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6999"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7021"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7023"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7025"]),
    ],
)
plastics_foam_cutting_objtypes.MaterialSupportType(
    nodeId="ns=plastics_foam_cutting;i=5048",
    browseName="ns=plastics_foam_cutting;MaterialSupport",
    description="An instance declaration of MaterialSupportType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6903",
                browseName="ns=plastics_foam_cutting;MaterialSupportCategory",
                description="This Property provides information about the category of the material support system.",
                dataType=plastics_foam_cutting_datypes.MaterialSupportCategoryEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6998",
                browseName="ns=plastics_foam_cutting;VacuumUnitsQuantity",
                description="This Property provides information about the total number of vacuum units on the material support system.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5049"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5050"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5086",
    browseName="ns=plastics_foam_cutting;JobInformation",
    description="The instances of this ObjectType provide information about the current job.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7054",
                browseName="ns=plastics_foam_cutting;JobName",
                description="Provides information about the current job name.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7056",
                browseName="ns=plastics_foam_cutting;FinishedParts",
                description="Provides a counter for finished parts, e.g. sheets.",
                dataType=o6.UInt32,
            )
        ),
    ],
)
plastics_foam_cutting_objtypes.OperationType(
    nodeId="ns=plastics_foam_cutting;i=5051",
    browseName="ns=plastics_foam_cutting;Operation",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5086"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5087"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6904",
                browseName="ns=plastics_foam_cutting;ControlVoltageSwitch",
                description="Provides information, if the control voltage switch is switched on or off. The drives can only be operated with active control voltage.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6948", browseName="ns=plastics_foam_cutting;ProcessingMode", dataType=plastics_foam_cutting_datypes.ProcessingModeEnumeration
            )
        ),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.FoamCuttingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5051"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7057",
    browseName="ns=plastics_foam_cutting;CurrentValue",
    description="Provides the current actual cutting speed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7058", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7088", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7089", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7090", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7091", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7059",
    browseName="ns=plastics_foam_cutting;MaxMachineLimit",
    description="The maximum mechanicaly achievable speed by the machine due to the drive, gears and other moving parts. The value applies for cutting and idle speed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7060", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7092", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7093", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7094", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7095", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7063",
    browseName="ns=plastics_foam_cutting;RecipeLimit",
    description="Provides the order (recipe) specific limit of the cutting speed when the knife is cutting material.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7064", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7096", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7097", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7098", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7099", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7065",
    browseName="ns=plastics_foam_cutting;RecipeLimitIdle",
    description="Provides the order (recipe) specific limit of the return speed of the knife to cut start position.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7066", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7100", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7101", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7102", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7103", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5056",
    browseName="ns=plastics_foam_cutting;CuttingSpeedFeed",
    description="The rate at which the material is cut, which would depend e.g. on the feed of the material, the speed and sharpness of the knife.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7057"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7059"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7061",
                browseName="ns=plastics_foam_cutting;Override",
                description="Provides the current override value in percent (e.g. 50 %), which is manually adjusted by the machine operator. The cutting speed setpoint calculates as follows: Setpoint = Override x RecipeLimit.",
                dataType=o6.Double,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7062", browseName="ns=plastics_foam_cutting;OverrideIdle", description="Same as override but for idle speed.", dataType=o6.Double
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7063"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7065"]),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7067",
    browseName="ns=plastics_foam_cutting;CuttingAngle",
    description="Provides the current cutting angle in degrees (°).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7068", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7104", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7105", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7106", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7107", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7069",
    browseName="ns=plastics_foam_cutting;CuttingThickness",
    description="Provides the set value of the cutting thickness.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7070", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7108", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7109", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7110", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7111", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7071",
    browseName="ns=plastics_foam_cutting;CuttingUnitPosition",
    description="Provides the current position of the cutting unit relative to a machine-specific reference point and range, where both zero and maximum values are machine-specific.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7112", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7113", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7114", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7115", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7073",
    browseName="ns=plastics_foam_cutting;PressureRollerOffset",
    description="Provides the offset of the pressure roller. Positive values mean offset inside the material.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7074", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7116", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7117", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7118", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7119", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5057",
    browseName="ns=plastics_foam_cutting;CuttingUnitParameters",
    description="This folder contains the cutting unit parameters.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7067"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7069"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7071"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7073"]),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7076",
    browseName="ns=plastics_foam_cutting;Orientation",
    description="Provides information about the actual orientation in degrees (°) of the material support system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7077", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7120", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7121", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7122", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7123", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5059",
    browseName="ns=plastics_foam_cutting;MaterialSupport",
    description="Provides the process values of the material support system.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7075",
                browseName="ns=plastics_foam_cutting;ActiveVacuumUnits",
                description="Information about the activity of the vacuum units. The array length shall match the total number of vacuum units given in the VacuumUnitsQuantity Property in the MachineConfigurationType.",
                dataType=plastics_foam_cutting_datypes.ActiveVacuumUnitsDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7076"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7078",
                browseName="ns=plastics_foam_cutting;SideFixtureActive",
                description="Indicates if the side fixture is active (true) or not (false).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7079",
                browseName="ns=plastics_foam_cutting;TopFixtureActive",
                description="Indicates if the top fixture is active (true) or not (false).",
                dataType=o6.Boolean,
            )
        ),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7080",
    browseName="ns=plastics_foam_cutting;ActualFoilLength",
    description="Provides the actual foil length.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7138", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7139", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7140", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7141", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7084",
    browseName="ns=plastics_foam_cutting;SpeedOffset",
    description="Provides the speed offset of the winder. Positive values mean the winder speed is higher than the material feed speed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7085", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7142", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7143", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7144", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7145", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7086",
    browseName="ns=plastics_foam_cutting;TargetFoilLength",
    description="Provides the set value (target) of the foil length.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7087", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7146", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7147", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7148", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7149", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5061",
    browseName="ns=plastics_foam_cutting;WindingSystem",
    description="Provides information about a winding system installed on the machine.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7080"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7082",
                browseName="ns=plastics_foam_cutting;RollCounter",
                description="Provides the total number of wound rolls.",
                dataType=o6.UInt32,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=7083",
                browseName="ns=plastics_foam_cutting;RollStop",
                description="Provides the time stamp of the last finished roll.",
                dataType=ns0.datatypes.UtcTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7084"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7086"]),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7124",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7125", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7150", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7151", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7152", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7153", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7126",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7127", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7154", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7155", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7156", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7157", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7128",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7158", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7159", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7160", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7161", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5088",
    browseName="ns=plastics_foam_cutting;CompressedAir",
    description="Provides information about the compressed air consumption of the machine.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7124"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7126"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7128"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=7130", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7131",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7132", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7162", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7163", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7164", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7165", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7133",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7134", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7166", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7167", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7168", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7169", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7135",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7136", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7170", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7171", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7172", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7173", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5089",
    browseName="ns=plastics_foam_cutting;Electricity",
    description="Provides information about the electrical energy consumption of the machine.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7131"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7133"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7135"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=7137", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5060",
    browseName="ns=plastics_foam_cutting;Supply",
    description="Provides information about the energy consumption of the machine.",
    references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5088"]), o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5089"])],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7174",
    browseName="ns=plastics_foam_cutting;KnifeSpeed",
    description="Provides the set value of the knife.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7175", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7176",
    browseName="ns=plastics_foam_cutting;Readjustment",
    description="Provides information about the mechanical adjustment in the mounting position of the knife to compensate for wear.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7177", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_foam_cutting;i=5092",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7180", browseName="NodeVersion", dataType=o6.String, value=""))],
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_foam_cutting;i=5100",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7189", browseName="NodeVersion", dataType=o6.String, value=""))],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_foam_cutting;i=5104",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7195",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7241", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7242", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7243", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7198",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7199", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7273", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7274", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7275", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7276", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7200",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7201", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7277", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7278", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7279", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7280", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7202",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7203", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7281", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7282", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7283", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7284", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5101",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7198"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7200"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7202"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=7204", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7206",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7207", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7285", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7286", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7287", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7288", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7208",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7209", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7289", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7290", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7291", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7292", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7210",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7211", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7293", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7294", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7295", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7296", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5102",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7191",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7205",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7190",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7206"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7208"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7210"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7193",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7194", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7297", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7298", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7299", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7300", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7212",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7213", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7214", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7301", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7302", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7216",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7217", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7303", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7304", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7305", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7306", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7218",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7219", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7307", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7308", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7309", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7310", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7220",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7221", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7311", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7312", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7313", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7314", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7222",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7223", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7315", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7316", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7317", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7318", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7224",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7225", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7226", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7319", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7320", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7228",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7229", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7321", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7322", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7323", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7324", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7230",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7231", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7325", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7326", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7327", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7328", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7232",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7233", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7329", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7331", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7332", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7234",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7235", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7236", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7333", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7334", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7237",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7238", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7335", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7336", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7337", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7338", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7239",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7240", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7339", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7340", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7341", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7342", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5103",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7215",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7193"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7212"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7216"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7218"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7220"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7222"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7224"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7227",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7228"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7230"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7232"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7234"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7237"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7239"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7196",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7197", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7343", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7344", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7345", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7346", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7244",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7245", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7246", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7347", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7348", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7248",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7249", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7349", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7350", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7351", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7352", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7250",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7251", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7353", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7354", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7355", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7356", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7252",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7253", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7357", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7358", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7359", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7360", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7254",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7255", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7361", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7362", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7363", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7364", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7256",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7257", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7258", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7365", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7366", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7260",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7261", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7367", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7368", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7369", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7370", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7262",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7263", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7371", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7372", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7373", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7374", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7264",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7265", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7375", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7376", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7377", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7378", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7266",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7267", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7268", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7379", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7380", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7269",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7270", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7381", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7382", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7383", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7384", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7271",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7272", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7385", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7386", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7387", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7388", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5105",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7247",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7196"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7244"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7248"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7250"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7252"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7254"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7256"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7259",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7260"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7262"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7264"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7266"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7269"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7271"]),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_foam_cutting;i=5098",
    browseName="ns=plastics_foam_cutting;<Name>_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7192", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5100"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5101"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5102"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5103"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5104"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5105"]),
    ],
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5082",
    browseName="ns=plastics_foam_cutting;GrindDrives",
    description="Provides information about the grind drives including the grinding unit speed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6665", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5098"]),
    ],
)
http_opcfoundation_org_UA_PlasticsRubber_FlexiblePURFoam_Cutting_ = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_foam_cutting;i=5099",
    browseName="ns=plastics_foam_cutting;http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7415", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7416", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7417", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7418", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7419",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7420", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7421", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_foam_cutting;i=7596", browseName="ns=plastics_foam_cutting;ActiveVacuumUnitsDataType", dataType=o6.String, value="ActiveVacuumUnitsDataType"
)
o6.reference(o6.ns["ns=plastics_foam_cutting;i=5073"], "i=39", o6.ns["ns=plastics_foam_cutting;i=7596"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_foam_cutting;i=6002",
    browseName="ns=plastics_foam_cutting;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6004",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7596"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ua="http://opcfoundation.org/UA/" xmlns:opc="http://opcfoundation.org/BinarySchema/" DefaultByteOrder="LittleEndian" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType Name="ActiveVacuumUnitsDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>Provides information about the position of a vacuum unit and the current vacuum power, given as a float value between 0 (off) and 1 (full power).</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="Position"/>\n  <opc:Field TypeName="opc:Float" Name="VacuumPower"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="BottomFixtureEnumeration">\n  <opc:Documentation>Provides information about the type of material fixture for the material bottom.</opc:Documentation>\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="Mechanical_Fixture" Value="1"/>\n  <opc:EnumeratedValue Name="Vacuum_Fixture" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ConveyorCategoryEnumeration">\n  <opc:Documentation>This property provides information, if this conveyor is used for unloading, loading or transportation of material.</opc:Documentation>\n  <opc:EnumeratedValue Name="Loading" Value="0"/>\n  <opc:EnumeratedValue Name="Unloading" Value="1"/>\n  <opc:EnumeratedValue Name="Transportation" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ConveyorSubCategoryEnumeration">\n  <opc:Documentation>This property provides information on what type of conveyor this instance is.</opc:Documentation>\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="AlignmentBelt" Value="1"/>\n  <opc:EnumeratedValue Name="Turntable" Value="2"/>\n  <opc:EnumeratedValue Name="Seperator" Value="3"/>\n  <opc:EnumeratedValue Name="Stacker" Value="4"/>\n  <opc:EnumeratedValue Name="Destacker" Value="5"/>\n  <opc:EnumeratedValue Name="PopUp" Value="6"/>\n  <opc:EnumeratedValue Name="ScissorTable" Value="7"/>\n  <opc:EnumeratedValue Name="CrossConveyor" Value="8"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DirectionEnumeration">\n  <opc:Documentation>Provides information about the current transportation direction of the conveyor.</opc:Documentation>\n  <opc:EnumeratedValue Name="Forward" Value="0"/>\n  <opc:EnumeratedValue Name="Backward" Value="1"/>\n  <opc:EnumeratedValue Name="Sideward" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GrindingUnitStateEnumeration">\n  <opc:Documentation>Provides information about the current state of the grinding unit.</opc:Documentation>\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Standby" Value="1"/>\n  <opc:EnumeratedValue Name="Running" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="LightBarrierEnumeration">\n  <opc:Documentation>Provides information about the positions of light barriers on this instance of conveyor.</opc:Documentation>\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="Infeed" Value="1"/>\n  <opc:EnumeratedValue Name="Outfeed" Value="2"/>\n  <opc:EnumeratedValue Name="Safety" Value="3"/>\n  <opc:EnumeratedValue Name="Other" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="MaterialSupportCategoryEnumeration">\n  <opc:Documentation>This Property provides information about the category of the material support system.</opc:Documentation>\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="Fixed_Machine_Table" Value="1"/>\n  <opc:EnumeratedValue Name="Sliding_Machine_Table" Value="2"/>\n  <opc:EnumeratedValue Name="Carousel" Value="3"/>\n  <opc:EnumeratedValue Name="Conveyor_Belt" Value="4"/>\n  <opc:EnumeratedValue Name="Turntable_90Degrees" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PossibleDirectionEnumeration">\n  <opc:Documentation>Provides information about the possible working directions of the conveyor.</opc:Documentation>\n  <opc:EnumeratedValue Name="Forwards" Value="0"/>\n  <opc:EnumeratedValue Name="Backwards" Value="1"/>\n  <opc:EnumeratedValue Name="Reversible" Value="2"/>\n  <opc:EnumeratedValue Name="Sidewards" Value="3"/>\n  <opc:EnumeratedValue Name="Any" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ProcessingModeEnumeration">\n  <opc:Documentation>Provides information about the current processing mode as addition to the MachineOperationMode state Processing.</opc:Documentation>\n  <opc:EnumeratedValue Name="Manual" Value="0"/>\n  <opc:EnumeratedValue Name="SemiAutomatic" Value="1"/>\n  <opc:EnumeratedValue Name="Automatic" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SideFixtureEnumeration">\n  <opc:Documentation>Provides information about the type of material fixture for the material side.</opc:Documentation>\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="Right" Value="1"/>\n  <opc:EnumeratedValue Name="Left" Value="2"/>\n  <opc:EnumeratedValue Name="Both" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="TopFixtureEnumeration">\n  <opc:Documentation>Provides information about the type of material fixture for the material top.</opc:Documentation>\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="Pressure_Pad" Value="1"/>\n  <opc:EnumeratedValue Name="Pressure_Roller" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_foam_cutting;i=7597",
    browseName="ns=plastics_foam_cutting;ActiveVacuumUnitsDataType",
    dataType=o6.String,
    value="//xs:element[@name='ActiveVacuumUnitsDataType']",
)
o6.reference(o6.ns["ns=plastics_foam_cutting;i=5074"], "i=39", o6.ns["ns=plastics_foam_cutting;i=7597"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_foam_cutting;i=6005",
    browseName="ns=plastics_foam_cutting;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6006",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/Types.xsd",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6007",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7597"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/FlexiblePURFoam/Cutting/Types.xsd" elementFormDefault="qualified">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="BottomFixtureEnumeration">\n  <xs:annotation>\n   <xs:documentation>Provides information about the type of material fixture for the material bottom.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="Mechanical_Fixture_1"/>\n   <xs:enumeration value="Vacuum_Fixture_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BottomFixtureEnumeration" name="BottomFixtureEnumeration"/>\n <xs:complexType name="ListOfBottomFixtureEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:BottomFixtureEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="BottomFixtureEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBottomFixtureEnumeration" nillable="true" name="ListOfBottomFixtureEnumeration"/>\n <xs:simpleType name="ConveyorCategoryEnumeration">\n  <xs:annotation>\n   <xs:documentation>This property provides information, if this conveyor is used for unloading, loading or transportation of material.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Loading_0"/>\n   <xs:enumeration value="Unloading_1"/>\n   <xs:enumeration value="Transportation_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ConveyorCategoryEnumeration" name="ConveyorCategoryEnumeration"/>\n <xs:complexType name="ListOfConveyorCategoryEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:ConveyorCategoryEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="ConveyorCategoryEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConveyorCategoryEnumeration" nillable="true" name="ListOfConveyorCategoryEnumeration"/>\n <xs:simpleType name="ConveyorSubCategoryEnumeration">\n  <xs:annotation>\n   <xs:documentation>This property provides information on what type of conveyor this instance is.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="AlignmentBelt_1"/>\n   <xs:enumeration value="Turntable_2"/>\n   <xs:enumeration value="Seperator_3"/>\n   <xs:enumeration value="Stacker_4"/>\n   <xs:enumeration value="Destacker_5"/>\n   <xs:enumeration value="PopUp_6"/>\n   <xs:enumeration value="ScissorTable_7"/>\n   <xs:enumeration value="CrossConveyor_8"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ConveyorSubCategoryEnumeration" name="ConveyorSubCategoryEnumeration"/>\n <xs:complexType name="ListOfConveyorSubCategoryEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:ConveyorSubCategoryEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="ConveyorSubCategoryEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConveyorSubCategoryEnumeration" nillable="true" name="ListOfConveyorSubCategoryEnumeration"/>\n <xs:simpleType name="DirectionEnumeration">\n  <xs:annotation>\n   <xs:documentation>Provides information about the current transportation direction of the conveyor.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Forward_0"/>\n   <xs:enumeration value="Backward_1"/>\n   <xs:enumeration value="Sideward_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DirectionEnumeration" name="DirectionEnumeration"/>\n <xs:complexType name="ListOfDirectionEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:DirectionEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="DirectionEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDirectionEnumeration" nillable="true" name="ListOfDirectionEnumeration"/>\n <xs:simpleType name="GrindingUnitStateEnumeration">\n  <xs:annotation>\n   <xs:documentation>Provides information about the current state of the grinding unit.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Standby_1"/>\n   <xs:enumeration value="Running_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GrindingUnitStateEnumeration" name="GrindingUnitStateEnumeration"/>\n <xs:complexType name="ListOfGrindingUnitStateEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:GrindingUnitStateEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="GrindingUnitStateEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGrindingUnitStateEnumeration" nillable="true" name="ListOfGrindingUnitStateEnumeration"/>\n <xs:simpleType name="LightBarrierEnumeration">\n  <xs:annotation>\n   <xs:documentation>Provides information about the positions of light barriers on this instance of conveyor.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="Infeed_1"/>\n   <xs:enumeration value="Outfeed_2"/>\n   <xs:enumeration value="Safety_3"/>\n   <xs:enumeration value="Other_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:LightBarrierEnumeration" name="LightBarrierEnumeration"/>\n <xs:complexType name="ListOfLightBarrierEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:LightBarrierEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="LightBarrierEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLightBarrierEnumeration" nillable="true" name="ListOfLightBarrierEnumeration"/>\n <xs:simpleType name="MaterialSupportCategoryEnumeration">\n  <xs:annotation>\n   <xs:documentation>This Property provides information about the category of the material support system.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="Fixed_Machine_Table_1"/>\n   <xs:enumeration value="Sliding_Machine_Table_2"/>\n   <xs:enumeration value="Carousel_3"/>\n   <xs:enumeration value="Conveyor_Belt_4"/>\n   <xs:enumeration value="Turntable_90Degrees_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MaterialSupportCategoryEnumeration" name="MaterialSupportCategoryEnumeration"/>\n <xs:complexType name="ListOfMaterialSupportCategoryEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:MaterialSupportCategoryEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="MaterialSupportCategoryEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMaterialSupportCategoryEnumeration" nillable="true" name="ListOfMaterialSupportCategoryEnumeration"/>\n <xs:simpleType name="PossibleDirectionEnumeration">\n  <xs:annotation>\n   <xs:documentation>Provides information about the possible working directions of the conveyor.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Forwards_0"/>\n   <xs:enumeration value="Backwards_1"/>\n   <xs:enumeration value="Reversible_2"/>\n   <xs:enumeration value="Sidewards_3"/>\n   <xs:enumeration value="Any_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PossibleDirectionEnumeration" name="PossibleDirectionEnumeration"/>\n <xs:complexType name="ListOfPossibleDirectionEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:PossibleDirectionEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="PossibleDirectionEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPossibleDirectionEnumeration" nillable="true" name="ListOfPossibleDirectionEnumeration"/>\n <xs:simpleType name="ProcessingModeEnumeration">\n  <xs:annotation>\n   <xs:documentation>Provides information about the current processing mode as addition to the MachineOperationMode state Processing.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Manual_0"/>\n   <xs:enumeration value="SemiAutomatic_1"/>\n   <xs:enumeration value="Automatic_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ProcessingModeEnumeration" name="ProcessingModeEnumeration"/>\n <xs:complexType name="ListOfProcessingModeEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:ProcessingModeEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="ProcessingModeEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProcessingModeEnumeration" nillable="true" name="ListOfProcessingModeEnumeration"/>\n <xs:simpleType name="SideFixtureEnumeration">\n  <xs:annotation>\n   <xs:documentation>Provides information about the type of material fixture for the material side.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="Right_1"/>\n   <xs:enumeration value="Left_2"/>\n   <xs:enumeration value="Both_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SideFixtureEnumeration" name="SideFixtureEnumeration"/>\n <xs:complexType name="ListOfSideFixtureEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:SideFixtureEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="SideFixtureEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSideFixtureEnumeration" nillable="true" name="ListOfSideFixtureEnumeration"/>\n <xs:simpleType name="TopFixtureEnumeration">\n  <xs:annotation>\n   <xs:documentation>Provides information about the type of material fixture for the material top.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="Pressure_Pad_1"/>\n   <xs:enumeration value="Pressure_Roller_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:TopFixtureEnumeration" name="TopFixtureEnumeration"/>\n <xs:complexType name="ListOfTopFixtureEnumeration">\n  <xs:sequence>\n   <xs:element type="tns:TopFixtureEnumeration" minOccurs="0" nillable="true" maxOccurs="unbounded" name="TopFixtureEnumeration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTopFixtureEnumeration" nillable="true" name="ListOfTopFixtureEnumeration"/>\n <xs:complexType name="ActiveVacuumUnitsDataType">\n  <xs:annotation>\n   <xs:documentation>Provides information about the position of a vacuum unit and the current vacuum power, given as a float value between 0 (off) and 1 (full power).</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:string" minOccurs="0" maxOccurs="1" name="Position"/>\n   <xs:element type="xs:float" minOccurs="0" maxOccurs="1" name="VacuumPower"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ActiveVacuumUnitsDataType" name="ActiveVacuumUnitsDataType"/>\n <xs:complexType name="ListOfActiveVacuumUnitsDataType">\n  <xs:sequence>\n   <xs:element type="tns:ActiveVacuumUnitsDataType" minOccurs="0" nillable="true" maxOccurs="unbounded" name="ActiveVacuumUnitsDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfActiveVacuumUnitsDataType" nillable="true" name="ListOfActiveVacuumUnitsDataType"/>\n</xs:schema>\n',
)
plastics_foam_cutting_objtypes.ConveyorProcessMonitoringType(
    nodeId="ns=plastics_foam_cutting;i=5026",
    browseName="ns=plastics_foam_cutting;<Conveyor_Nr>",
    description="The instance of “<Conveyor_Nr>” shall match the instance of “<Conveyor_Nr>” in the ConveyorConfigurationType.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7599",
                browseName="ns=plastics_foam_cutting;Description",
                description="Provides a user-defined textual description or identifier to distinguish and locate the conveyor within the machine or system.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5027"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6428", browseName="ns=plastics_foam_cutting;Active", description="Indicates if the conveyor is active.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6429",
                browseName="ns=plastics_foam_cutting;Direction",
                description="Provides information about the current transportation direction of the conveyor.",
                dataType=plastics_foam_cutting_datypes.DirectionEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6431"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5011",
    browseName="ns=plastics_foam_cutting;ConveyorProcessMonitoring",
    description="This folder provides the process values of the conveyors for the transport of material.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5026"])],
)
o6.reference(plastics_foam_cutting_objtypes.ProcessMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5011"])
plastics_foam_cutting_objtypes.ConveyorConfigurationType(
    nodeId="ns=plastics_foam_cutting;i=5044",
    browseName="ns=plastics_foam_cutting;<Conveyor_Nr>",
    description="When instances for device conveyor are created, the BrowseNames shall be “<Conveyor_Nr>” (“Nr” starting with 001).",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6845",
                browseName="ns=plastics_foam_cutting;ConveyorCategory",
                description="This property provides information, if this conveyor is used for unloading, loading or transportation of material.",
                dataType=plastics_foam_cutting_datypes.ConveyorCategoryEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6849",
                browseName="ns=plastics_foam_cutting;ConveyorSubCategory",
                description="This property provides information on what type of conveyor this instance is.",
                dataType=plastics_foam_cutting_datypes.ConveyorSubCategoryEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6850",
                browseName="ns=plastics_foam_cutting;FixedSpeedConveyor",
                description="This Property provides information, if the conveyor has a fixed speed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6851",
                browseName="ns=plastics_foam_cutting;IsPresent",
                description="The IsPresent Property provides information, if an instance of the conveyor is present in the current configuration of the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6854",
                browseName="ns=plastics_foam_cutting;LightBarriers",
                description="Provides information about the positions of light barriers on this instance of conveyor.\nEach array entry represents one light barrier.",
                dataType=plastics_foam_cutting_datypes.LightBarrierEnumeration,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6855",
                browseName="ns=plastics_foam_cutting;NumberOfBelts",
                description="Provides the number of individual belts on the conveyor.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6856",
                browseName="ns=plastics_foam_cutting;PossibleDirection",
                description="Provides information about the possible working directions of the conveyor.",
                dataType=plastics_foam_cutting_datypes.PossibleDirectionEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7602",
                browseName="ns=plastics_foam_cutting;Description",
                description="Provides a user-defined textual description or identifier to distinguish and locate the conveyor within the machine or system.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6846"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6852"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6857"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5040",
    browseName="ns=plastics_foam_cutting;ConveyorConfigurations",
    description="An instance declaration of the 0:FolderType. It provides a folder to organize the child nodes that represent the configurations of the conveyers that are attached, to a foam cutting unit.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5044"])],
)
o6.reference(plastics_foam_cutting_objtypes.MachineConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5040"])
plastics_foam_cutting_objtypes.ConveyorConfigurationType(
    nodeId="ns=plastics_foam_cutting;i=5065",
    browseName="ns=plastics_foam_cutting;<Conveyor_Nr>",
    description="The ConveyorConfigurationType details the configuration of the conveyor that is used to feed material towards or away from the cutting edge of the knife.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6949",
                browseName="ns=plastics_foam_cutting;ConveyorCategory",
                description="This property provides information, if this conveyor is used for unloading, loading or transportation of material.",
                dataType=plastics_foam_cutting_datypes.ConveyorCategoryEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6953",
                browseName="ns=plastics_foam_cutting;ConveyorSubCategory",
                description="This property provides information on what type of conveyor this instance is.",
                dataType=plastics_foam_cutting_datypes.ConveyorSubCategoryEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6954",
                browseName="ns=plastics_foam_cutting;FixedSpeedConveyor",
                description="This Property provides information, if the conveyor has a fixed speed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6955",
                browseName="ns=plastics_foam_cutting;IsPresent",
                description="The IsPresent Property provides information, if an instance of the conveyor is present in the current configuration of the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6958",
                browseName="ns=plastics_foam_cutting;LightBarriers",
                description="Provides information about the positions of light barriers on this instance of conveyor.\nEach array entry represents one light barrier.",
                dataType=plastics_foam_cutting_datypes.LightBarrierEnumeration,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6959",
                browseName="ns=plastics_foam_cutting;NumberOfBelts",
                description="Provides the number of individual belts on the conveyor.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6960",
                browseName="ns=plastics_foam_cutting;PossibleDirection",
                description="Provides information about the possible working directions of the conveyor.",
                dataType=plastics_foam_cutting_datypes.PossibleDirectionEnumeration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7603",
                browseName="ns=plastics_foam_cutting;Description",
                description="Provides a user-defined textual description or identifier to distinguish and locate the conveyor within the machine or system.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6950"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6956"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6961"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5084",
    browseName="ns=plastics_foam_cutting;ConveyorConfigurations",
    description="An instance declaration of the 0:FolderType. It provides a folder to organize the child nodes that represent the configurations of the conveyers that are attached, to a foam cutting unit.",
    references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5065"])],
)
plastics_foam_cutting_objtypes.MachineConfigurationType(
    nodeId="ns=plastics_foam_cutting;i=5047",
    browseName="ns=plastics_foam_cutting;MachineConfiguration",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6898",
                browseName="ns=plastics_foam_cutting;GrindingUnit",
                description="A property with 0:Boolean data type. Its value is 1 if a grinding unit is physically present in a foam cutting machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=6899",
                browseName="ns=plastics_foam_cutting;Knife",
                description="A property with 0:Boolean data type. Its value is 1 if is physically present in a foam cutting machine and is used for its normal operation.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5048"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5084"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.FoamCuttingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5047"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7605",
    browseName="ns=plastics_foam_cutting;KnifeSpeed",
    description="Provides the set value of the knife.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7606", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_foam_cutting_objtypes.KnifeType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=7605"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5075",
    browseName="ns=plastics_foam_cutting;WearStatus",
    description="Provides information about the wear status of the knife.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7608",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7607",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.KnifeType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5075"])
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5076",
    browseName="ns=plastics_foam_cutting;GrindDrives",
    description="Provides information about the grind drives including the grinding unit speed.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7609", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_foam_cutting_objtypes.KnifeType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5076"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7611",
    browseName="ns=plastics_foam_cutting;Readjustment",
    description="Provides information about the mechanical adjustment in the mounting position of the knife to compensate for wear.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7612", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_foam_cutting_objtypes.KnifeType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=7611"])
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5077",
    browseName="ns=plastics_foam_cutting;KnifeDrives",
    description="Provides information about the drives of the knife.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7613", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_foam_cutting_objtypes.KnifeType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5077"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_foam_cutting;i=5096",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7186",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7631", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7632", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7633", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7389",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7390", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7663", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7664", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7665", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7666", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7391",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7392", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7667", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7668", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7669", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7670", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7393",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7394", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7671", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7672", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7673", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7674", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5093",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7389"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7391"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7393"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=7395", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7397",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7398", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7675", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7676", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7677", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7678", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7399",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7400", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7679", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7680", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7681", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7682", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7401",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7402", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7683", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7684", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7685", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7686", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5094",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7182",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7396",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7181",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7397"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7399"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7401"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7184",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7185", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7687", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7688", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7689", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7690", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7403",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7404", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7405", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7691", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7692", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7407",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7408", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7693", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7694", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7695", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7696", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7409",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7410", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7697", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7698", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7699", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7700", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7411",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7412", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7701", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7702", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7703", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7704", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7413",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7414", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7705", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7706", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7707", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7708", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7614",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7615", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7616", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7709", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7710", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7618",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7619", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7711", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7712", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7713", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7714", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7620",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7621", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7715", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7716", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7717", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7718", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7622",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7623", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7719", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7720", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7721", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7722", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7624",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7625", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7626", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7723", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7724", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7627",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7628", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7725", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7726", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7727", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7728", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7629",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7630", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7729", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7730", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7731", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7732", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5095",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7406",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7184"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7403"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7407"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7409"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7411"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7413"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7614"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7617",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7618"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7620"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7622"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7624"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7627"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7629"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7187",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7188", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7733", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7734", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7735", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7736", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7634",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7635", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7636", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7737", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7738", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7638",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7639", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7739", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7740", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7741", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7742", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7640",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7641", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7743", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7744", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7745", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7746", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7642",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7643", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7747", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7748", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7749", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7750", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7644",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7645", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7751", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7752", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7753", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7754", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7646",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7647", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7648", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7755", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7756", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7650",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7651", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7757", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7758", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7759", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7760", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7652",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7653", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7761", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7762", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7763", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7764", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7654",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7655", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7765", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7766", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7767", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7768", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7656",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7657", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7658", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7769", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7770", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7659",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7660", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7771", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7772", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7773", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7774", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7661",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7662", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7775", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7776", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7777", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7778", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5097",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7637",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7187"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7634"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7638"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7640"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7642"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7644"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7646"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7649",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7650"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7652"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7654"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7656"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7659"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7661"]),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_foam_cutting;i=5091",
    browseName="ns=plastics_foam_cutting;<Name>_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7183", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5092"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5093"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5094"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5095"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5096"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5097"]),
    ],
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5083",
    browseName="ns=plastics_foam_cutting;KnifeDrives",
    description="Provides information about the drives of the knife.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6667", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5091"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7780",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7781", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7782",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7783", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7784",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7785", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5085",
    browseName="ns=plastics_foam_cutting;WearStatus",
    description="Provides information about the wear status of the knife.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7179",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7779",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7178",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7780"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7782"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7784"]),
    ],
)
plastics_foam_cutting_objtypes.KnifeType(
    nodeId="ns=plastics_foam_cutting;i=5081",
    browseName="ns=plastics_foam_cutting;<Knife_Nr>",
    description="Contains process values of one knife.",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5082"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5083"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5085"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6664",
                browseName="ns=plastics_foam_cutting;KnifeRunning",
                description="Indicates if the knife is switched on (true) or off (false).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6666",
                browseName="ns=plastics_foam_cutting;GrindingUnitState",
                description="Provides information about the current state of the grinding unit.",
                dataType=plastics_foam_cutting_datypes.GrindingUnitStateEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7174"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7176"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5090",
    browseName="ns=plastics_foam_cutting;Knifes",
    description="This folder contains process values of the knife.",
    references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5081"])],
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_foam_cutting;i=5107",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7786", browseName="NodeVersion", dataType=o6.String, value=""))],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_foam_cutting;i=5111",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7792",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7838", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7839", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_foam_cutting;i=7840", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7795",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7796", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7870", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7871", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7872", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7873", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7797",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7798", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7874", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7875", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7876", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7877", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_foam_cutting;i=7799",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7800", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7878", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7879", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7880", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7881", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_foam_cutting;i=5108",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7795"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7797"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7799"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_foam_cutting;i=7801", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7803",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7804", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7882", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7883", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7884", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7885", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7805",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7806", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7886", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7887", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7888", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7889", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7807",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7808", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7890", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7891", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7892", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7893", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_foam_cutting;i=5109",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7788",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7802",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7787",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7803"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7805"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7807"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7790",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7791", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7894", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7895", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7896", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7897", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7809",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7810", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7811", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7898", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7899", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7813",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7814", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7900", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7901", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7902", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7903", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7815",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7816", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7904", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7905", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7906", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7907", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7817",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7818", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7908", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7909", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7910", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7911", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7819",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7820", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7912", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7913", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7914", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7915", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7821",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7822", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7823", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7916", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7917", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7825",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7826", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7918", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7919", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7920", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7921", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7827",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7828", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7922", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7923", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7924", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7925", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7829",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7830", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7926", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7927", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7928", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7929", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7831",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7832", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7833", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7930", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7931", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7834",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7835", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7932", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7933", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7934", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7935", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7836",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7837", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7936", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7937", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7938", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7939", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5110",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7812",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7790"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7809"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7813"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7815"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7817"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7819"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7821"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7824",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7825"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7827"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7829"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7831"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7834"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7836"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7793",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7794", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7940", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7941", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7942", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7943", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7841",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7842", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7843", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7944", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7945", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7845",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7846", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7946", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7947", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7948", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7949", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7847",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7848", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7950", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7951", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7952", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7953", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7849",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7850", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7954", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7955", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7956", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7957", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7851",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7852", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7958", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7959", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7960", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7961", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7853",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7854", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7855", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7962", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7963", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7857",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7858", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7964", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7965", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7966", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7967", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7859",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7860", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7968", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7969", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7970", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7971", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7861",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7862", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7972", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7973", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7974", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7975", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_foam_cutting;i=7863",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7864", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7865", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7976", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7977", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7866",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7867", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7978", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7979", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7980", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7981", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_foam_cutting;i=7868",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7869", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7982", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7983", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7984", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7985", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_foam_cutting;i=5112",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7844",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7793"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7841"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7845"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7847"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7849"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7851"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7853"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_foam_cutting;i=7856",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7857"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7859"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7861"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7863"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7866"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=7868"]),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_foam_cutting;i=5106",
    browseName="ns=plastics_foam_cutting;<Name>_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=7789", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5107"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5108"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5109"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5110"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5111"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5112"]),
    ],
)
plastics_rubber.objtypes.DrivesType(
    nodeId="ns=plastics_foam_cutting;i=5055",
    browseName="ns=plastics_foam_cutting;Drives",
    description="Drives is a container object for all drives of the conveyor.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_foam_cutting;i=6907", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5106"]),
    ],
)
plastics_foam_cutting_objtypes.ConveyorProcessMonitoringType(
    nodeId="ns=plastics_foam_cutting;i=5054",
    browseName="ns=plastics_foam_cutting;<Conveyor_Nr>",
    description="Provides information about the process values of one conveyor.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_foam_cutting;i=7600",
                browseName="ns=plastics_foam_cutting;Description",
                description="Provides a user-defined textual description or identifier to distinguish and locate the conveyor within the machine or system.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5055"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6905", browseName="ns=plastics_foam_cutting;Active", description="Indicates if the conveyor is active.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_foam_cutting;i=6906",
                browseName="ns=plastics_foam_cutting;Direction",
                description="Provides information about the current transportation direction of the conveyor.",
                dataType=plastics_foam_cutting_datypes.DirectionEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=6908"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_foam_cutting;i=5053",
    browseName="ns=plastics_foam_cutting;ConveyorProcessMonitoring",
    description="This folder provides the process values of the conveyors for the transport of material.",
    references=[o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5054"])],
)
plastics_foam_cutting_objtypes.ProcessMonitoringType(
    nodeId="ns=plastics_foam_cutting;i=5052",
    browseName="ns=plastics_foam_cutting;ProcessMonitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5053"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5056"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5057"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5058"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5059"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5060"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5061"]),
        o6.hasComponent(o6.ns["ns=plastics_foam_cutting;i=5090"]),
    ],
)
o6.reference(plastics_foam_cutting_objtypes.FoamCuttingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_foam_cutting;i=5052"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_rubber, plastics_foam_cutting_datypes, plastics_foam_cutting_objtypes
