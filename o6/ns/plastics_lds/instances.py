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

"""Generated OPC UA plastics_lds namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_lds_datypes
from . import objtypes as plastics_lds_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6003",
    browseName="EnumValues",
    parent="ns=plastics_lds;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("GOOD"), description=o6.LocalizedText("Component has no error or warning.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("WARNING"), description=o6.LocalizedText("The component has an undefined warning, but no need to stop the production.")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("WARNING_PRESSURE_TOO_HIGH"),
            description=o6.LocalizedText("Pressure is too high. No need to stop the process but influence to the part quality."),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("WARNING_PRESSURE_TOO_LOW"),
            description=o6.LocalizedText("Pressure is too low. No need to stop the process but influence to the part quality."),
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("ADVANCE_WARNING_DRUM_CHANGE"), description=o6.LocalizedText("Warning, barrel change is imminent. No need to stop the process.")
        ),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("ERROR_DRUM_EMPTY"), description=o6.LocalizedText("Drum of the component is empty. Production needs to be stopped.")
        ),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("ERROR"), description=o6.LocalizedText("The component has an error and process needs to be stopped.")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6011",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6012", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6015", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6016",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6017", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6018", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6028",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6029", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6030", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6044",
    browseName="ns=plastics_lds;ActualPressure",
    description="Actual pressure of the component",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6045", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6051", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_lds_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6044"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6046",
    browseName="ns=plastics_lds;ResidualAmount",
    description="Residual amount of the material",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6047", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6053", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_lds_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6046"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6040",
    browseName="ns=plastics_lds;SetValueDensity",
    description="Set point material density",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6041", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6054", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_lds_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6040"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6055",
    browseName="EnumStrings",
    parent="ns=plastics_lds;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("OFF"),
        o6.LocalizedText("COMPONENT_A"),
        o6.LocalizedText("COMPONENT_B"),
        o6.LocalizedText("COMPONENT_A_AND_B"),
        o6.LocalizedText("COMPONENT_A_AND_B_CYCLIC"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6056",
    browseName="EnumStrings",
    parent="ns=plastics_lds;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("NOT_AVAILABLE"), o6.LocalizedText("ALWAYS_ACTIVE"), o6.LocalizedText("SELECTABLE")],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6062",
    browseName="ns=plastics_lds;DeliveryType",
    description="Indication if the dosing system works with delivery pressure or volumetric flow",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6063", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6064", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6062"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6065",
    browseName="ns=plastics_lds;DeliveryPressureMeasuringPoint",
    description="Position of the pressure sensor used for the DeliveryPressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6066", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6067", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6065"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6082",
    browseName="ns=plastics_lds;PurgeMode",
    description="Depending on this preselected PurgeMode, various purge function can be activated via the dosing signal of the IMM",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6083", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6084", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6082"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6087",
    browseName="EnumValues",
    parent="ns=plastics_lds;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("GOOD"), description=o6.LocalizedText("Component has no error or warning.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("WARNING"), description=o6.LocalizedText("The component has an undefined warning, but no need to stop the production.")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("ADVANCE_WARNING_ADDITIVE_CHANGE"),
            description=o6.LocalizedText("Warning, additive change is imminent. No need to stop the process."),
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("ERROR_EMPTY"), description=o6.LocalizedText("Error, the additive is empty. Production needs to be stopped.")
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ERROR"), description=o6.LocalizedText("The additive has an error and process needs to be stopped.")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6073",
    browseName="ns=plastics_lds;ActualShotWeight",
    description="Specifies the value determined by the feeder as the shot weight",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6074", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6091", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6073"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6060",
    browseName="ns=plastics_lds;ActivateRemoteControl",
    description="With this variable the client selects the method of remote control",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6085", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6095", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6060"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6096",
    browseName="ns=plastics_lds;ActivateRemoteControl",
    description="With this variable the client selects the method of remote control",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6099", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6101", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6070",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6071", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6104", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6105",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6106", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6107", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6117",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6118", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6119", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6068",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6069", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6130", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6131",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6132", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6133", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6143",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6144", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6145", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6079",
    browseName="ns=plastics_lds;MaxDeviationMixingRatio",
    description="Used to limit the maximum deviation in percent",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6080", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6156", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6079"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6157",
    browseName="ns=plastics_lds;MaxDeviationMixingRatio",
    description="Used to limit the maximum deviation in percent",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6158", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6159", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=plastics_lds;i=6160",
    browseName="ns=plastics_lds;RemainingMaterialTime",
    description="Remaining time until first material is empty",
    dataType=ns0.datatypes.Duration,
    value=0.0,
)
o6.reference(o6.ns["ns=plastics_lds;i=6160"], "i=41", plastics_lds_objtypes.LDSCycleParametersEventType)
plastics_rubber.objtypes.IdentificationType(
    nodeId="ns=plastics_lds;i=5008",
    browseName="ns=plastics_lds;Identification",
    description="Identification of the device",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6161",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose a certain device is used",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6162", browseName="ns=di;Manufacturer", description="Provides the name of the manufacturer of the machine", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6163", browseName="ns=di;Model", description="Represents the name of the machine type", dataType=o6.LocalizedText)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6164",
                browseName="ns=di;SerialNumber",
                description="Represents the serial number of the machine (unique ID given by the manufacturer)",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6165", browseName="ns=di;AssetId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6166", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6167", browseName="ns=di;DeviceManual", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6168", browseName="ns=di;DeviceRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6169", browseName="ns=di;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6170", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6171", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6172", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6173", browseName="ns=di;RevisionCounter", dataType=o6.Int32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6174", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6175",
                browseName="ns=plastics_rubber;YearOfConstruction",
                description="Represents the year of construction of the machine",
                dataType=o6.UInt16,
            )
        ),
    ],
)
o6.reference(plastics_lds_objtypes.LDS_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5008"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6086",
    browseName="ns=plastics_lds;RemoteControlActivated",
    description="With this signal, the LDS signalizes, if it is ready to be controlled via this or a separate interface",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6103", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6178", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6086"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6179",
    browseName="ns=plastics_lds;RemoteControlActivated",
    description="With this signal, the LDS signalizes, if it is ready to be controlled via this or a separate interface",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6180", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6181", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6075",
    browseName="ns=plastics_lds;SetShotWeight",
    description="Reference value determined by the IMM or defined by the user on the IMM side",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6076", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6182", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6075"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6077",
    browseName="ns=plastics_lds;SetValueCompositeDensity",
    description="The composite set point of density",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6078", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6077"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6194",
    browseName="ns=plastics_lds;DeliveryType",
    description="Indication if the dosing system works with delivery pressure or volumetric flow",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6195", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6196", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6214",
    browseName="ns=plastics_lds;ActivateMaterialBalanceSystem",
    description="If the value is true, the material balance system is activated",
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=plastics_lds;i=6214"], "i=41", plastics_lds_objtypes.LDSCycleParametersEventType)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6135",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6136", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6221",
    browseName="ns=plastics_lds;DeliveryPressureMeasuringPoint",
    description="Position of the pressure sensor used for the DeliveryPressure",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6222", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6223", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6227",
    browseName="ns=plastics_lds;PurgeMode",
    description="Depending on this preselected PurgeMode, various purge function can be activated via the dosing signal of the IMM",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6228", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6229", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6137",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6138", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6234", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6139",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6140", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6235", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6141",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6142", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6236", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6146",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6147", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6237", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6148",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6149", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6238", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6150",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6151", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6239", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6152",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6153", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6240", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6154",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6155", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6241", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6246",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6247", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6248", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6258",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6259", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6260", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6271",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6272", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6273", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6278",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6279", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6280", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6281",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6282", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6283", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6184",
    browseName="ns=plastics_lds;PurgeQuantity",
    description="Amount of material during the active purge mode",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6185", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6289", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6184"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6186",
    browseName="ns=plastics_lds;PurgeCyclicQuantity",
    description="Amount of material during a purge ccle as the sum of both components",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6187", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6290", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6186"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6286",
    browseName="ns=plastics_lds;PurgeQuantity",
    description="Amount of material during the active purge mode",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6287", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6303", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6225",
    browseName="ns=plastics_lds;PurgeCyclicQuantity",
    description="Amount of material during a purge ccle as the sum of both components",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6226", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6304", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6306",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6307", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5004",
    browseName="ns=plastics_lds;AdditiveFraction",
    description="Contains the SetValue, ActualValue, LowerTolerance and UpperTolerance of the additive fraction in percent",
    references=[o6.hasComponent(o6.ns["ns=plastics_lds;i=6306"])],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6308",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6309", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5014",
    browseName="ns=plastics_lds;AdditiveStrokeVolume",
    description="Defines the value of additive per shot/stroke",
    references=[o6.hasComponent(o6.ns["ns=plastics_lds;i=6308"])],
)
oPC40082_3 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_lds;i=6004",
    browseName="ns=plastics_lds;OPC40082_3",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/LDS/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6005", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/LDS/")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6311",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:ua="http://opcfoundation.org/UA/" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/LDS/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/LDS/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType Name="AdditiveStatusEnumeration" LengthInBits="32">\n  <opc:Documentation>Actual status of the additive provides a minimal error handling for devices without event support.</opc:Documentation>\n  <opc:EnumeratedValue Name="GOOD" Value="0"/>\n  <opc:EnumeratedValue Name="WARNING" Value="1"/>\n  <opc:EnumeratedValue Name="ADVANCE_WARNING_ADDITIVE_CHANGE" Value="2"/>\n  <opc:EnumeratedValue Name="ERROR_EMPTY" Value="3"/>\n  <opc:EnumeratedValue Name="ERROR" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="ComponentStatusEnumeration" LengthInBits="32">\n  <opc:Documentation>Actual status of the component provides a minimal error handling for devices without event support.</opc:Documentation>\n  <opc:EnumeratedValue Name="GOOD" Value="0"/>\n  <opc:EnumeratedValue Name="WARNING" Value="1"/>\n  <opc:EnumeratedValue Name="WARNING_PRESSURE_TOO_HIGH" Value="2"/>\n  <opc:EnumeratedValue Name="WARNING_PRESSURE_TOO_LOW" Value="3"/>\n  <opc:EnumeratedValue Name="ADVANCE_WARNING_DRUM_CHANGE" Value="4"/>\n  <opc:EnumeratedValue Name="ERROR_DRUM_EMPTY" Value="5"/>\n  <opc:EnumeratedValue Name="ERROR" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="MaterialBalanceSystemTypeEnumeration" LengthInBits="32">\n  <opc:EnumeratedValue Name="NOT_AVAILABLE" Value="0"/>\n  <opc:EnumeratedValue Name="ALWAYS_ACTIVE" Value="1"/>\n  <opc:EnumeratedValue Name="SELECTABLE" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="PurgeStatusEnumeration" LengthInBits="32">\n  <opc:EnumeratedValue Name="OFF" Value="0"/>\n  <opc:EnumeratedValue Name="COMPONENT_A" Value="1"/>\n  <opc:EnumeratedValue Name="COMPONENT_B" Value="2"/>\n  <opc:EnumeratedValue Name="COMPONENT_A_AND_B" Value="3"/>\n  <opc:EnumeratedValue Name="COMPONENT_A_AND_B_CYCLIC" Value="4"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6215",
    browseName="ns=plastics_lds;ActualShotWeight",
    description="Specifies the value determined by the feeder as the shot weight",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6216", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6312", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6230",
    browseName="ns=plastics_lds;SetShotWeight",
    description="Reference value determined by the IMM or defined by the user on the IMM side",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6231", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6313", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6232",
    browseName="ns=plastics_lds;SetValueCompositeDensity",
    description="The composite set point of density",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6233", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6314", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6020",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6021", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6319", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6022",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6023", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6320", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6024",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6025", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6321", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6026",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6027", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6322", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6031",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6032", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6323", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6033",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6034", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6324", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6035",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6036", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6325", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6037",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6038", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6326", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6092",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6093", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6327", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6013",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6014", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6328", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6329",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6330", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6331", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6341",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6342", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6343", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6333",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6334", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6357", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6335",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6336", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6358", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6337",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6338", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6359", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
oPC40082_3_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_lds;i=6006",
    browseName="ns=plastics_lds;OPC40082_3",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/LDS/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6007", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/LDS/Types.xsd"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6360",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" elementFormDefault="qualified" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/LDS/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/LDS/Types.xsd">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AdditiveStatusEnumeration">\n  <xs:annotation>\n   <xs:documentation>Actual status of the additive provides a minimal error handling for devices without event support.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="GOOD_0"/>\n   <xs:enumeration value="WARNING_1"/>\n   <xs:enumeration value="ADVANCE_WARNING_ADDITIVE_CHANGE_2"/>\n   <xs:enumeration value="ERROR_EMPTY_3"/>\n   <xs:enumeration value="ERROR_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="AdditiveStatusEnumeration" type="tns:AdditiveStatusEnumeration"/>\n <xs:complexType name="ListOfAdditiveStatusEnumeration">\n  <xs:sequence>\n   <xs:element name="AdditiveStatusEnumeration" type="tns:AdditiveStatusEnumeration" nillable="true" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAdditiveStatusEnumeration" type="tns:ListOfAdditiveStatusEnumeration" nillable="true"/>\n <xs:simpleType name="ComponentStatusEnumeration">\n  <xs:annotation>\n   <xs:documentation>Actual status of the component provides a minimal error handling for devices without event support.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="GOOD_0"/>\n   <xs:enumeration value="WARNING_1"/>\n   <xs:enumeration value="WARNING_PRESSURE_TOO_HIGH_2"/>\n   <xs:enumeration value="WARNING_PRESSURE_TOO_LOW_3"/>\n   <xs:enumeration value="ADVANCE_WARNING_DRUM_CHANGE_4"/>\n   <xs:enumeration value="ERROR_DRUM_EMPTY_5"/>\n   <xs:enumeration value="ERROR_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="ComponentStatusEnumeration" type="tns:ComponentStatusEnumeration"/>\n <xs:complexType name="ListOfComponentStatusEnumeration">\n  <xs:sequence>\n   <xs:element name="ComponentStatusEnumeration" type="tns:ComponentStatusEnumeration" nillable="true" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfComponentStatusEnumeration" type="tns:ListOfComponentStatusEnumeration" nillable="true"/>\n <xs:simpleType name="MaterialBalanceSystemTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NOT_AVAILABLE_0"/>\n   <xs:enumeration value="ALWAYS_ACTIVE_1"/>\n   <xs:enumeration value="SELECTABLE_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="MaterialBalanceSystemTypeEnumeration" type="tns:MaterialBalanceSystemTypeEnumeration"/>\n <xs:complexType name="ListOfMaterialBalanceSystemTypeEnumeration">\n  <xs:sequence>\n   <xs:element name="MaterialBalanceSystemTypeEnumeration" type="tns:MaterialBalanceSystemTypeEnumeration" nillable="true" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfMaterialBalanceSystemTypeEnumeration" type="tns:ListOfMaterialBalanceSystemTypeEnumeration" nillable="true"/>\n <xs:simpleType name="PurgeStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OFF_0"/>\n   <xs:enumeration value="COMPONENT_A_1"/>\n   <xs:enumeration value="COMPONENT_B_2"/>\n   <xs:enumeration value="COMPONENT_A_AND_B_3"/>\n   <xs:enumeration value="COMPONENT_A_AND_B_CYCLIC_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="PurgeStatusEnumeration" type="tns:PurgeStatusEnumeration"/>\n <xs:complexType name="ListOfPurgeStatusEnumeration">\n  <xs:sequence>\n   <xs:element name="PurgeStatusEnumeration" type="tns:PurgeStatusEnumeration" nillable="true" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPurgeStatusEnumeration" type="tns:ListOfPurgeStatusEnumeration" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6284",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6285", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6366", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6367",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6368", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6369", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6370",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6371", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6372", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6373",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6374", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6375", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6376",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6377", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6378", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6379",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6380", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6381", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6382",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6383", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6384", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6385",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6386", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6387", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6242",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6243", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6388", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6244",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6245", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6389", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6109",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6110", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6393", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6111",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6112", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6394", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6113",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6114", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6395", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6115",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6116", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6396", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6120",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6121", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6397", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6122",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6123", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6398", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6124",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6125", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6399", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6126",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6127", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6400", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6128",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6129", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6401", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6339",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6340", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6421", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6344",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6345", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6422", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6423",
    browseName="ns=plastics_lds;ActualDeviationMixingRatio",
    description="Actual deviation of the mixing ratio (in percent)",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6424", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6428", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6426",
    browseName="ns=plastics_lds;TargetDeviationMixingRatio",
    description="This deviation (in percent) is set/used by the material balance system",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6427", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6429", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashLDSSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_lds;i=5017",
    browseName="ns=plastics_lds;http://opcfoundation.org/UA/PlasticsRubber/LDS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6202", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6203", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-04-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6204", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/LDS/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6433", browseName="NamespaceVersion", dataType=o6.String, value="1.02.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6437",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6438", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6439", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6346",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6347", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6440", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6348",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6349", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6441", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6350",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6351", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6442", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6352",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6353", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6443", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6250",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6251", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6444", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6252",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6253", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6445", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6254",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6255", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6446", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6256",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6257", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6447", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6452",
    browseName="ns=plastics_lds;MixingRatioTarget",
    description="Target mixing ratio of the last cycle (includes ratio change when MaterialBalanceSystem is active)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6453", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6454", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6452"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6483",
    browseName="ns=plastics_lds;AdditivesPressure",
    description="Average pressure of the additive during the last cycle at the measuring point",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6484", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6489", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6483"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6461",
    browseName="ns=plastics_lds;AdditivesRatioActual",
    description="Actual ratios of additive in percentage",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6462", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6490", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6461"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6457",
    browseName="ns=plastics_lds;AdditivesRatioTarget",
    description="Target ratios of additives in percentage which are set in AdditiveFraction of AdditiveType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6458", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6491", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6457"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6485",
    browseName="ns=plastics_lds;FilterPressurePrimary",
    description="Average material pressure during the last cycle before the filter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6486", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6492", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6485"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6487",
    browseName="ns=plastics_lds;FilterPressureSecondary",
    description="Average material pressure during the last cycle after the filter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6488", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6493", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6487"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6477",
    browseName="ns=plastics_lds;MixingPointPressureA",
    description="Average pressure of component A during the last cycle at the blender",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6478", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6494", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6477"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6479",
    browseName="ns=plastics_lds;MixingPointPressureB",
    description="Average pressure of component B during the last cycle at the blender",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6480", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6495", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6479"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6481",
    browseName="ns=plastics_lds;MixingPointPressureBlender",
    description="Average pressure of components A and B during the last cycle at the blender",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6482", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6496", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6481"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6455",
    browseName="ns=plastics_lds;MixingRatioActual",
    description="Actual mixing ratio of the components",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6456", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6497", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6455"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6473",
    browseName="ns=plastics_lds;ResidualAmountA",
    description="Residual weight amount of component A at the end of the dosing cycle",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6474", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6499", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6473"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6475",
    browseName="ns=plastics_lds;ResidualAmountB",
    description="Residual weight amount of component B at the end of the dosing cycle",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6476", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6500", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6475"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6463",
    browseName="ns=plastics_lds;VolumeA",
    description="Volume of component A that was added to the process in the last cycle",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6464", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6501", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6463"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6467",
    browseName="ns=plastics_lds;VolumeAB",
    description="Volume of components A + B that was added to the process in the last cycle",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6468", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6502", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6467"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6469",
    browseName="ns=plastics_lds;VolumeAdditives",
    description="Volumes of the additives that were added to the process in the last cycle",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6470", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6503", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6469"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6465",
    browseName="ns=plastics_lds;VolumeB",
    description="Volume of component B that was added to the process in the last cycle",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6466", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6504", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6465"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6471",
    browseName="ns=plastics_lds;VolumeTotal",
    description="Volume of all components (A + B + all additives)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6472", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6505", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.LDSCycleParametersEventType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6471"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6508",
    browseName="ns=plastics_lds;ActualDeviationMixingRatio",
    description="Actual deviation of the mixing ratio (in percent)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6509", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6510", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6508"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6515",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6516", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6517", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6522",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6523", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6524", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6525",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6526", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6527", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6528",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6529", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6530", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6531",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6532", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6533", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6534",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6535", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6536", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6537",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6538", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6539", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6540",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6541", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6542", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6543",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6544", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6545", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6546",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6547", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6548", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6549",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6550", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6551", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6552",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6553", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6554", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6559",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6560", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6561", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6562",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6563", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6564", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6565",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6566", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6567", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6568",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6569", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6570", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6571",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6572", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6573", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6574",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6575", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6576", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6577",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6578", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6579", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6580",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6581", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6582", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6583",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6584", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6585", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6586",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6587", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6588", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6511",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6512", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6589", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6513",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6514", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6590", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6198",
    browseName="ns=plastics_lds;TargetDeviationMixingRatio",
    description="This deviation (in percent) is set/used by the material balance system",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6593", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6594", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6198"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6261",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6262", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6595", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6263",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6596", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6265",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6266", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6597", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6267",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6268", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6598", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6269",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6270", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6599", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6097",
    browseName="ns=plastics_lds;MixingRatioTarget",
    description="Target of the mixing ratio (includes ratio change when MaterialBalanceSystem is active)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6098", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6620", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6097"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6176",
    browseName="ns=plastics_lds;MixingRatioTarget",
    description="Target of the mixing ratio (includes ratio change when MaterialBalanceSystem is active)",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6177", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6624", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6001",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6002", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6631", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
plastics_lds_objtypes.AdditiveType(
    nodeId="ns=plastics_lds;i=5015",
    browseName="ns=plastics_lds;Additive_<Y>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6305",
                browseName="ns=plastics_lds;ActivateClosedLoopControl",
                description="Activate the closed loop control of the additive",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6310",
                browseName="ns=plastics_lds;ClosedLoopControlActivated",
                description="Is true if the closed loop control of the additive is activated",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6434",
                browseName="ns=plastics_lds;ActivateAdditive",
                description="Set value to activate the additive",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6435",
                browseName="ns=plastics_lds;AdditiveActivated",
                description="Is true if the additive is activated.",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6436",
                browseName="ns=plastics_lds;Status",
                description="Actual status of the additive provides a minimal error handling for devices without event support.",
                dataType=plastics_lds_datypes.AdditiveStatusEnumeration,
                value=plastics_lds_datypes.AdditiveStatusEnumeration.GOOD,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6638",
                browseName="ns=plastics_lds;IsPresent",
                description="Informs the client if the additive is physically present.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5004"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5014"]),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6632",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6639", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6640", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6364",
    browseName="ns=plastics_lds;ActualPressure",
    description="Actual pressure of the component",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6365", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6644", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6622",
    browseName="ns=plastics_lds;ResidualAmount",
    description="Residual amount of the material",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6623", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6646", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6626",
    browseName="ns=plastics_lds;SetValueDensity",
    description="Set point material density",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6627", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6647", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6628",
    browseName="ns=plastics_lds;ActualPressure",
    description="Actual pressure of the component",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6629", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6648", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6634",
    browseName="ns=plastics_lds;ResidualAmount",
    description="Residual amount of the material",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6635", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6650", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6642",
    browseName="ns=plastics_lds;SetValueDensity",
    description="Set point material density",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6643", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6651", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6656",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6660", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6667", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6652",
    browseName="ns=plastics_lds;ActualPressure",
    description="Actual pressure of the component",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6653", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6676", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6668",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6672", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6677", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6658",
    browseName="ns=plastics_lds;ResidualAmount",
    description="Residual amount of the material",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6659", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6678", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6662",
    browseName="ns=plastics_lds;SetValueDensity",
    description="Set point material density",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6663", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6679", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6664",
    browseName="ns=plastics_lds;ActualPressure",
    description="Actual pressure of the component",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6665", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6680", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6670",
    browseName="ns=plastics_lds;ResidualAmount",
    description="Residual amount of the material",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6671", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6682", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6674",
    browseName="ns=plastics_lds;SetValueDensity",
    description="Set point material density",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6675", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6683", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6686",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6687", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6688", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6689",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6690", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6691", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6692",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6693", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6694", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_lds;i=6695",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6696", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6697", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6698",
    browseName="ns=plastics_lds;ActualFollowerPlatePressure",
    description="Actual material pressure under the follower plate",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6699", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6704", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6698"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6700",
    browseName="ns=plastics_lds;SetFollowerPlatePressure",
    description="Set value for material pressure under the follower plate",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6701", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6705", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_lds_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6700"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6702",
    browseName="ns=plastics_lds;DrumCapacity",
    description="Maximum capacity of the drum",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6703", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6706", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_lds_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=6702"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6707",
    browseName="ns=plastics_lds;ActualFollowerPlatePressure",
    description="Actual material pressure under the follower plate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6291", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6708", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6709",
    browseName="ns=plastics_lds;DrumCapacity",
    description="Maximum capacity of the drum",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6292", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6710", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6711",
    browseName="ns=plastics_lds;SetFollowerPlatePressure",
    description="Set value for material pressure under the follower plate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6293", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6712", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6713",
    browseName="ns=plastics_lds;ActualFollowerPlatePressure",
    description="Actual material pressure under the follower plate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6294", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6714", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6715",
    browseName="ns=plastics_lds;DrumCapacity",
    description="Maximum capacity of the drum",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6295", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6716", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6717",
    browseName="ns=plastics_lds;SetFollowerPlatePressure",
    description="Set value for material pressure under the follower plate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6296", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6718", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6719",
    browseName="ns=plastics_lds;ActualFollowerPlatePressure",
    description="Actual material pressure under the follower plate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6297", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6720", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6721",
    browseName="ns=plastics_lds;DrumCapacity",
    description="Maximum capacity of the drum",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6298", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6722", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6723",
    browseName="ns=plastics_lds;SetFollowerPlatePressure",
    description="Set value for material pressure under the follower plate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6299", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6724", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6725",
    browseName="ns=plastics_lds;ActualFollowerPlatePressure",
    description="Actual material pressure under the follower plate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6300", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6726", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6727",
    browseName="ns=plastics_lds;DrumCapacity",
    description="Maximum capacity of the drum",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6301", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6728", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_lds;i=6729",
    browseName="ns=plastics_lds;SetFollowerPlatePressure",
    description="Set value for material pressure under the follower plate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6302", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6730", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6189",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7007",
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
    nodeId="ns=plastics_lds;i=7007",
    browseName="ns=plastics_rubber;SetMachineTime",
    description="Method for setting the server time together with TimeZoneOffset",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6189"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6209",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VisualisationUnit", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6210",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7008",
    browseName="ns=plastics_rubber;GetCurrentPage",
    description="Method for retrieving a screenshot of the control system with the currently shown contents",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6209"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6210"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6211",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6212",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7009",
    browseName="ns=plastics_rubber;GetPage",
    description="Method for retrieving the image of a page of the control system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6211"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6212"]),
)

plastics_rubber.objtypes.MachineConfigurationType(
    nodeId="ns=plastics_lds;i=5009",
    browseName="ns=plastics_lds;MachineConfiguration",
    description="Information about the machine configuration",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6188",
                browseName="ns=plastics_rubber;LocationName",
                description="Description of the location of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6190",
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
                nodeId="ns=plastics_lds;i=6191",
                browseName="ns=plastics_rubber;UserMachineName",
                description="Description of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6213",
                browseName="ns=plastics_rubber;PageDirectory",
                description="List of the pages that are implemented in the machine control system and are shown on the screen of the machine",
                dataType=plastics_rubber.datatypes.PageEntryDataType,
                valueRank=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7007"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7008"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7009"]),
    ],
)
o6.reference(plastics_lds_objtypes.LDS_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5009"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_lds;i=5013",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6217",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6218",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6219",
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
                nodeId="ns=plastics_lds;i=7012",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7013", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5002",
    browseName="ns=plastics_lds;DeliveryPressure",
    description="With this Object the client can set (and monitor) the delivery pressure of the LDS.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6134",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5013"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6068"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6131"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6135"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6137"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6139"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6141"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6143"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6146"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6148"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6150"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6152"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6154"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6692"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7005",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5002"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6094",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CycleNumber", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7014",
    browseName="ns=plastics_lds;SetCycleNumber",
    description="Method to set the cycle number of the LDS to synchronize it with the cycle number of the injection moulding machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6094"]),
)

plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_lds;i=5016",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6316",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6317",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6318",
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
                nodeId="ns=plastics_lds;i=7015",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7016", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5001",
    browseName="ns=plastics_lds;AdditiveFraction",
    description="Contains the SetValue, ActualValue, LowerTolerance and UpperTolerance of the additive fraction in percent",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6019",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5016"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6001"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6011"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6016"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6020"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6022"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6024"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6026"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6028"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6031"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6033"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6035"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6037"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6092"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7001",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_lds_objtypes.AdditiveType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5001"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_lds;i=5018",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6354",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6355",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6356",
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
                nodeId="ns=plastics_lds;i=7018",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7019", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5007",
    browseName="ns=plastics_lds;AdditiveStrokeVolume",
    description="Defines the value of additive per shot/stroke",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6332",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5018"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6013"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6329"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6333"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6335"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6337"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6339"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6341"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6344"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6346"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6348"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6350"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6352"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6656"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7017",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_lds_objtypes.AdditiveType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5007"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_lds;i=5021",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6519",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6520",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6521",
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
                nodeId="ns=plastics_lds;i=7022",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7023", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5019",
    browseName="ns=plastics_lds;AdditiveFraction",
    description="Contains the SetValue, ActualValue, LowerTolerance and UpperTolerance of the additive fraction in percent",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6518",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5021"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6511"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6515"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6522"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6525"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6528"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6531"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6534"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6537"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6540"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6543"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6546"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6549"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6632"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7024",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_lds;i=5022",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6556",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6557",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6558",
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
                nodeId="ns=plastics_lds;i=7025",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7026", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5020",
    browseName="ns=plastics_lds;AdditiveStrokeVolume",
    description="Defines the value of additive per shot/stroke",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6555",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5022"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6513"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6552"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6559"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6562"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6565"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6568"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6571"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6574"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6577"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6580"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6583"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6586"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6668"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7027",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_lds_objtypes.AdditiveType(
    nodeId="ns=plastics_lds;i=5006",
    browseName="ns=plastics_lds;Additive_<Y>",
    description="Information about the additives",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6043",
                browseName="ns=plastics_lds;ActivateClosedLoopControl",
                description="Activate the closed loop control of the additive",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6088",
                browseName="ns=plastics_lds;ActivateAdditive",
                description="Set value to activate the additive",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6089",
                browseName="ns=plastics_lds;AdditiveActivated",
                description="Is true if the additive is activated.",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6090",
                browseName="ns=plastics_lds;Status",
                description="Actual status of the additive provides a minimal error handling for devices without event support.",
                dataType=plastics_lds_datypes.AdditiveStatusEnumeration,
                value=plastics_lds_datypes.AdditiveStatusEnumeration.GOOD,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6459",
                browseName="ns=plastics_lds;ClosedLoopControlActivated",
                description="Is true if the closed loop control of the additive is activated",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6637",
                browseName="ns=plastics_lds;IsPresent",
                description="Informs the client if the additive is physically present.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5019"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5020"]),
    ],
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5006"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6625",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Density", dataType=o6.Double, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7029",
    browseName="ns=plastics_lds;SetSetValueDensity",
    description="This optional method is used to modify SetValueDensity if allowed by the device.",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6625"]),
)

plastics_lds_objtypes.ComponentType(
    nodeId="ns=plastics_lds;i=5005",
    browseName="ns=plastics_lds;Component_A",
    description="Information about component A",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6100",
                browseName="ns=plastics_lds;Status",
                description="Actual status of the component provides a minimal error handling for devices without event support.",
                dataType=plastics_lds_datypes.ComponentStatusEnumeration,
                value=plastics_lds_datypes.ComponentStatusEnumeration.GOOD,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6591",
                browseName="ns=plastics_lds;AllowsCycles",
                description="Expected number of remaining cycles with the current drum",
                dataType=o6.Double,
                value=0.0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6364"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_lds;i=6621",
                browseName="ns=plastics_lds;RemainingMaterialTime",
                description="Time until the material of the component is empty",
                dataType=ns0.datatypes.Duration,
                value=0.0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6622"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6626"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6707"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6709"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6711"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7029"]),
    ],
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5005"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6425",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7030",
    browseName="ns=plastics_lds;ResetErrorById",
    description="Method to reset one error of the device",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6425"]),
)

plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_lds;i=5026",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6275",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6276",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6277",
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
                nodeId="ns=plastics_lds;i=7033",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7034", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5024",
    browseName="ns=plastics_lds;DeliveryPressure",
    description="With this Object the client can set (and monitor) the delivery pressure of the LDS.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6274",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5026"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6244"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6271"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6278"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6281"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6284"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6367"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6370"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6373"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6376"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6379"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6382"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6385"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6695"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7035",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_lds;i=5012",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6390",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6391",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6392",
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
                nodeId="ns=plastics_lds;i=7036",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7037", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5003",
    browseName="ns=plastics_lds;DeliveryFlowrate",
    description="Delivery volumetric flow rate",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6108",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5012"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6070"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6105"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6109"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6111"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6113"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6115"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6117"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6120"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6122"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6124"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6126"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6128"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6686"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7004",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5003"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_lds;i=5025",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6430",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6431",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6432",
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
                nodeId="ns=plastics_lds;i=7038",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7039", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_lds;i=5023",
    browseName="ns=plastics_lds;DeliveryFlowrate",
    description="Delivery volumetric flow rate",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6249",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5025"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6242"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6246"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6250"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6252"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6254"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6256"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6258"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6261"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6263"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6265"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6267"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6269"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6689"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7032",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6641",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Density", dataType=o6.Double, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7045",
    browseName="ns=plastics_lds;SetSetValueDensity",
    description="This optional method is used to modify SetValueDensity if allowed by the device.",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6641"]),
)

plastics_lds_objtypes.ComponentType(
    nodeId="ns=plastics_lds;i=5029",
    browseName="ns=plastics_lds;Component_A",
    description="Information about component A",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6193",
                browseName="ns=plastics_lds;Status",
                description="Actual status of the component provides a minimal error handling for devices without event support.",
                dataType=plastics_lds_datypes.ComponentStatusEnumeration,
                value=plastics_lds_datypes.ComponentStatusEnumeration.GOOD,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6630",
                browseName="ns=plastics_lds;AllowsCycles",
                description="Expected number of remaining cycles with the current drum",
                dataType=o6.Double,
                value=0.0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6628"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_lds;i=6633",
                browseName="ns=plastics_lds;RemainingMaterialTime",
                description="Time until the material of the component is empty",
                dataType=ns0.datatypes.Duration,
                value=0.0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6634"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6642"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6719"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6721"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6723"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7045"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6661",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Density", dataType=o6.Double, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7047",
    browseName="ns=plastics_lds;SetSetValueDensity",
    description="This optional method is used to modify SetValueDensity if allowed by the device.",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6661"]),
)

plastics_lds_objtypes.ComponentType(
    nodeId="ns=plastics_lds;i=5011",
    browseName="ns=plastics_lds;Component_B",
    description="Information about component B",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6102",
                browseName="ns=plastics_lds;Status",
                description="Actual status of the component provides a minimal error handling for devices without event support.",
                dataType=plastics_lds_datypes.ComponentStatusEnumeration,
                value=plastics_lds_datypes.ComponentStatusEnumeration.GOOD,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6654",
                browseName="ns=plastics_lds;AllowsCycles",
                description="Expected number of remaining cycles with the current drum",
                dataType=o6.Double,
                value=0.0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6652"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_lds;i=6657",
                browseName="ns=plastics_lds;RemainingMaterialTime",
                description="Time until the material of the component is empty",
                dataType=ns0.datatypes.Duration,
                value=0.0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6658"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6662"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6713"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6715"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6717"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7047"]),
    ],
)
o6.reference(plastics_lds_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5011"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6673",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Density", dataType=o6.Double, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7049",
    browseName="ns=plastics_lds;SetSetValueDensity",
    description="This optional method is used to modify SetValueDensity if allowed by the device.",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6673"]),
)

plastics_lds_objtypes.ComponentType(
    nodeId="ns=plastics_lds;i=5030",
    browseName="ns=plastics_lds;Component_B",
    description="Information about component B",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6363",
                browseName="ns=plastics_lds;Status",
                description="Actual status of the component provides a minimal error handling for devices without event support.",
                dataType=plastics_lds_datypes.ComponentStatusEnumeration,
                value=plastics_lds_datypes.ComponentStatusEnumeration.GOOD,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6666",
                browseName="ns=plastics_lds;AllowsCycles",
                description="Expected number of remaining cycles with the current drum",
                dataType=o6.Double,
                value=0.0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6664"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_lds;i=6669",
                browseName="ns=plastics_lds;RemainingMaterialTime",
                description="Time until the material of the component is empty",
                dataType=ns0.datatypes.Duration,
                value=0.0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6670"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6674"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6725"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6727"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6729"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7049"]),
    ],
)
plastics_lds_objtypes.OperationType(
    nodeId="ns=plastics_lds;i=5010",
    browseName="ns=plastics_lds;Operation",
    description="This Object contains components which are necessary to operate the LDS",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6197",
                browseName="ns=plastics_lds;DeviceMappingNumber",
                description="Unique identifier/address/number for devices of the same DeviceType within a local network",
                dataType=o6.UInt32,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6199",
                browseName="ns=plastics_lds;MaterialBalanceSystemType",
                description="Type of the material balance system",
                dataType=plastics_lds_datypes.MaterialBalanceSystemTypeEnumeration,
                value=plastics_lds_datypes.MaterialBalanceSystemTypeEnumeration.NOT_AVAILABLE,
            )
        ),
        o6.hasProperty(o6.ns["ns=plastics_lds;i=6214"]),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6315",
                browseName="ns=plastics_lds;HighestActiveAlarmSeverity",
                description="Indication of the severity of the highest active alarm",
                dataType=o6.UInt16,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_lds;i=6420",
                browseName="ns=plastics_lds;PurgeStatus",
                description="Actual status of the purge function",
                dataType=plastics_lds_datypes.PurgeStatusEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5015"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5023"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5024"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5029"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=5030"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6096"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6157"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6160"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6176"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6179"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6194"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_lds;i=6207", browseName="ns=plastics_lds;DosingActive", dataType=o6.Boolean)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_lds;i=6208",
                browseName="ns=plastics_lds;PurgeCyclicActive",
                description="Difference between purging (true) and waiting (false)",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6215"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6221"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_lds;i=6224",
                browseName="ns=plastics_lds;PurgeCyclicIdleTime",
                description="Time until the next purge cycle starts",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6225"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6227"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6230"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6232"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6286"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_lds;i=6288",
                browseName="ns=plastics_lds;PurgeTimeout",
                description="Maximum time of the active PurgeMode",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6423"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=6426"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_lds;i=6507",
                browseName="ns=plastics_lds;ActiveErrors",
                description="List of the active errors of the device",
                dataType=plastics_rubber.datatypes.ClassifiedActiveErrorDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7011",
                browseName="ns=plastics_lds;IdentifyDevice",
                description="The peripheral device on which this method is called shows itself by e.g. activation of a LED.",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7014"]),
        o6.hasComponent(o6.ns["ns=plastics_lds;i=7030"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7031", browseName="ns=plastics_lds;ResetAllErrors", description="Method to reset all errors of the device")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_lds;i=7040",
                browseName="ns=plastics_lds;StartDosing",
                description="If RemoteControlActivated = 2, this Method (without arguments) is used to start the dosing",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7041", browseName="ns=plastics_lds;StopDosing")),
    ],
)
o6.reference(plastics_lds_objtypes.LDS_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_lds;i=5010"])
o6.reference(o6.ns["ns=plastics_lds;i=5010"], "i=41", plastics_lds_objtypes.LDSCycleParametersEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_lds_datypes, plastics_lds_objtypes
