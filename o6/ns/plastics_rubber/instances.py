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

"""Generated OPC UA plastics_rubber namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as plastics_rubber_datypes
from . import objtypes as plastics_rubber_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

defaultSpaceBinary = ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5001", browseName="Default Binary")
defaultSpaceXML = ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5002", browseName="Default XML")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5003", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5006", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.ProductionDatasetWriteOptionsType, o6.ns["ns=plastics_rubber;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5009", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.ProductionDatasetInformationType, o6.ns["ns=plastics_rubber;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5012", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5013", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.ProductionDatasetReadOptionsType, o6.ns["ns=plastics_rubber;i=5013"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5014", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.ConfigurationParameterType, o6.ns["ns=plastics_rubber;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5015", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5024", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5025", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.PageEntryDataType, o6.ns["ns=plastics_rubber;i=5025"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5026", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5027", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.StandstillReasonType, o6.ns["ns=plastics_rubber;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5034", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.PIDParametersDataType, o6.ns["ns=plastics_rubber;i=5034"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5036", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5038", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.JobListElementType, o6.ns["ns=plastics_rubber;i=5038"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5041", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5042", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.CyclicJobListElementType, o6.ns["ns=plastics_rubber;i=5042"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5043", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.ParameterSettingType, o6.ns["ns=plastics_rubber;i=5043"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5048", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5049", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.ActiveErrorDataType, o6.ns["ns=plastics_rubber;i=5049"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5065", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_rubber;i=5066", browseName="Default XML")
o6.hasEncoding(plastics_rubber_datypes.ClassifiedActiveErrorDataType, o6.ns["ns=plastics_rubber;i=5066"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=plastics_rubber;i=6008", browseName="ns=plastics_rubber;PageEntryDataType", dataType=o6.String, value="PageEntryDataType")
o6.reference(o6.ns["ns=plastics_rubber;i=5024"], "i=39", o6.ns["ns=plastics_rubber;i=6008"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6011",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("NOT_READY_TO_START"),
        o6.LocalizedText("START_BLOCKED_BY_CLIENT"),
        o6.LocalizedText("READY_TO_START"),
        o6.LocalizedText("START_REQUESTED"),
        o6.LocalizedText("STARTED"),
        o6.LocalizedText("STOP_REQUESTED"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6034",
    browseName="ns=plastics_rubber;ActualTemperature",
    description="Current temperature of the PowerUnit",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6035", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6036",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.PowerUnitType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6034"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6017",
    browseName="ns=plastics_rubber;ActualTemperature",
    description="Current temperature of the zone",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6042", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6043", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.TemperatureZoneCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6017"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6071",
    browseName="ns=plastics_rubber;ActualTemperature",
    description="Current temperature of the zone",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6073", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.TemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6071"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6074",
    browseName="ns=plastics_rubber;HighDeviationTemperature1",
    description="Maximum temperature that is in the normal tolerance. A higher actual value may create a warning. Used for quality control. Relative value.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6076", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.TemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6074"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6077",
    browseName="ns=plastics_rubber;HighDeviationTemperature2",
    description="Maximum tolerable temperature. A higher actual value may create an alarm. Relative value.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6078", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6079", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.TemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6077"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6081",
    browseName="ns=plastics_rubber;LowDeviationTemperature1",
    description="Minimum temperature that is in the normal tolerance. A lower actual value may create a warning. Used for quality control. Relative value.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6082", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6083", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.TemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6081"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6084",
    browseName="ns=plastics_rubber;LowDeviationTemperature2",
    description="Minimum tolerable temperature. A lower actual value may create an alarm. Relative value.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6085", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6086", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.TemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6084"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6088",
    browseName="ns=plastics_rubber;NominalTemperature",
    description="Nominal temperature (absolute value)",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6089", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6090", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.TemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6088"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6091",
    browseName="ns=plastics_rubber;StandbyTemperature",
    description="Standby temperature of the zone",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6092", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6093", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.TemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6091"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6110",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Undefined")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MACHINE"), description=o6.LocalizedText("The machine causes the event (e.g. an alarm)")),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("OPERATOR"), description=o6.LocalizedText("The operator of the machine causes the event (e.g. a parameter change)")
        ),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("MES"), description=o6.LocalizedText("The MES causes the event (e.g. a MESMessage)")),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("PERIPHERAL_DEVICE"), description=o6.LocalizedText("A peripheral device causes the event (e.g. an alarm)")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6111",
    browseName="ns=plastics_rubber;ActualTemperature",
    description="Current temperature of the zone",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6112", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6113", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6117",
    browseName="ns=plastics_rubber;NominalTemperature",
    description="Nominal temperature (absolute value)",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6118", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6119", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6120",
    browseName="ns=plastics_rubber;StandbyTemperature",
    description="Standby temperature of the zone",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6121", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6122", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber_objtypes.TemperatureZonesType(
    nodeId="ns=plastics_rubber;i=5019",
    browseName="ns=plastics_rubber;TemperatureZones",
    description="Container for the temperature zones of the mould",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6128", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_rubber_objtypes.MouldType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5019"])
plastics_rubber_objtypes.TemperatureZonesType(
    nodeId="ns=plastics_rubber;i=5021",
    browseName="ns=plastics_rubber;TemperatureZones",
    description="Container for the temperature zones of the mould",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6133", browseName="NodeVersion", dataType=o6.String, value=""))],
)
plastics_rubber_objtypes.MouldType(
    nodeId="ns=plastics_rubber;i=5020",
    browseName="ns=plastics_rubber;Mould_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6129", browseName="ns=plastics_rubber;Index", description="Number of the mould", dataType=o6.UInt32, value=0)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6130",
                browseName="ns=plastics_rubber;MouldStatus",
                description="Current (physical) status of the mould",
                dataType=plastics_rubber_datypes.MouldStatusEnumeration,
                value=plastics_rubber_datypes.MouldStatusEnumeration.OTHER,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6131", browseName="ns=plastics_rubber;Description", description="Description of the installed mould", dataType=o6.String, value=""
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6132", browseName="ns=plastics_rubber;Id", description="Id of the installed mould", dataType=o6.String, value="")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6143",
                browseName="ns=plastics_rubber;IsPresent",
                description="Indication if the mould is physically present and connected",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5021"]),
    ],
)
o6.reference(plastics_rubber_objtypes.MouldsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5020"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6148",
    browseName="ns=plastics_rubber;ActualPressure",
    description="Current pressure of the hydraulic unit",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6149", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6150",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.HydraulicUnitType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6148"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6151",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("This state is used if none of the other states below apply")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("OFF"), description=o6.LocalizedText("Control is switched off")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("AUTOMATIC"), description=o6.LocalizedText("The parameter is controlled automatically")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("TUNING"), description=o6.LocalizedText("Optimisation of the control circuit")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("STANDBY"), description=o6.LocalizedText("Parameter is controlled to stand by value")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("OPEN_LOOP"), description=o6.LocalizedText("Open loop control is used")),
        ns0.datatypes.EnumValueType(
            value=6, displayName=o6.LocalizedText("ONLY_MEASUREMENT"), description=o6.LocalizedText("The sensors deliver the current value but there is no controlling")
        ),
    ],
)
plastics_rubber_objtypes.UserType(
    nodeId="ns=plastics_rubber;i=5016",
    browseName="ns=plastics_rubber;User_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6064",
                browseName="ns=plastics_rubber;CardUid",
                description="Uid of the identification card used by the operator for logging in to the machine",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6065", browseName="ns=plastics_rubber;Id", description="Id of the user", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6066",
                browseName="ns=plastics_rubber;Language",
                description="Currently selected language on the machine control unit",
                dataType=ns0.datatypes.LocaleId,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6067", browseName="ns=plastics_rubber;Name", description="Name of the user", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6068", browseName="ns=plastics_rubber;UserLevel", description="Level of the user", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6069", browseName="ns=plastics_rubber;UserRole", description="Role of the user", dataType=o6.String, value="")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6157",
                browseName="ns=plastics_rubber;IsPresent",
                description="The machine can have instances for the maximum number of users that can be simultaneously logged in. TRUE if the instance of UserType represents a user that is currently logged in.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.UsersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5016"])
plastics_rubber_objtypes.UserType(
    nodeId="ns=plastics_rubber;i=5023",
    browseName="ns=plastics_rubber;User",
    description="Indicates the user who is responsible for the change that leads to the event. The fields of UserType shall be null if no user is directly responsible (e.g. for messages coming from the machine control system).",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6158",
                browseName="ns=plastics_rubber;CardUid",
                description="Uid of the identification card used by the operator for logging in to the machine",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6159", browseName="ns=plastics_rubber;Id", description="Id of the user", dataType=o6.String, value="")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6160",
                browseName="ns=plastics_rubber;IsPresent",
                description="The machine can have instances for the maximum number of users that can be simultaneously logged in. TRUE if the instance of UserType represents a user that is currently logged in.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6161",
                browseName="ns=plastics_rubber;Language",
                description="Currently selected language on the machine control unit",
                dataType=ns0.datatypes.LocaleId,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6162", browseName="ns=plastics_rubber;Name", description="Name of the user", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6163", browseName="ns=plastics_rubber;UserLevel", description="Level of the user", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6164", browseName="ns=plastics_rubber;UserRole", description="Role of the user", dataType=o6.String, value="")
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.LogbookEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5023"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6174",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("This state is used if none of the other states below apply")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("NO_PRODUCTION"), description=o6.LocalizedText("The machine does not produce any parts/products")),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("START_UP"),
            description=o6.LocalizedText("The machine is producing parts/products in the start-up phase. So the correct settings of the machines are not reached."),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("READY_FOR_PRODUCTION"),
            description=o6.LocalizedText(
                "The machine is producing parts/products, the correct settings of the machines are reached but the production is not yet released (e.g. waiting for release from quality assurance)"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("PRODUCTION"),
            description=o6.LocalizedText(
                "The machine is producing parts/products.\nIn semi-automatic mode also during waiting time (e.g. for manual loading/unloading of parts) ProductionStatus remains in this state (time out possible if e.g. cycle time exceeds a pre-defined limit)"
            ),
        ),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("DRY_RUN"), description=o6.LocalizedText("The machine is moving without material")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6179",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("UPDATE"), description=o6.LocalizedText("The sequence has been updated (e.g. when a new production dataset has been activated)")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ADD"), description=o6.LocalizedText("An element has been added to the sequence")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("MODIFY"), description=o6.LocalizedText("An element of the sequence has been modified")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("MOVE"), description=o6.LocalizedText("An element of the sequence has been moved")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("DELETE"), description=o6.LocalizedText("An element of the sequence has been deleted")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6181",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("This state is used if none of the other states apply")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AUTOMATIC"), description=o6.LocalizedText("The machine is in automatic mode")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SEMI_AUTOMATIC"), description=o6.LocalizedText("The machine is in semi-automatic mode")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("MANUAL"), description=o6.LocalizedText("The machine is in manual mode")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("SETUP"), description=o6.LocalizedText("The machine is in setup mode")),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("SLEEP"),
            description=o6.LocalizedText(
                "The machine is in sleep mode. Machine is still switched on, energy consumption reduced by e.g. reducing heating, switching drives off. Production is not possible."
            ),
        ),
    ],
)
plastics_rubber_objtypes.UsersType(
    nodeId="ns=plastics_rubber;i=5028",
    browseName="ns=plastics_rubber;Users",
    description="Container for the user(s) of the machine",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6204", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_rubber_objtypes.MachineStatusType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5028"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6213",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("This state is used if none of the other states below apply")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MOULD_NOT_INSTALLED"), description=o6.LocalizedText("The mould is not installed on the machine")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("MOULD_CHANGE"), description=o6.LocalizedText("During installation or changing of the mould")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("MOULD_INSTALLED"), description=o6.LocalizedText("The mould is installed and ready for production")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6214",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("GOOD_CYCLE"),
            description=o6.LocalizedText("The machine has detected no failures during the cycle and the part quality (for all cavities) is assumed as good"),
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("BAD_CYCLE"), description=o6.LocalizedText("The quality of the part(s) is assumed as bad")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("TEST_SAMPLE_CYCLE"), description=o6.LocalizedText("A cycle is separated as a test sample")),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("FAILED_CYCLE"),
            description=o6.LocalizedText(
                "The machine has detected failures during the cycle and the part quality is assumed as bad. Further information is provided by the MessageCondition fired in this case."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6215",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("LOG_ON"), description=o6.LocalizedText("The user has logged on the machine")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("LOG_OFF"), description=o6.LocalizedText("The user has logged off the machine")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6216",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NO_PART"), description=o6.LocalizedText("There is no part in cavity")),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("GOOD_PART"),
            description=o6.LocalizedText("The machine has detected no failures during the cycle for this cavity and the part quality is assumed as good"),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("BAD_PART"),
            description=o6.LocalizedText("The machine has detected failures during the cycle for the cavity and the part quality is assumed as bad"),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("REWORK"),
            description=o6.LocalizedText("The machine has detected failures during the cycle for the cavity which might be fixed by reworking the part"),
        ),
    ],
)
plastics_rubber_objtypes.MESMessageType(
    nodeId="ns=plastics_rubber;i=5029",
    browseName="ns=plastics_rubber;MESMessage",
    description="Text message sent from the MES to be shown on the machine",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6224", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6225", browseName="ns=plastics_rubber;Message", description="Text of the message", dataType=o6.String, value="")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6226", browseName="Severity", description="Severity of the message", dataType=o6.UInt16, value=0)),
    ],
)
o6.reference(plastics_rubber_objtypes.MachineMESStatusType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5029"])
plastics_rubber_objtypes.StandstillMessageType(
    nodeId="ns=plastics_rubber;i=5031",
    browseName="ns=plastics_rubber;StandstillMessage",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6233", browseName="ns=plastics_rubber;Classification", description="Classification of the message", dataType=ns0.datatypes.Enumeration
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6234", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6235", browseName="Severity", description="Severity of the message", dataType=o6.UInt16, value=0)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6236", browseName="Message", description="Text of the message", dataType=o6.LocalizedText, value=o6.LocalizedText()
            )
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.MachineMESStatusType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5031"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6264",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("This state is used if none of the other states below apply")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("TRANSFERRED_ASSIGNED"), description=o6.LocalizedText("The job has been transferred to the machine and assigned as current job")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SET_UP_ACTIVE"), description=o6.LocalizedText("The operator prepares the machine for the job")),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("SET_UP_INTERRUPTED"),
            description=o6.LocalizedText("The operator has interrupted but not finished the preparation of the machine for the job"),
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("SET_UP_FINISHED"), description=o6.LocalizedText("The operator has finished the preparation of the machine for the job")
        ),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("START_UP_ACTIVE"), description=o6.LocalizedText("The operator is setting the machine in the start-up phase")
        ),
        ns0.datatypes.EnumValueType(
            value=6, displayName=o6.LocalizedText("JOB_IN_PRODUCTION"), description=o6.LocalizedText("The machine is producing parts/products for the job")
        ),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("JOB_INTERRUPTED"), description=o6.LocalizedText("The job is interrupted. The nominal output is not reached")
        ),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("JOB_FINISHED"), description=o6.LocalizedText("Nominal output reached")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("TEAR_DOWN_ACTIVE"), description=o6.LocalizedText("The operator tears the machine down")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("TEAR_DOWN_INTERRUPTED"), description=o6.LocalizedText("Tear-down is interrupted but not finished")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("TEAR_DOWN_FINISHED"), description=o6.LocalizedText("Tear-down is finished")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6281",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("PRODUCTION"),
            description=o6.LocalizedText("The production dataset is written directly to the (active layer of the) control system of the machine"),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("PREPARATION"),
            description=o6.LocalizedText("The production dataset is written to the preparation layer of the control system of the machine (if supported)"),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("FILE_SYSTEM"),
            description=o6.LocalizedText("The production dataset is written to the file system of the machine for later activation"),
        ),
    ],
)
plastics_rubber_objtypes.JobInformationType(
    nodeId="ns=plastics_rubber;i=5010",
    browseName="ns=plastics_rubber;JobInPreparation",
    description="Job in a preparation layer of the machine",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6006",
                browseName="ns=plastics_rubber;ContinueAtJobEnd",
                description="Indication if the machine continues the production even if the nominal output has been reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6007", browseName="ns=plastics_rubber;JobDescription", description="Description of the job", dataType=o6.String, value=""
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6106", browseName="ns=plastics_rubber;JobName", description="Name of the job", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6107",
                browseName="ns=plastics_rubber;Material",
                description="Array of material names used for the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=[""],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6108",
                browseName="ns=plastics_rubber;ProductDescription",
                description="Array of descriptions of the products produced by the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=[""],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6109",
                browseName="ns=plastics_rubber;ProductionDatasetDescription",
                description="Additional description of the production dataset which is needed for the job",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6114",
                browseName="ns=plastics_rubber;ProductionDatasetName",
                description="Name of the production dataset which is needed for the job",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6115",
                browseName="ns=plastics_rubber;ProductName",
                description="Array of product names produced by the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=[""],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6287",
                browseName="ns=plastics_rubber;CustomerName",
                description="Name of the customer for that the job is produced",
                dataType=o6.String,
                value="",
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(plastics_rubber_objtypes.JobsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5010"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6292", browseName="ns=plastics_rubber;PageEntryDataType", dataType=o6.String, value="//xs:element[@name='PageEntryDataType']"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5025"], "i=39", o6.ns["ns=plastics_rubber;i=6292"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6293",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[11],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("PARAMETER_CHANGE"), description=o6.LocalizedText("Support of ParameterChangeLogType")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("USER"), description=o6.LocalizedText("Support of UserLogType ")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("REMOTE_ACCESS"), description=o6.LocalizedText("Support of RemoteAccessLogType")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("SEQUENCE_CHANGE"), description=o6.LocalizedText("Support of SequenceChangeLogType")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("MACHINE_MODE_CHANGE"), description=o6.LocalizedText("Support of MachineModeChangeLogType")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("PRODUCTION_STATUS_CHANGE"), description=o6.LocalizedText("Support of ProductionStatusChangeLogType")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("PRODUCTION_DATASET_CHANGE"), description=o6.LocalizedText("Support of ProductionDatasetChangeLogType")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("PRODUCTION_DATASET_FROZEN"), description=o6.LocalizedText("Support of ProductionDatasetFrozenLogType")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("STANDSTILL_REASON"), description=o6.LocalizedText("Support of StandstillReasonLogType")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("MESSAGE"), description=o6.LocalizedText("Support of MessageLogType")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("USER_FEEDBACK"), description=o6.LocalizedText("Support of UserFeedbackLogType")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6297", browseName="ns=plastics_rubber;ConfigurationParameterType", dataType=o6.String, value="ConfigurationParameterType"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5003"], "i=39", o6.ns["ns=plastics_rubber;i=6297"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6301", browseName="ns=plastics_rubber;ConfigurationParameterType", dataType=o6.String, value="//xs:element[@name='ConfigurationParameterType']"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5014"], "i=39", o6.ns["ns=plastics_rubber;i=6301"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=plastics_rubber;i=6302", browseName="ns=plastics_rubber;ParameterSettingType", dataType=o6.String, value="ParameterSettingType")
o6.reference(o6.ns["ns=plastics_rubber;i=5015"], "i=39", o6.ns["ns=plastics_rubber;i=6302"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6303", browseName="ns=plastics_rubber;ParameterSettingType", dataType=o6.String, value="//xs:element[@name='ParameterSettingType']"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5043"], "i=39", o6.ns["ns=plastics_rubber;i=6303"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6294",
    browseName="ns=plastics_rubber;Density",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6308", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber_objtypes.MaterialType(
    nodeId="ns=plastics_rubber;i=5039",
    browseName="ns=plastics_rubber;Material_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6304", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6305", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6294"]),
    ],
)
o6.reference(plastics_rubber_objtypes.MaterialListType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5039"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6096",
    browseName="ns=plastics_rubber;Density",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6316", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.MaterialType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6096"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6312",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6313", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.MaintenanceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6312"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6314",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6315", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6331", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.MaintenanceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6314"])
plastics_rubber_objtypes.JobInformationType(
    nodeId="ns=plastics_rubber;i=5033",
    browseName="ns=plastics_rubber;ActiveJob",
    description="Job that is currently active on the machine",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6288",
                browseName="ns=plastics_rubber;CustomerName",
                description="Name of the customer for that the job is produced",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6298",
                browseName="ns=plastics_rubber;ContinueAtJobEnd",
                description="Indication if the machine continues the production even if the nominal output has been reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6299",
                browseName="ns=plastics_rubber;ProductionDatasetDescription",
                description="Additional description of the production dataset which is needed for the job",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6300",
                browseName="ns=plastics_rubber;ProductionDatasetName",
                description="Name of the production dataset which is needed for the job",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6326", browseName="ns=plastics_rubber;JobDescription", description="Description of the job", dataType=o6.String, value=""
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6327", browseName="ns=plastics_rubber;JobName", description="Name of the job", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6328",
                browseName="ns=plastics_rubber;Material",
                description="Array of material names used for the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=[""],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6332",
                browseName="ns=plastics_rubber;ProductDescription",
                description="Array of descriptions of the products produced by the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=[""],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6333",
                browseName="ns=plastics_rubber;ProductName",
                description="Array of product names produced by the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=[""],
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(plastics_rubber_objtypes.JobsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5033"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6322",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6324", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6334", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6322"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6335",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6336", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6337", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6335"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6344",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6345", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6351", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6344"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6354",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6355", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6356", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6354"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6348",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6349", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6357", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6348"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6340",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6341", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6358", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6340"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6338",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6339", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6359", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6338"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6352",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6353", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6360", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6352"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6325",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6329", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6361", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6325"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6346",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6347", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6362", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6346"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6342",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6343", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6363", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6342"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6321",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6323", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6364", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6321"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6365",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6366", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6369", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.ControlledParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6365"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6367",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6368", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6370", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_rubber_objtypes.ControlledParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6367"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6383",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6385", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6386", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=plastics_rubber;i=6391", browseName="ns=plastics_rubber;StandstillReasonType", dataType=o6.String, value="StandstillReasonType")
o6.reference(o6.ns["ns=plastics_rubber;i=5026"], "i=39", o6.ns["ns=plastics_rubber;i=6391"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6392", browseName="ns=plastics_rubber;StandstillReasonType", dataType=o6.String, value="//xs:element[@name='StandstillReasonType']"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5027"], "i=39", o6.ns["ns=plastics_rubber;i=6392"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6381",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6395", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber_objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_rubber;i=5052",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6397", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_rubber_objtypes.DriveType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5052"])
o6.reference(o6.ns["ns=plastics_rubber;i=5052"], "i=41", "i=2133")
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6398",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("This value is used if none of the other values below apply")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("HEATING"), description=o6.LocalizedText("The zone is a heating zone")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("COOLING"), description=o6.LocalizedText("The zone is a cooling zone")),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("TEMPERATURE_CONTROL"), description=o6.LocalizedText("The zone is controlled by a temperature control device")
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("HOT_RUNNER"), description=o6.LocalizedText("The zone is a hot runner zone")),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("MEASURING"), description=o6.LocalizedText("The zone has no heating or cooling, Only the temperature is measured.")
        ),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6396",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6400", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=plastics_rubber;i=6401", browseName="ns=plastics_rubber;JobListElementType", dataType=o6.String, value="JobListElementType")
o6.reference(o6.ns["ns=plastics_rubber;i=5036"], "i=39", o6.ns["ns=plastics_rubber;i=6401"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6402", browseName="ns=plastics_rubber;JobListElementType", dataType=o6.String, value="//xs:element[@name='JobListElementType']"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5038"], "i=39", o6.ns["ns=plastics_rubber;i=6402"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6403",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6404", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6405", browseName="ns=plastics_rubber;CyclicJobListElementType", dataType=o6.String, value="CyclicJobListElementType"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5041"], "i=39", o6.ns["ns=plastics_rubber;i=6405"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6406", browseName="ns=plastics_rubber;CyclicJobListElementType", dataType=o6.String, value="//xs:element[@name='CyclicJobListElementType']"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5042"], "i=39", o6.ns["ns=plastics_rubber;i=6406"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6407", browseName="ns=plastics_rubber;ProductionDatasetInformationType", dataType=o6.String, value="ProductionDatasetInformationType"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5004"], "i=39", o6.ns["ns=plastics_rubber;i=6407"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6408",
    browseName="ns=plastics_rubber;ProductionDatasetInformationType",
    dataType=o6.String,
    value="//xs:element[@name='ProductionDatasetInformationType']",
)
o6.reference(o6.ns["ns=plastics_rubber;i=5009"], "i=39", o6.ns["ns=plastics_rubber;i=6408"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6409", browseName="ns=plastics_rubber;ProductionDatasetReadOptionsType", dataType=o6.String, value="ProductionDatasetReadOptionsType"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5012"], "i=39", o6.ns["ns=plastics_rubber;i=6409"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6410",
    browseName="ns=plastics_rubber;ProductionDatasetReadOptionsType",
    dataType=o6.String,
    value="//xs:element[@name='ProductionDatasetReadOptionsType']",
)
o6.reference(o6.ns["ns=plastics_rubber;i=5013"], "i=39", o6.ns["ns=plastics_rubber;i=6410"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6411", browseName="ns=plastics_rubber;ProductionDatasetWriteOptionsType", dataType=o6.String, value="ProductionDatasetWriteOptionsType"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5005"], "i=39", o6.ns["ns=plastics_rubber;i=6411"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6412",
    browseName="ns=plastics_rubber;ProductionDatasetWriteOptionsType",
    dataType=o6.String,
    value="//xs:element[@name='ProductionDatasetWriteOptionsType']",
)
o6.reference(o6.ns["ns=plastics_rubber;i=5006"], "i=39", o6.ns["ns=plastics_rubber;i=6412"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=plastics_rubber;i=6413", browseName="ns=plastics_rubber;PIDParametersDataType", dataType=o6.String, value="PIDParametersDataType")
o6.reference(o6.ns["ns=plastics_rubber;i=5017"], "i=39", o6.ns["ns=plastics_rubber;i=6413"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6414", browseName="ns=plastics_rubber;PIDParametersDataType", dataType=o6.String, value="//xs:element[@name='PIDParametersDataType']"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5034"], "i=39", o6.ns["ns=plastics_rubber;i=6414"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6415",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6416", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber_objtypes.EnergyType(
    nodeId="ns=plastics_rubber;i=5051",
    browseName="ns=plastics_rubber;Energy",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6381"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6403"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6415"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_rubber;i=6429", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_rubber_objtypes.DriveType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5051"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6417",
    browseName="ns=plastics_rubber;ActualPower",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6431", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.EnergyType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6417"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6421",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6432", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.EnergyType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6421"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6419",
    browseName="ns=plastics_rubber;PowerConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6433", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_rubber_objtypes.EnergyType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6419"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6434",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6435", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6440", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6436",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6437", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6443", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6438",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6439", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6444", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6388",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6390", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6445", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6446",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6447", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6448", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6458",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6459", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6466", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6450",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6451", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6477", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6452",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6453", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6478", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6454",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6455", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6479", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6456",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6457", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6480", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6467",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6468", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6481", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6469",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6470", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6482", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6471",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6472", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6483", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6473",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6474", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6484", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6475",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6476", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6485", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6393",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6394", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6486", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6487",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6488", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6489", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6496",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6497", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6498", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6506",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6507", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6510", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6508",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6509", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6511", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6516",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6517", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6518", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_rubber_objtypes.MaintenanceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6516"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=plastics_rubber;i=6519", browseName="ns=plastics_rubber;ActiveErrorDataType", dataType=o6.String, value="ActiveErrorDataType")
o6.reference(o6.ns["ns=plastics_rubber;i=5048"], "i=39", o6.ns["ns=plastics_rubber;i=6519"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6520", browseName="ns=plastics_rubber;ActiveErrorDataType", dataType=o6.String, value="//xs:element[@name='ActiveErrorDataType']"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5049"], "i=39", o6.ns["ns=plastics_rubber;i=6520"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6521",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NOT_DUE"), description=o6.LocalizedText("Maintenance of the device/component is not due")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("WARNING"), description=o6.LocalizedText("Maintenance of the device/component is due in the near future")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("DUE"), description=o6.LocalizedText("Maintenance of the device/component is due")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6524",
    browseName="ns=plastics_rubber;HighDeviationTemperature1",
    description="Maximum temperature that is in the normal tolerance. A higher actual value may create a warning. Used for quality control. Relative value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6525", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6526", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6527",
    browseName="ns=plastics_rubber;HighDeviationTemperature2",
    description="Maximum tolerable temperature. A higher actual value may create an alarm. Relative value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6528", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6529", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6530",
    browseName="ns=plastics_rubber;LowDeviationTemperature1",
    description="Minimum temperature that is in the normal tolerance. A lower actual value may create a warning. Used for quality control. Relative value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6531", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6532", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6533",
    browseName="ns=plastics_rubber;LowDeviationTemperature2",
    description="Minimum tolerable temperature. A lower actual value may create an alarm. Relative value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6534", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6535", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber_objtypes.TemperatureZoneType(
    nodeId="ns=plastics_rubber;i=5018",
    browseName="ns=plastics_rubber;<TemperatureZone_Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6116", browseName="ns=plastics_rubber;Name", description="Name of the zone", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6153", browseName="ns=plastics_rubber;Index", description="Number of the zone", dataType=o6.UInt32, value=0)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6154",
                browseName="ns=plastics_rubber;IsPresent",
                description="Indication if the temperature zone is physically present and connected",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6155",
                browseName="ns=plastics_rubber;ControlMode",
                description="Indication how the temperature is currently controlled",
                dataType=plastics_rubber_datypes.ControlModeEnumeration,
                value=plastics_rubber_datypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6523",
                browseName="ns=plastics_rubber;Classification",
                description="Type of the temperature zone",
                dataType=plastics_rubber_datypes.TemperatureZoneClassificationEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6111"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6117"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6120"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6524"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6527"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6530"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6533"]),
    ],
)
o6.reference(plastics_rubber_objtypes.TemperatureZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5018"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6541",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6542", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6543", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6491",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6492", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6554", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6493",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6494", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6555", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6537",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6538", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6556", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6539",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6540", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6557", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6544",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6545", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6558", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6546",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6547", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6559", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6548",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6549", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6560", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6550",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6551", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6561", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6552",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6553", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6562", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber_objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_rubber;i=5055",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6564", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(o6.ns["ns=plastics_rubber;i=5055"], "i=41", "i=2133")
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashGeneralTypesSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_rubber;i=5061",
    browseName="ns=plastics_rubber;http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6418", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6420", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-05-10T12:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6422", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6441", browseName="NamespaceVersion", dataType=o6.String, value="1.03")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6442",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6565", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6566", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6053",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6573", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6574", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6581",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6582", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6583", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6584",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6585", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6586", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6587",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6588", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6589", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6590",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6591", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6592", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6594",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6595", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6596", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6597",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6598", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6599", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6600",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6601", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6602", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6603",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6604", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6605", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6606",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6607", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6608", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6609",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6610", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6611", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6612",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6613", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6614", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6615",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6616", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6617", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6618",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6619", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6620", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6621",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6622", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6623", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6624",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6625", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6626", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6628",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6629", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6630", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6631",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6632", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6633", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6634",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6635", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6636", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6637",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6638", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6639", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6640",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6641", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6642", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6643",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6644", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6645", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6646",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6647", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6648", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6649",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6650", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6651", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6652",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6653", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6654", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6655",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6656", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6657", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6568",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6569", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6659", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6571",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6572", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6660", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6666",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6667", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6668", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6680",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6681", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_rubber;i=6682",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6683", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber_objtypes.EnergyType(
    nodeId="ns=plastics_rubber;i=5056",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6396"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_rubber;i=6579", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6680"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6682"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6576",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6577", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6689", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6578",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6658", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6690", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6692",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6693", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6694", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6695",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6696", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6697", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6698",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6700", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6662",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6663", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6701", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6664",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6665", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6702", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6669",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6670", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6703", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6671",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6672", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6704", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6673",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6674", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6705", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6676",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6677", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6706", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6678",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6679", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6707", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_rubber;i=6708",
    browseName="ns=plastics_rubber;ActualTemperature",
    description="Current temperature of the PowerUnit",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6709",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6710", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber_objtypes.PowerUnitType(
    nodeId="ns=plastics_rubber;i=5022",
    browseName="ns=plastics_rubber;PowerUnit_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6144", browseName="ns=plastics_rubber;Index", description="Number of the power unit", dataType=o6.UInt32, value=0
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6145",
                browseName="ns=plastics_rubber;IsPresent",
                description="Indication if the power unit is physically present and connected",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6146", browseName="ns=plastics_rubber;PowerOn", description="Indication if the PowerUnit is switched on", dataType=o6.Boolean
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6147", browseName="ns=plastics_rubber;Id", description="Id of the PowerUnit", dataType=o6.String, value="")
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6708"]),
    ],
)
o6.reference(plastics_rubber_objtypes.PowerUnitsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5022"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6712",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=3027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OFF"), description=o6.LocalizedText("Diagnostics inactive ")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ACTIVE_OK"), description=o6.LocalizedText("Diagnostics active ")),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("ACTIVE_ERROR_DETECTED"), description=o6.LocalizedText("Diagnostics active, at least one error detected")
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("COMPLETE"), description=o6.LocalizedText("Diagnostics completed successfully, result in variable &#8220;Result&#8221; available")
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("COMPLETE_ERROR_DETECTED"), description=o6.LocalizedText("Diagnostics completed detected some error")),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6711",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6714", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6715", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6711"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6716", browseName="ns=plastics_rubber;ClassifiedActiveErrorDataType", dataType=o6.String, value="ClassifiedActiveErrorDataType"
)
o6.reference(o6.ns["ns=plastics_rubber;i=5065"], "i=39", o6.ns["ns=plastics_rubber;i=6716"])
oPC40083 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_rubber;i=6002",
    browseName="ns=plastics_rubber;OPC40083",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6003",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6008"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6297"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6302"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6391"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6401"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6405"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6407"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6409"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6411"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6413"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6519"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6716"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ActiveErrorDataType">\n  <opc:Documentation>Iinformation about an active error in a device</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field TypeName="opc:UInt16" Name="Severity"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="Message"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ActiveErrorDataType" Name="ClassifiedActiveErrorDataType">\n  <opc:Documentation>Iinformation about an active error in a device including the SoureNodes and a Classification</opc:Documentation>\n  <opc:Field SourceType="tns:ActiveErrorDataType" TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SourceType="tns:ActiveErrorDataType" TypeName="opc:UInt16" Name="Severity"/>\n  <opc:Field SourceType="tns:ActiveErrorDataType" TypeName="ua:LocalizedText" Name="Message"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSourceNodes"/>\n  <opc:Field LengthField="NoOfSourceNodes" TypeName="ua:NodeId" Name="SourceNodes"/>\n  <opc:Field TypeName="opc:UInt16" Name="Classification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConfigurationParameterType">\n  <opc:Field TypeName="opc:UInt32" Name="Id"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field TypeName="ua:Variant" Name="DefaultValue"/>\n  <opc:Field TypeName="ua:EUInformation" Name="Unit"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="JobListElementType">\n  <opc:Documentation>Description of a job in a job list</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="JobName"/>\n  <opc:Field TypeName="opc:CharArray" Name="JobDescription"/>\n  <opc:Field TypeName="opc:CharArray" Name="JobClassification"/>\n  <opc:Field TypeName="opc:CharArray" Name="CustomerName"/>\n  <opc:Field TypeName="opc:CharArray" Name="ProductionDatasetName"/>\n  <opc:Field TypeName="opc:CharArray" Name="ProductionDatasetDescription"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfMaterial"/>\n  <opc:Field LengthField="NoOfMaterial" TypeName="opc:CharArray" Name="Material"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfProductName"/>\n  <opc:Field LengthField="NoOfProductName" TypeName="opc:CharArray" Name="ProductName"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfProductDescription"/>\n  <opc:Field LengthField="NoOfProductDescription" TypeName="opc:CharArray" Name="ProductDescription"/>\n  <opc:Field TypeName="opc:CharArray" Name="JobPriority"/>\n  <opc:Field TypeName="opc:DateTime" Name="PlannedStart"/>\n  <opc:Field TypeName="opc:Double" Name="PlannedProductionTime"/>\n  <opc:Field TypeName="opc:DateTime" Name="LatestEnd"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:JobListElementType" Name="CyclicJobListElementType">\n  <opc:Documentation>Description of a job in a cyclic job list</opc:Documentation>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="JobName"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="JobDescription"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="JobClassification"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="CustomerName"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="ProductionDatasetName"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="ProductionDatasetDescription"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:Int32" Name="NoOfMaterial"/>\n  <opc:Field LengthField="NoOfMaterial" SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="Material"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:Int32" Name="NoOfProductName"/>\n  <opc:Field LengthField="NoOfProductName" SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="ProductName"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:Int32" Name="NoOfProductDescription"/>\n  <opc:Field LengthField="NoOfProductDescription" SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="ProductDescription"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:CharArray" Name="JobPriority"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:DateTime" Name="PlannedStart"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:Double" Name="PlannedProductionTime"/>\n  <opc:Field SourceType="tns:JobListElementType" TypeName="opc:DateTime" Name="LatestEnd"/>\n  <opc:Field TypeName="opc:UInt64" Name="NominalParts"/>\n  <opc:Field TypeName="opc:UInt64" Name="NominalBoxParts"/>\n  <opc:Field TypeName="opc:Double" Name="ExpectedCycleTime"/>\n  <opc:Field TypeName="opc:CharArray" Name="MouldId"/>\n  <opc:Field TypeName="opc:UInt32" Name="NumCavities"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PageEntryDataType">\n  <opc:Documentation>Information on a page that is implemented in the machine control system and shown on the screen of the machine</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="Title"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ParameterSettingType">\n  <opc:Field TypeName="opc:UInt32" Name="Id"/>\n  <opc:Field TypeName="ua:Variant" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PIDParametersDataType">\n  <opc:Documentation>Structure for storing the parameters of a PID controller</opc:Documentation>\n  <opc:Field TypeName="opc:Double" Name="P"/>\n  <opc:Field TypeName="opc:Double" Name="I"/>\n  <opc:Field TypeName="opc:Double" Name="D"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProductionDatasetInformationType">\n  <opc:Documentation>Information on a production dataset</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field TypeName="opc:CharArray" Name="MESId"/>\n  <opc:Field TypeName="opc:DateTime" Name="CreationTimestamp"/>\n  <opc:Field TypeName="opc:DateTime" Name="LastModificationTimestamp"/>\n  <opc:Field TypeName="opc:DateTime" Name="LastSaveTimestamp"/>\n  <opc:Field TypeName="opc:CharArray" Name="UserName"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfComponents"/>\n  <opc:Field LengthField="NoOfComponents" TypeName="opc:UInt16" Name="Components"/>\n  <opc:Field TypeName="opc:CharArray" Name="Manufacturer"/>\n  <opc:Field TypeName="opc:CharArray" Name="SerialNumber"/>\n  <opc:Field TypeName="opc:CharArray" Name="Model"/>\n  <opc:Field TypeName="opc:CharArray" Name="ControllerName"/>\n  <opc:Field TypeName="opc:CharArray" Name="UserMachineName"/>\n  <opc:Field TypeName="opc:CharArray" Name="LocationName"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfProductName"/>\n  <opc:Field LengthField="NoOfProductName" TypeName="opc:CharArray" Name="ProductName"/>\n  <opc:Field TypeName="opc:CharArray" Name="MouldId"/>\n  <opc:Field TypeName="opc:UInt32" Name="NumCavities"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProductionDatasetReadOptionsType">\n  <opc:Documentation>Used as GenerateOptions in the Method GenerateFileForRead in ProductionDatasetTransfer</opc:Documentation>\n  <opc:Field TypeName="tns:StorageEnumeration" Name="Storage"/>\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProductionDatasetWriteOptionsType">\n  <opc:Documentation>Used as GenerateOptions in the Method GenerateFileForWrite in ProductionDatasetTransfer</opc:Documentation>\n  <opc:Field TypeName="tns:StorageEnumeration" Name="Storage"/>\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfComponents"/>\n  <opc:Field LengthField="NoOfComponents" TypeName="opc:UInt16" Name="Components"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="StandstillReasonType">\n  <opc:Documentation>Description of a standstill reason</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="Text"/>\n  <opc:Field TypeName="opc:Boolean" Name="LockedByMES"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="CavityCycleQualityEnumeration">\n  <opc:Documentation>Quality of the cycle for each cavity</opc:Documentation>\n  <opc:EnumeratedValue Name="NO_PART" Value="0"/>\n  <opc:EnumeratedValue Name="GOOD_PART" Value="1"/>\n  <opc:EnumeratedValue Name="BAD_PART" Value="2"/>\n  <opc:EnumeratedValue Name="REWORK" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ControlModeEnumeration">\n  <opc:Documentation>Indication how the parameter is currently controlled</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="OFF" Value="1"/>\n  <opc:EnumeratedValue Name="AUTOMATIC" Value="2"/>\n  <opc:EnumeratedValue Name="TUNING" Value="3"/>\n  <opc:EnumeratedValue Name="STANDBY" Value="4"/>\n  <opc:EnumeratedValue Name="OPEN_LOOP" Value="5"/>\n  <opc:EnumeratedValue Name="ONLY_MEASUREMENT" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CycleQualityEnumeration">\n  <opc:Documentation>Quality of the whole cycle</opc:Documentation>\n  <opc:EnumeratedValue Name="GOOD_CYCLE" Value="0"/>\n  <opc:EnumeratedValue Name="BAD_CYCLE" Value="1"/>\n  <opc:EnumeratedValue Name="TEST_SAMPLE_CYCLE" Value="2"/>\n  <opc:EnumeratedValue Name="FAILED_CYCLE" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DiagnosticsStatusEnumeration">\n  <opc:EnumeratedValue Name="OFF" Value="0"/>\n  <opc:EnumeratedValue Name="ACTIVE_OK" Value="1"/>\n  <opc:EnumeratedValue Name="ACTIVE_ERROR_DETECTED" Value="2"/>\n  <opc:EnumeratedValue Name="COMPLETE" Value="3"/>\n  <opc:EnumeratedValue Name="COMPLETE_ERROR_DETECTED" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EventOriginatorEnumeration">\n  <opc:Documentation>Originator of an event</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="MACHINE" Value="1"/>\n  <opc:EnumeratedValue Name="OPERATOR" Value="2"/>\n  <opc:EnumeratedValue Name="MES" Value="3"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_DEVICE" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="JobStatusEnumeration">\n  <opc:Documentation>Current status of the job</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="TRANSFERRED_ASSIGNED" Value="1"/>\n  <opc:EnumeratedValue Name="SET_UP_ACTIVE" Value="2"/>\n  <opc:EnumeratedValue Name="SET_UP_INTERRUPTED" Value="3"/>\n  <opc:EnumeratedValue Name="SET_UP_FINISHED" Value="4"/>\n  <opc:EnumeratedValue Name="START_UP_ACTIVE" Value="5"/>\n  <opc:EnumeratedValue Name="JOB_IN_PRODUCTION" Value="6"/>\n  <opc:EnumeratedValue Name="JOB_INTERRUPTED" Value="7"/>\n  <opc:EnumeratedValue Name="JOB_FINISHED" Value="8"/>\n  <opc:EnumeratedValue Name="TEAR_DOWN_ACTIVE" Value="9"/>\n  <opc:EnumeratedValue Name="TEAR_DOWN_INTERRUPTED" Value="10"/>\n  <opc:EnumeratedValue Name="TEAR_DOWN_FINISHED" Value="11"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="LogbookEventsEnumeration">\n  <opc:Documentation>Information which LogbookEvents are supported by the machine</opc:Documentation>\n  <opc:EnumeratedValue Name="PARAMETER_CHANGE" Value="0"/>\n  <opc:EnumeratedValue Name="USER" Value="1"/>\n  <opc:EnumeratedValue Name="REMOTE_ACCESS" Value="2"/>\n  <opc:EnumeratedValue Name="SEQUENCE_CHANGE" Value="3"/>\n  <opc:EnumeratedValue Name="MACHINE_MODE_CHANGE" Value="4"/>\n  <opc:EnumeratedValue Name="PRODUCTION_STATUS_CHANGE" Value="5"/>\n  <opc:EnumeratedValue Name="PRODUCTION_DATASET_CHANGE" Value="6"/>\n  <opc:EnumeratedValue Name="PRODUCTION_DATASET_FROZEN" Value="7"/>\n  <opc:EnumeratedValue Name="STANDSTILL_REASON" Value="8"/>\n  <opc:EnumeratedValue Name="MESSAGE" Value="9"/>\n  <opc:EnumeratedValue Name="USER_FEEDBACK" Value="10"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="MachineModeEnumeration">\n  <opc:Documentation>Current machine mode (as defined by mode selector on the machine)</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="AUTOMATIC" Value="1"/>\n  <opc:EnumeratedValue Name="SEMI_AUTOMATIC" Value="2"/>\n  <opc:EnumeratedValue Name="MANUAL" Value="3"/>\n  <opc:EnumeratedValue Name="SETUP" Value="4"/>\n  <opc:EnumeratedValue Name="SLEEP" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="MaintenanceStatusEnumeration">\n  <opc:Documentation>Maintenance status of a machine/device/component</opc:Documentation>\n  <opc:EnumeratedValue Name="NOT_DUE" Value="0"/>\n  <opc:EnumeratedValue Name="WARNING" Value="1"/>\n  <opc:EnumeratedValue Name="DUE" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="MouldStatusEnumeration">\n  <opc:Documentation>Current (physical) status of the mould</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="MOULD_NOT_INSTALLED" Value="1"/>\n  <opc:EnumeratedValue Name="MOULD_CHANGE" Value="2"/>\n  <opc:EnumeratedValue Name="MOULD_INSTALLED" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ProductionStatusEnumeration">\n  <opc:Documentation>Production status of the machine</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="NO_PRODUCTION" Value="1"/>\n  <opc:EnumeratedValue Name="START_UP" Value="2"/>\n  <opc:EnumeratedValue Name="READY_FOR_PRODUCTION" Value="3"/>\n  <opc:EnumeratedValue Name="PRODUCTION" Value="4"/>\n  <opc:EnumeratedValue Name="DRY_RUN" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SequenceChangeEnumeration">\n  <opc:Documentation>Classification of production sequence change</opc:Documentation>\n  <opc:EnumeratedValue Name="UPDATE" Value="0"/>\n  <opc:EnumeratedValue Name="ADD" Value="1"/>\n  <opc:EnumeratedValue Name="MODIFY" Value="2"/>\n  <opc:EnumeratedValue Name="MOVE" Value="3"/>\n  <opc:EnumeratedValue Name="DELETE" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="StartEnumeration">\n  <opc:EnumeratedValue Name="NOT_READY_TO_START" Value="0"/>\n  <opc:EnumeratedValue Name="START_BLOCKED_BY_CLIENT" Value="1"/>\n  <opc:EnumeratedValue Name="READY_TO_START" Value="2"/>\n  <opc:EnumeratedValue Name="START_REQUESTED" Value="3"/>\n  <opc:EnumeratedValue Name="STARTED" Value="4"/>\n  <opc:EnumeratedValue Name="STOP_REQUESTED" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="StorageEnumeration">\n  <opc:Documentation>Indication which parts of the production dataset shall be activated in the machine control after writing</opc:Documentation>\n  <opc:EnumeratedValue Name="PRODUCTION" Value="1"/>\n  <opc:EnumeratedValue Name="PREPARATION" Value="2"/>\n  <opc:EnumeratedValue Name="FILE_SYSTEM" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="TemperatureZoneClassificationEnumeration">\n  <opc:Documentation>Type of the temperature zone</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="HEATING" Value="1"/>\n  <opc:EnumeratedValue Name="COOLING" Value="2"/>\n  <opc:EnumeratedValue Name="TEMPERATURE_CONTROL" Value="3"/>\n  <opc:EnumeratedValue Name="HOT_RUNNER" Value="4"/>\n  <opc:EnumeratedValue Name="MEASURING" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="UserChangeEnumeration">\n  <opc:Documentation>Information if a user logs in or off</opc:Documentation>\n  <opc:EnumeratedValue Name="LOG_ON" Value="0"/>\n  <opc:EnumeratedValue Name="LOG_OFF" Value="1"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_rubber;i=6717",
    browseName="ns=plastics_rubber;ClassifiedActiveErrorDataType",
    dataType=o6.String,
    value="//xs:element[@name='ClassifiedActiveErrorDataType']",
)
o6.reference(o6.ns["ns=plastics_rubber;i=5066"], "i=39", o6.ns["ns=plastics_rubber;i=6717"])
oPC40083_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_rubber;i=6004",
    browseName="ns=plastics_rubber;OPC40083",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6005",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/Types.xsd",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6292"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6301"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6303"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6392"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6402"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6406"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6408"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6410"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6412"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6414"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6520"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6717"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="CavityCycleQualityEnumeration">\n  <xs:annotation>\n   <xs:documentation>Quality of the cycle for each cavity</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NO_PART_0"/>\n   <xs:enumeration value="GOOD_PART_1"/>\n   <xs:enumeration value="BAD_PART_2"/>\n   <xs:enumeration value="REWORK_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CavityCycleQualityEnumeration" name="CavityCycleQualityEnumeration"/>\n <xs:complexType name="ListOfCavityCycleQualityEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavityCycleQualityEnumeration" name="CavityCycleQualityEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavityCycleQualityEnumeration" name="ListOfCavityCycleQualityEnumeration" nillable="true"/>\n <xs:simpleType name="ControlModeEnumeration">\n  <xs:annotation>\n   <xs:documentation>Indication how the parameter is currently controlled</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="OFF_1"/>\n   <xs:enumeration value="AUTOMATIC_2"/>\n   <xs:enumeration value="TUNING_3"/>\n   <xs:enumeration value="STANDBY_4"/>\n   <xs:enumeration value="OPEN_LOOP_5"/>\n   <xs:enumeration value="ONLY_MEASUREMENT_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ControlModeEnumeration" name="ControlModeEnumeration"/>\n <xs:complexType name="ListOfControlModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ControlModeEnumeration" name="ControlModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfControlModeEnumeration" name="ListOfControlModeEnumeration" nillable="true"/>\n <xs:simpleType name="CycleQualityEnumeration">\n  <xs:annotation>\n   <xs:documentation>Quality of the whole cycle</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="GOOD_CYCLE_0"/>\n   <xs:enumeration value="BAD_CYCLE_1"/>\n   <xs:enumeration value="TEST_SAMPLE_CYCLE_2"/>\n   <xs:enumeration value="FAILED_CYCLE_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CycleQualityEnumeration" name="CycleQualityEnumeration"/>\n <xs:complexType name="ListOfCycleQualityEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CycleQualityEnumeration" name="CycleQualityEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCycleQualityEnumeration" name="ListOfCycleQualityEnumeration" nillable="true"/>\n <xs:simpleType name="DiagnosticsStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OFF_0"/>\n   <xs:enumeration value="ACTIVE_OK_1"/>\n   <xs:enumeration value="ACTIVE_ERROR_DETECTED_2"/>\n   <xs:enumeration value="COMPLETE_3"/>\n   <xs:enumeration value="COMPLETE_ERROR_DETECTED_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DiagnosticsStatusEnumeration" name="DiagnosticsStatusEnumeration"/>\n <xs:complexType name="ListOfDiagnosticsStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DiagnosticsStatusEnumeration" name="DiagnosticsStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDiagnosticsStatusEnumeration" name="ListOfDiagnosticsStatusEnumeration" nillable="true"/>\n <xs:simpleType name="EventOriginatorEnumeration">\n  <xs:annotation>\n   <xs:documentation>Originator of an event</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="MACHINE_1"/>\n   <xs:enumeration value="OPERATOR_2"/>\n   <xs:enumeration value="MES_3"/>\n   <xs:enumeration value="PERIPHERAL_DEVICE_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EventOriginatorEnumeration" name="EventOriginatorEnumeration"/>\n <xs:complexType name="ListOfEventOriginatorEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EventOriginatorEnumeration" name="EventOriginatorEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEventOriginatorEnumeration" name="ListOfEventOriginatorEnumeration" nillable="true"/>\n <xs:simpleType name="JobStatusEnumeration">\n  <xs:annotation>\n   <xs:documentation>Current status of the job</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="TRANSFERRED_ASSIGNED_1"/>\n   <xs:enumeration value="SET_UP_ACTIVE_2"/>\n   <xs:enumeration value="SET_UP_INTERRUPTED_3"/>\n   <xs:enumeration value="SET_UP_FINISHED_4"/>\n   <xs:enumeration value="START_UP_ACTIVE_5"/>\n   <xs:enumeration value="JOB_IN_PRODUCTION_6"/>\n   <xs:enumeration value="JOB_INTERRUPTED_7"/>\n   <xs:enumeration value="JOB_FINISHED_8"/>\n   <xs:enumeration value="TEAR_DOWN_ACTIVE_9"/>\n   <xs:enumeration value="TEAR_DOWN_INTERRUPTED_10"/>\n   <xs:enumeration value="TEAR_DOWN_FINISHED_11"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:JobStatusEnumeration" name="JobStatusEnumeration"/>\n <xs:complexType name="ListOfJobStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:JobStatusEnumeration" name="JobStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJobStatusEnumeration" name="ListOfJobStatusEnumeration" nillable="true"/>\n <xs:simpleType name="LogbookEventsEnumeration">\n  <xs:annotation>\n   <xs:documentation>Information which LogbookEvents are supported by the machine</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="PARAMETER_CHANGE_0"/>\n   <xs:enumeration value="USER_1"/>\n   <xs:enumeration value="REMOTE_ACCESS_2"/>\n   <xs:enumeration value="SEQUENCE_CHANGE_3"/>\n   <xs:enumeration value="MACHINE_MODE_CHANGE_4"/>\n   <xs:enumeration value="PRODUCTION_STATUS_CHANGE_5"/>\n   <xs:enumeration value="PRODUCTION_DATASET_CHANGE_6"/>\n   <xs:enumeration value="PRODUCTION_DATASET_FROZEN_7"/>\n   <xs:enumeration value="STANDSTILL_REASON_8"/>\n   <xs:enumeration value="MESSAGE_9"/>\n   <xs:enumeration value="USER_FEEDBACK_10"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:LogbookEventsEnumeration" name="LogbookEventsEnumeration"/>\n <xs:complexType name="ListOfLogbookEventsEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:LogbookEventsEnumeration" name="LogbookEventsEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLogbookEventsEnumeration" name="ListOfLogbookEventsEnumeration" nillable="true"/>\n <xs:simpleType name="MachineModeEnumeration">\n  <xs:annotation>\n   <xs:documentation>Current machine mode (as defined by mode selector on the machine)</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="AUTOMATIC_1"/>\n   <xs:enumeration value="SEMI_AUTOMATIC_2"/>\n   <xs:enumeration value="MANUAL_3"/>\n   <xs:enumeration value="SETUP_4"/>\n   <xs:enumeration value="SLEEP_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MachineModeEnumeration" name="MachineModeEnumeration"/>\n <xs:complexType name="ListOfMachineModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MachineModeEnumeration" name="MachineModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMachineModeEnumeration" name="ListOfMachineModeEnumeration" nillable="true"/>\n <xs:simpleType name="MaintenanceStatusEnumeration">\n  <xs:annotation>\n   <xs:documentation>Maintenance status of a machine/device/component</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NOT_DUE_0"/>\n   <xs:enumeration value="WARNING_1"/>\n   <xs:enumeration value="DUE_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MaintenanceStatusEnumeration" name="MaintenanceStatusEnumeration"/>\n <xs:complexType name="ListOfMaintenanceStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MaintenanceStatusEnumeration" name="MaintenanceStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMaintenanceStatusEnumeration" name="ListOfMaintenanceStatusEnumeration" nillable="true"/>\n <xs:simpleType name="MouldStatusEnumeration">\n  <xs:annotation>\n   <xs:documentation>Current (physical) status of the mould</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="MOULD_NOT_INSTALLED_1"/>\n   <xs:enumeration value="MOULD_CHANGE_2"/>\n   <xs:enumeration value="MOULD_INSTALLED_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MouldStatusEnumeration" name="MouldStatusEnumeration"/>\n <xs:complexType name="ListOfMouldStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MouldStatusEnumeration" name="MouldStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMouldStatusEnumeration" name="ListOfMouldStatusEnumeration" nillable="true"/>\n <xs:simpleType name="ProductionStatusEnumeration">\n  <xs:annotation>\n   <xs:documentation>Production status of the machine</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="NO_PRODUCTION_1"/>\n   <xs:enumeration value="START_UP_2"/>\n   <xs:enumeration value="READY_FOR_PRODUCTION_3"/>\n   <xs:enumeration value="PRODUCTION_4"/>\n   <xs:enumeration value="DRY_RUN_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ProductionStatusEnumeration" name="ProductionStatusEnumeration"/>\n <xs:complexType name="ListOfProductionStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProductionStatusEnumeration" name="ProductionStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProductionStatusEnumeration" name="ListOfProductionStatusEnumeration" nillable="true"/>\n <xs:simpleType name="SequenceChangeEnumeration">\n  <xs:annotation>\n   <xs:documentation>Classification of production sequence change</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="UPDATE_0"/>\n   <xs:enumeration value="ADD_1"/>\n   <xs:enumeration value="MODIFY_2"/>\n   <xs:enumeration value="MOVE_3"/>\n   <xs:enumeration value="DELETE_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SequenceChangeEnumeration" name="SequenceChangeEnumeration"/>\n <xs:complexType name="ListOfSequenceChangeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SequenceChangeEnumeration" name="SequenceChangeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSequenceChangeEnumeration" name="ListOfSequenceChangeEnumeration" nillable="true"/>\n <xs:simpleType name="StartEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NOT_READY_TO_START_0"/>\n   <xs:enumeration value="START_BLOCKED_BY_CLIENT_1"/>\n   <xs:enumeration value="READY_TO_START_2"/>\n   <xs:enumeration value="START_REQUESTED_3"/>\n   <xs:enumeration value="STARTED_4"/>\n   <xs:enumeration value="STOP_REQUESTED_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:StartEnumeration" name="StartEnumeration"/>\n <xs:complexType name="ListOfStartEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StartEnumeration" name="StartEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStartEnumeration" name="ListOfStartEnumeration" nillable="true"/>\n <xs:simpleType name="StorageEnumeration">\n  <xs:annotation>\n   <xs:documentation>Indication which parts of the production dataset shall be activated in the machine control after writing</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="PRODUCTION_1"/>\n   <xs:enumeration value="PREPARATION_2"/>\n   <xs:enumeration value="FILE_SYSTEM_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:StorageEnumeration" name="StorageEnumeration"/>\n <xs:complexType name="ListOfStorageEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StorageEnumeration" name="StorageEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStorageEnumeration" name="ListOfStorageEnumeration" nillable="true"/>\n <xs:simpleType name="TemperatureZoneClassificationEnumeration">\n  <xs:annotation>\n   <xs:documentation>Type of the temperature zone</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="HEATING_1"/>\n   <xs:enumeration value="COOLING_2"/>\n   <xs:enumeration value="TEMPERATURE_CONTROL_3"/>\n   <xs:enumeration value="HOT_RUNNER_4"/>\n   <xs:enumeration value="MEASURING_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:TemperatureZoneClassificationEnumeration" name="TemperatureZoneClassificationEnumeration"/>\n <xs:complexType name="ListOfTemperatureZoneClassificationEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TemperatureZoneClassificationEnumeration" name="TemperatureZoneClassificationEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTemperatureZoneClassificationEnumeration" name="ListOfTemperatureZoneClassificationEnumeration" nillable="true"/>\n <xs:simpleType name="UserChangeEnumeration">\n  <xs:annotation>\n   <xs:documentation>Information if a user logs in or off</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="LOG_ON_0"/>\n   <xs:enumeration value="LOG_OFF_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:UserChangeEnumeration" name="UserChangeEnumeration"/>\n <xs:complexType name="ListOfUserChangeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:UserChangeEnumeration" name="UserChangeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfUserChangeEnumeration" name="ListOfUserChangeEnumeration" nillable="true"/>\n <xs:complexType name="ActiveErrorDataType">\n  <xs:annotation>\n   <xs:documentation>Iinformation about an active error in a device</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="Severity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Message"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ActiveErrorDataType" name="ActiveErrorDataType"/>\n <xs:complexType name="ListOfActiveErrorDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ActiveErrorDataType" name="ActiveErrorDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfActiveErrorDataType" name="ListOfActiveErrorDataType" nillable="true"/>\n <xs:complexType name="ClassifiedActiveErrorDataType">\n  <xs:annotation>\n   <xs:documentation>Iinformation about an active error in a device including the SoureNodes and a Classification</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ActiveErrorDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfNodeId" name="SourceNodes"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="Classification"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ClassifiedActiveErrorDataType" name="ClassifiedActiveErrorDataType"/>\n <xs:complexType name="ListOfClassifiedActiveErrorDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ClassifiedActiveErrorDataType" name="ClassifiedActiveErrorDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfClassifiedActiveErrorDataType" name="ListOfClassifiedActiveErrorDataType" nillable="true"/>\n <xs:complexType name="ConfigurationParameterType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="DefaultValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="Unit"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ConfigurationParameterType" name="ConfigurationParameterType"/>\n <xs:complexType name="ListOfConfigurationParameterType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConfigurationParameterType" name="ConfigurationParameterType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConfigurationParameterType" name="ListOfConfigurationParameterType" nillable="true"/>\n <xs:complexType name="JobListElementType">\n  <xs:annotation>\n   <xs:documentation>Description of a job in a job list</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="JobName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="JobDescription"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="JobClassification"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CustomerName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ProductionDatasetName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ProductionDatasetDescription"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Material"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="ProductName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="ProductDescription"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="JobPriority"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="PlannedStart"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="PlannedProductionTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="LatestEnd"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JobListElementType" name="JobListElementType"/>\n <xs:complexType name="ListOfJobListElementType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:JobListElementType" name="JobListElementType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJobListElementType" name="ListOfJobListElementType" nillable="true"/>\n <xs:complexType name="CyclicJobListElementType">\n  <xs:annotation>\n   <xs:documentation>Description of a job in a cyclic job list</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:JobListElementType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedLong" name="NominalParts"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedLong" name="NominalBoxParts"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="ExpectedCycleTime"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MouldId"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="NumCavities"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CyclicJobListElementType" name="CyclicJobListElementType"/>\n <xs:complexType name="ListOfCyclicJobListElementType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CyclicJobListElementType" name="CyclicJobListElementType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCyclicJobListElementType" name="ListOfCyclicJobListElementType" nillable="true"/>\n <xs:complexType name="PageEntryDataType">\n  <xs:annotation>\n   <xs:documentation>Information on a page that is implemented in the machine control system and shown on the screen of the machine</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Title"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PageEntryDataType" name="PageEntryDataType"/>\n <xs:complexType name="ListOfPageEntryDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PageEntryDataType" name="PageEntryDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPageEntryDataType" name="ListOfPageEntryDataType" nillable="true"/>\n <xs:complexType name="ParameterSettingType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="Value"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ParameterSettingType" name="ParameterSettingType"/>\n <xs:complexType name="ListOfParameterSettingType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ParameterSettingType" name="ParameterSettingType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfParameterSettingType" name="ListOfParameterSettingType" nillable="true"/>\n <xs:complexType name="PIDParametersDataType">\n  <xs:annotation>\n   <xs:documentation>Structure for storing the parameters of a PID controller</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="P"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="I"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="D"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PIDParametersDataType" name="PIDParametersDataType"/>\n <xs:complexType name="ListOfPIDParametersDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PIDParametersDataType" name="PIDParametersDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPIDParametersDataType" name="ListOfPIDParametersDataType" nillable="true"/>\n <xs:complexType name="ProductionDatasetInformationType">\n  <xs:annotation>\n   <xs:documentation>Information on a production dataset</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MESId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="CreationTimestamp"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="LastModificationTimestamp"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="LastSaveTimestamp"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="UserName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfUInt16" name="Components"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Manufacturer"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SerialNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Model"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ControllerName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="UserMachineName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="LocationName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="ProductName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MouldId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="NumCavities"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProductionDatasetInformationType" name="ProductionDatasetInformationType"/>\n <xs:complexType name="ListOfProductionDatasetInformationType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProductionDatasetInformationType" name="ProductionDatasetInformationType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProductionDatasetInformationType" name="ListOfProductionDatasetInformationType" nillable="true"/>\n <xs:complexType name="ProductionDatasetReadOptionsType">\n  <xs:annotation>\n   <xs:documentation>Used as GenerateOptions in the Method GenerateFileForRead in ProductionDatasetTransfer</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:StorageEnumeration" name="Storage"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProductionDatasetReadOptionsType" name="ProductionDatasetReadOptionsType"/>\n <xs:complexType name="ListOfProductionDatasetReadOptionsType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProductionDatasetReadOptionsType" name="ProductionDatasetReadOptionsType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProductionDatasetReadOptionsType" name="ListOfProductionDatasetReadOptionsType" nillable="true"/>\n <xs:complexType name="ProductionDatasetWriteOptionsType">\n  <xs:annotation>\n   <xs:documentation>Used as GenerateOptions in the Method GenerateFileForWrite in ProductionDatasetTransfer</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:StorageEnumeration" name="Storage"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfUInt16" name="Components"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProductionDatasetWriteOptionsType" name="ProductionDatasetWriteOptionsType"/>\n <xs:complexType name="ListOfProductionDatasetWriteOptionsType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProductionDatasetWriteOptionsType" name="ProductionDatasetWriteOptionsType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProductionDatasetWriteOptionsType" name="ListOfProductionDatasetWriteOptionsType" nillable="true"/>\n <xs:complexType name="StandstillReasonType">\n  <xs:annotation>\n   <xs:documentation>Description of a standstill reason</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Text"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="LockedByMES"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:StandstillReasonType" name="StandstillReasonType"/>\n <xs:complexType name="ListOfStandstillReasonType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StandstillReasonType" name="StandstillReasonType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStandstillReasonType" name="ListOfStandstillReasonType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_rubber;i=6718",
    browseName="ns=plastics_rubber;Status",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6719", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6720", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
o6.reference(plastics_rubber_objtypes.MonitoredParameterAlarmType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=6718"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6026",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="NameFilter", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="MouldId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6027",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7005",
    browseName="ns=plastics_rubber;GetProductionDatasetList",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6026"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6027"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6028",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(nodeId="ns=plastics_rubber;i=7006", browseName="ns=plastics_rubber;SendProductionDatasetList", inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6028"]))

plastics_rubber_objtypes.ProductionDatasetListsType(
    nodeId="ns=plastics_rubber;i=5007",
    browseName="ns=plastics_rubber;ProductionDatasetLists",
    description="Functions for exchanging information on the available production datasets on client and server",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=plastics_rubber;i=7005"]), o6.hasComponent(o6.ns["ns=plastics_rubber;i=7006"])],
    eventNotifier=1,
)
o6.reference(plastics_rubber_objtypes.ProductionDatasetManagementType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5007"])
o6.reference(o6.ns["ns=plastics_rubber;i=5007"], "i=41", plastics_rubber_objtypes.RequestProductionDatasetListEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6030",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6031",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7007",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6030"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6031"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6032",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3007"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6033",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7008",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6032"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6033"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6037",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3004"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6038",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7011",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6037"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6038"]),
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=plastics_rubber;i=5008",
    browseName="ns=plastics_rubber;ProductionDatasetTransfer",
    description="Transfer of production datasets between server and client",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6029", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=7007"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=7008"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=7011"]),
    ],
    eventNotifier=1,
)
o6.reference(plastics_rubber_objtypes.ProductionDatasetManagementType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5008"])
o6.reference(o6.ns["ns=plastics_rubber;i=5008"], "i=41", plastics_rubber_objtypes.RequestProductionDatasetReadEventType)
o6.reference(o6.ns["ns=plastics_rubber;i=5008"], "i=41", plastics_rubber_objtypes.RequestProductionDatasetWriteEventType)
o6.reference(o6.ns["ns=plastics_rubber;i=5008"], "i=41", plastics_rubber_objtypes.RequestProductionDatasetListEventType)
plastics_rubber_objtypes.ActiveJobValuesType(
    nodeId="ns=plastics_rubber;i=5037",
    browseName="ns=plastics_rubber;ActiveJobValues",
    description="Status of the job",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6223",
                browseName="ns=plastics_rubber;BoxId",
                description="Id of the box in which the current production is put in",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6374",
                browseName="ns=plastics_rubber;CurrentLotName",
                description="Name of the current production lot",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6378",
                browseName="ns=plastics_rubber;JobStatus",
                description="Current status of the job",
                dataType=plastics_rubber_datypes.JobStatusEnumeration,
                value=plastics_rubber_datypes.JobStatusEnumeration.OTHER,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7010",
                browseName="ns=plastics_rubber;StartJob",
                description="With this Method the client (e.g. MES) request the machine to change the JobStatus to JOB_IN_PRODUCTION_6",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7012",
                browseName="ns=plastics_rubber;InterruptJob",
                description="With this Method the client (e.g. MES) requests the machine to change the JobStatus to JOB_INTERRUPTED_7",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7013",
                browseName="ns=plastics_rubber;FinishJob",
                description="With this Method the client (e.g. MES) requests the machine to change the JobStatus to JOB_FINISHED_8",
            )
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.JobsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5037"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6189",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7015",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6189"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6274",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7023",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6274"]),
)

plastics_rubber_objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_rubber;i=5011",
    browseName="ns=plastics_rubber;ProductionDatasetInPreparationStatus",
    description="Status of the production dataset in the preparation layer",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6136",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber_datypes.ProductionDatasetInformationType,
                value=plastics_rubber_datypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[""],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6188",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6273",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=7015"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=7023"]),
    ],
)
o6.reference(plastics_rubber_objtypes.ProductionDatasetManagementType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5011"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6278",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7027",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6278"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6231",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="WatchDogTime", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7038",
    browseName="ns=plastics_rubber;SetWatchDogTime",
    description="Release of production for a given time",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6231"]),
)

plastics_rubber_objtypes.ProductionControlType(
    nodeId="ns=plastics_rubber;i=5030",
    browseName="ns=plastics_rubber;ProductionControl",
    description="Control of the production of the machine by MES",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6103",
                browseName="ns=plastics_rubber;ProductionReleasedByMES",
                description="Indication if ProductionStatus may have the value PRODUCTION_4",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6227",
                browseName="ns=plastics_rubber;AutomaticRunEnabled",
                description="Indication if semi-automatic and automatic run of the machine is allowed by MES",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6229",
                browseName="ns=plastics_rubber;ProductionOnlyWithMES",
                description="Indication if production with the machine is only allowed when the MES is active",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6230",
                browseName="ns=plastics_rubber;ProductionStatus",
                description="Production status when the machine is in automatic or semi-automatic mode",
                dataType=plastics_rubber_datypes.ProductionStatusEnumeration,
                value=plastics_rubber_datypes.ProductionStatusEnumeration.OTHER,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7014",
                browseName="ns=plastics_rubber;RequestTestSample",
                description="The machine shall separate a test sample (e.g. for quality check). The size of the test sample depends on the product/machine configuration.",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7033",
                browseName="ns=plastics_rubber;DisableAutomaticRun",
                description="Method for disabling the semi-automatic and automatic run of the machine",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7035",
                browseName="ns=plastics_rubber;EnableAutomaticRun",
                description="Method for enabling the semi-automatic and automatic run of the machine",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7037",
                browseName="ns=plastics_rubber;ResetWatchDog",
                description="Setting the watch dog timer to the value set by the last calling of SetWatchDogTime",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=7038"]),
    ],
)
o6.reference(plastics_rubber_objtypes.MachineMESStatusType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5030"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6282",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7044",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6282"]),
)

plastics_rubber_objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_rubber;i=5032",
    browseName="ns=plastics_rubber;ActiveProductionDatasetStatus",
    description="Status of the active production dataset",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6276",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber_datypes.ProductionDatasetInformationType,
                value=plastics_rubber_datypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[""],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6277",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6280",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=7027"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=7044"]),
    ],
)
o6.reference(plastics_rubber_objtypes.ProductionDatasetManagementType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5032"])
plastics_rubber_objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_rubber;i=5035",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6371",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6372",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6373",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber_datypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[1],
                value=[plastics_rubber_datypes.PIDParametersDataType(p=0.0, i=0.0, d=0.0)],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7049",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7050", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
o6.reference(plastics_rubber_objtypes.ControlledParameterType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5035"])
plastics_rubber_objtypes.MaintenanceType(
    nodeId="ns=plastics_rubber;i=5053",
    browseName="ns=plastics_rubber;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6399",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber_datypes.MaintenanceStatusEnumeration,
                value=plastics_rubber_datypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6430",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6434"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6436"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6438"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7052", browseName="ns=plastics_rubber;Reset", description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0"
            )
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.DriveType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5053"])
plastics_rubber_objtypes.MonitoredParameterType(
    nodeId="ns=plastics_rubber;i=5046",
    browseName="ns=plastics_rubber;Speed",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6449",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6388"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6446"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6450"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6452"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6454"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6456"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6458"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6467"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6469"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6471"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6473"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6475"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7054",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.DriveType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5046"])
plastics_rubber_objtypes.StartDeviceType(
    nodeId="ns=plastics_rubber;i=5040",
    browseName="ns=plastics_rubber;StartDevice",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6380", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6387",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber_datypes.StartEnumeration,
                value=plastics_rubber_datypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7061", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7062", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
o6.reference(plastics_rubber_objtypes.MeasuringDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5040"])
plastics_rubber_objtypes.MaintenanceType(
    nodeId="ns=plastics_rubber;i=5047",
    browseName="ns=plastics_rubber;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6505",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber_datypes.MaintenanceStatusEnumeration,
                value=plastics_rubber_datypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6515",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6496"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6506"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6508"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_rubber;i=7063", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.MeasuringDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5047"])
plastics_rubber_objtypes.StartDeviceType(
    nodeId="ns=plastics_rubber;i=5044",
    browseName="ns=plastics_rubber;StartDrive",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6504",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber_datypes.StartEnumeration,
                value=plastics_rubber_datypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6684", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7055", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7064", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
o6.reference(plastics_rubber_objtypes.DriveType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5044"])
plastics_rubber_objtypes.MonitoredParameterType(
    nodeId="ns=plastics_rubber;i=5050",
    browseName="ns=plastics_rubber;Torque",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6490",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6393"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6487"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6491"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6493"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6537"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6539"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6541"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6544"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6546"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6548"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6550"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6552"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7065",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.DriveType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5050"])
plastics_rubber_objtypes.MaintenanceType(
    nodeId="ns=plastics_rubber;i=5057",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6567",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber_datypes.MaintenanceStatusEnumeration,
                value=plastics_rubber_datypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6580",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6581"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6584"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6587"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7066", browseName="ns=plastics_rubber;Reset", description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0"
            )
        ),
    ],
)
plastics_rubber_objtypes.MonitoredParameterType(
    nodeId="ns=plastics_rubber;i=5058",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6593",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6568"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6590"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6594"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6597"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6600"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6603"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6606"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6609"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6612"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6615"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6618"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6621"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7067",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber_objtypes.StartDeviceType(
    nodeId="ns=plastics_rubber;i=5059",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6570",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber_datypes.StartEnumeration,
                value=plastics_rubber_datypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6685", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7068", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7069", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber_objtypes.MonitoredParameterType(
    nodeId="ns=plastics_rubber;i=5060",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6627",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6571"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6624"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6628"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6631"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6634"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6637"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6640"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6643"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6646"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6649"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6652"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6655"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7070",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber_objtypes.DriveType(
    nodeId="ns=plastics_rubber;i=5054",
    browseName="ns=plastics_rubber;<Name>_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6722", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5055"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5056"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5057"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5058"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5059"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5060"]),
    ],
)
o6.reference(plastics_rubber_objtypes.DrivesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5054"])
plastics_rubber_objtypes.MaintenanceType(
    nodeId="ns=plastics_rubber;i=5063",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6661",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber_datypes.MaintenanceStatusEnumeration,
                value=plastics_rubber_datypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6691",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6692"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6695"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6698"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_rubber;i=7071", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_rubber_objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_rubber;i=5062",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6686",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6687",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6688",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber_datypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[1],
                value=[plastics_rubber_datypes.PIDParametersDataType(p=0.0, i=0.0, d=0.0)],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7073",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7074", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber_objtypes.StartDeviceType(
    nodeId="ns=plastics_rubber;i=5064",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6382", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6675",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber_datypes.StartEnumeration,
                value=plastics_rubber_datypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7075", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7076", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber_objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_rubber;i=5045",
    browseName="ns=plastics_rubber;<Name>_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6461", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6462",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber_datypes.ControlModeEnumeration,
                value=plastics_rubber_datypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6463", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6464", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6465", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_rubber;i=6575",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5062"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5063"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=5064"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6053"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6383"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6576"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6578"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6662"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6664"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6666"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6669"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6671"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6673"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6676"]),
        o6.hasComponent(o6.ns["ns=plastics_rubber;i=6678"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_rubber;i=7072",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_rubber_objtypes.MeasuringDevicesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_rubber;i=5045"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber_datypes, plastics_rubber_objtypes
