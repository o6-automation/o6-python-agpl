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

"""Generated OPC UA machinery_processvalues namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.irdi as irdi
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import vartypes as machinery_processvalues_vartypes
from . import objtypes as machinery_processvalues_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMachinerySlashProcessValuesSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=machinery_processvalues;i=5001",
    browseName="ns=machinery_processvalues;http://opcfoundation.org/UA/Machinery/ProcessValues/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2023-05-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/ProcessValues/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.00.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6005",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=machinery_processvalues;i=6008",
    browseName="ns=machinery_processvalues;PercentageValue",
    description="Provides the process value in percentage.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6009",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6010", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0)
            )
        ),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6008"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6011",
    browseName="ns=machinery_processvalues;LowLowLimit",
    description="Defines the absolute low low limit",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6011"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6013",
    browseName="ns=machinery_processvalues;LowLimit",
    description="Defines the absolute low limit",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6014", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6013"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6015",
    browseName="ns=machinery_processvalues;HighLimit",
    description="Defines the absolute high limit",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6016", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6015"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6017",
    browseName="ns=machinery_processvalues;HighHighLimit",
    description="Defines the absolute high high limit",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6018", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6017"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6019",
    browseName="ns=machinery_processvalues;LowLowDeviation",
    description="Defines the low low limit for deviation, relative to the process value setpoint.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6020", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueSetpointVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6019"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6021",
    browseName="ns=machinery_processvalues;LowDeviation",
    description="Defines the low limit for deviation, relative to the process value setpoint.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6022", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueSetpointVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6021"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6023",
    browseName="ns=machinery_processvalues;HighDeviation",
    description="Defines the high limit for deviation, relative to the process value setpoint.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6024", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueSetpointVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6023"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6025",
    browseName="ns=machinery_processvalues;HighHighDeviation",
    description="Defines the high high limit for deviation, relative to the process value setpoint.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6026", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueSetpointVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6025"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_processvalues;i=6028",
    browseName="ns=machinery_processvalues;DeviationSensitivity",
    description="Indicates the sensitivity of the deviation variables when automatically set.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6029",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("FINE"), description=o6.LocalizedText("tight tolerances")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MIDDLE"), description=o6.LocalizedText("mean tolerances")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ROUGH"), description=o6.LocalizedText("large tolerances")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6030", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_vartypes.ProcessValueSetpointVariableType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6028"])
machinery_processvalues_vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=machinery_processvalues;i=6036",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    description="The desired value, may or may not be controlled by the server.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6037", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6038", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_objtypes.ProcessValueType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6036"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=machinery_processvalues;i=6040",
    browseName="ActiveState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6041", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machinery_processvalues;i=6042",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6043", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ExclusiveLimitStateMachineType(
    nodeId="ns=machinery_processvalues;i=5003", browseName="LimitState", references=[o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6042"])]
)
o6.reference(o6.ns["ns=machinery_processvalues;i=6040"], "i=9004", o6.ns["ns=machinery_processvalues;i=5003"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=machinery_processvalues;i=6044",
    browseName="EnabledState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6045", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
o6.reference(o6.ns["ns=machinery_processvalues;i=6044"], "i=9004", o6.ns["ns=machinery_processvalues;i=6040"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=machinery_processvalues;i=6048",
    browseName="AckedState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6049", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=machinery_processvalues;i=6054",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6055", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=machinery_processvalues;i=6059",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6060", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=machinery_processvalues;i=6061",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6062", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=machinery_processvalues;i=6072",
    browseName="ActiveState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6073", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machinery_processvalues;i=6074",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6075", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ExclusiveLimitStateMachineType(
    nodeId="ns=machinery_processvalues;i=5005", browseName="LimitState", references=[o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6074"])]
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=machinery_processvalues;i=6076",
    browseName="EnabledState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6077", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=machinery_processvalues;i=6080",
    browseName="AckedState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6081", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=machinery_processvalues;i=6086",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6087", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=machinery_processvalues;i=6091",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6092", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=machinery_processvalues;i=6093",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6094", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_processvalues;i=6105",
    browseName="ns=machinery_processvalues;Status",
    description="Indicates if a limit has been reached.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6106",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[11],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NONE"), description=o6.LocalizedText("Not monitoring")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("UNKNOWN"), description=o6.LocalizedText("Status not known")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("BELOW_LOWLOW_LIMIT"), description=o6.LocalizedText("Value is below LowLowLimit")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("BELOW_LOW_LIMIT"), description=o6.LocalizedText("Value is below LowLimit")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("BELOW_LOWLOW_DEVIATION"), description=o6.LocalizedText("Value is below LowLowDeviation")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("BELOW_LOW_DEVIATION"), description=o6.LocalizedText("Value is below LowDeviation")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("WITHIN_TOLERANCE"), description=o6.LocalizedText("Value is in tolerance")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ABOVE_HIGH_DEVIATION"), description=o6.LocalizedText("Value is above HighDeviation")),
                    ns0.datatypes.EnumValueType(
                        value=8, displayName=o6.LocalizedText("ABOVE_HIGHHIGH_DEVIATION"), description=o6.LocalizedText("Value is above HighHighDeviation")
                    ),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("ABOVE_HIGH_LIMIT"), description=o6.LocalizedText("Value is above HighLimit")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("ABOVE_HIGHHIGH_LIMIT"), description=o6.LocalizedText("Value is above HighHighLimit")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6107", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_objtypes.ProcessValueType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6105"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=machinery_processvalues;i=6108",
    browseName="ns=machinery_processvalues;AlarmSuppression",
    description="Indicates if alarms based on the Status shall be suppressed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6109",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OFF"), description=o6.LocalizedText("no alarm suppression")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("HORN"), description=o6.LocalizedText("suppressess only horn")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("COMPLETE"), description=o6.LocalizedText("all alarms are suppressed")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6110", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_objtypes.ProcessValueType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6108"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=machinery_processvalues;i=6104",
    browseName="ns=machinery_processvalues;PercentageValue",
    description="Provides the process value in percentage.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6111",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_processvalues;i=6112", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0)
            )
        ),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6113",
    browseName="ns=machinery_processvalues;LowLowLimit",
    description="Defines the absolute low low limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6114", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6115",
    browseName="ns=machinery_processvalues;LowLimit",
    description="Defines the absolute low limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6116", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6117",
    browseName="ns=machinery_processvalues;HighLimit",
    description="Defines the absolute high limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6118", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machinery_processvalues;i=6119",
    browseName="ns=machinery_processvalues;HighHighLimit",
    description="Defines the absolute high high limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6120", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=machinery_processvalues;i=6033",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6034", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6035", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6104"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6113"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6115"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6117"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6119"]),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_processvalues_objtypes.ProcessValueType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=6033"])


ns0.vartypes.PropertyType(
    nodeId="ns=machinery_processvalues;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_processvalues;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=machinery_processvalues;i=7002", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=machinery_processvalues;i=6050"]))
o6.reference(o6.ns["ns=machinery_processvalues;i=7002"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_processvalues;i=6051",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_processvalues;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=machinery_processvalues;i=7003", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=machinery_processvalues;i=6051"]))
o6.reference(o6.ns["ns=machinery_processvalues;i=7003"], "i=3065", "i=2829")

o6.call(nodeId="ns=machinery_processvalues;i=7004", browseName="Disable")
o6.reference(o6.ns["ns=machinery_processvalues;i=7004"], "i=3065", "i=2803")

o6.call(nodeId="ns=machinery_processvalues;i=7005", browseName="Enable")
o6.reference(o6.ns["ns=machinery_processvalues;i=7005"], "i=3065", "i=2803")

ns0.objtypes.ExclusiveDeviationAlarmType(
    nodeId="ns=machinery_processvalues;i=5002",
    browseName="ns=machinery_processvalues;DeviationAlarm",
    description="Becomes active, when the process values derivates from the ProcessValueSetpoint.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6039", browseName="SetpointNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6046", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6047", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6052", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6053", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6056", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6057", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6058", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6063", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6064", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6065", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6066", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6067", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6068", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6069", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6070", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6071", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=5003"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6040"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6044"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6048"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6054"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6059"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6061"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=7002"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=7003"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=7004"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=7005"]),
    ],
)
o6.reference(machinery_processvalues_objtypes.ProcessValueType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=5002"])


ns0.vartypes.PropertyType(
    nodeId="ns=machinery_processvalues;i=6082",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_processvalues;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=machinery_processvalues;i=7006", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=machinery_processvalues;i=6082"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_processvalues;i=6083",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_processvalues;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=machinery_processvalues;i=7007", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=machinery_processvalues;i=6083"]))

ns0.objtypes.ExclusiveLimitAlarmType(
    nodeId="ns=machinery_processvalues;i=5004",
    browseName="ns=machinery_processvalues;LimitAlarm",
    description="Becomes active, when absolute limits are reached.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6078", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6079", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6084", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6085", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6088", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6089", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6090", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6095", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6096", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6097", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6098", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6099", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6100", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6101", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6102", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_processvalues;i=6103", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=5005"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6072"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6076"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6080"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6086"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6091"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=6093"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=7006"]),
        o6.hasComponent(o6.ns["ns=machinery_processvalues;i=7007"]),
        o6.hasComponent(o6.call(nodeId="ns=machinery_processvalues;i=7008", browseName="Disable")),
        o6.hasComponent(o6.call(nodeId="ns=machinery_processvalues;i=7009", browseName="Enable")),
    ],
)
o6.reference(machinery_processvalues_objtypes.ProcessValueType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_processvalues;i=5004"])


del Any, TYPE_CHECKING, uuid, o6, di, irdi, ns0, padim, machinery_processvalues_vartypes, machinery_processvalues_objtypes
