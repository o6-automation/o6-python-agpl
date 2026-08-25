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

"""Generated OPC UA wmtp namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.machinery as machinery
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import datatypes as wmtp_datypes
from . import vartypes as wmtp_vartypes
from . import objtypes as wmtp_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=wmtp;i=5020", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wmtp;i=5021", browseName="Default XML")
o6.hasEncoding(wmtp_datypes.WMTPOutputDataType, o6.ns["ns=wmtp;i=5021"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wmtp;i=5022", browseName="Default JSON")
o6.hasEncoding(wmtp_datypes.WMTPOutputDataType, o6.ns["ns=wmtp;i=5022"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=wmtp;i=6001",
    browseName="ns=machinery;LifetimeVariable",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6002", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6003", browseName="ns=di;LimitValue", description="LimitValue indicates when the end of lifetime has been reached.", dataType=ns0.datatypes.Number
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6004",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=wmtp;i=5009",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6006",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6007",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=wmtp;i=5008"], "i=17604", o6.ns["ns=wmtp;i=5009"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6008",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6009", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6010", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=wmtp;i=5010",
    browseName="ns=wmtp;BatteryLevel",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6011", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6008"]),
    ],
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=wmtp;i=6016",
    browseName="ns=wmtp;LicenseValidity",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6017", browseName="ns=di;LimitValue", description="LimitValue indicates when the end of lifetime has been reached.", dataType=ns0.datatypes.Number
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6018",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6019", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=wmtp;i=6020",
    browseName="ns=wmtp;RemainingLifetimeCounter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6021", browseName="ns=di;LimitValue", description="LimitValue indicates when the end of lifetime has been reached.", dataType=ns0.datatypes.Number
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6022",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6023", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=wmtp;i=6024",
    browseName="ns=wmtp;RemainingCycleCounter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6025", browseName="ns=di;LimitValue", description="LimitValue indicates when the end of lifetime has been reached.", dataType=ns0.datatypes.Number
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6026",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6027", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=wmtp;i=6028",
    browseName="ns=wmtp;NextServiceCounter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6029", browseName="ns=di;LimitValue", description="LimitValue indicates when the end of lifetime has been reached.", dataType=ns0.datatypes.Number
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6030",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6031", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machinery.objtypes.MachineryLifetimeCounterType(
    nodeId="ns=wmtp;i=5005",
    browseName="ns=machinery;LifetimeCounters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=wmtp;i=6001"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6016"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6020"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6024"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6028"]),
    ],
)
o6.reference(wmtp_objtypes.WirelessMachineToolPeripheralType, ns0.reftypes.HasAddIn, o6.ns["ns=wmtp;i=5005"])
o6.reference(o6.ns["ns=wmtp;i=5008"], "i=17604", o6.ns["ns=wmtp;i=5005"])
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=wmtp;i=5006",
    browseName="ns=machinery;OperationCounters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=wmtp;i=6032", browseName="ns=wmtp;OperationSinceLastServiceCounter", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1
            )
        )
    ],
)
o6.reference(wmtp_objtypes.WirelessMachineToolPeripheralType, ns0.reftypes.HasAddIn, o6.ns["ns=wmtp;i=5006"])
o6.reference(o6.ns["ns=wmtp;i=5008"], "i=17604", o6.ns["ns=wmtp;i=5006"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6033",
    browseName="ns=wmtp;TriggerSettings",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6034", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(wmtp_objtypes.WMTPMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=6033"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6035",
    browseName="ns=wmtp;DeltaCondition",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6036", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(wmtp_objtypes.WMTPMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=6035"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6037",
    browseName="ns=wmtp;TypeOfMeasurement",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6038",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6039", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(wmtp_objtypes.WMTPMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=6037"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6040",
    browseName="ns=wmtp;TypeOfSample",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6041",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6042", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(wmtp_objtypes.WMTPMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=6040"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6043",
    browseName="ns=wmtp;RelativeUncertainty",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6044", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(wmtp_objtypes.WMTPMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=6043"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6045",
    browseName="ns=wmtp;AbsoluteUncertainty",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6046", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(wmtp_objtypes.WMTPMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=6045"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6051",
    browseName="ns=wmtp;DeltaCondition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6052", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6053",
    browseName="ns=wmtp;TriggerSettings",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6054", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6055",
    browseName="ns=wmtp;TypeOfMeasurement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6056",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6057", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6058",
    browseName="ns=wmtp;TypeOfSample",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6059",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6060", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6061",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6062", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6063", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6065",
    browseName="ns=wmtp;DeltaCondition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6066", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6067",
    browseName="ns=wmtp;TriggerSettings",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6068", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6069",
    browseName="ns=wmtp;TypeOfMeasurement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6070",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6071", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6072",
    browseName="ns=wmtp;TypeOfSample",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6073",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6074", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6075",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6076", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6077", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6079",
    browseName="ns=wmtp;DeltaCondition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6080", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6081",
    browseName="ns=wmtp;TriggerSettings",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6082", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6083",
    browseName="ns=wmtp;TypeOfMeasurement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6084",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6085", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6086",
    browseName="ns=wmtp;TypeOfSample",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6087",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6088", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6089",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6090", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6091", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6093",
    browseName="ns=wmtp;DeltaCondition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6094", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6095",
    browseName="ns=wmtp;TriggerSettings",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6096", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6097",
    browseName="ns=wmtp;TypeOfMeasurement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6098",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6099", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6100",
    browseName="ns=wmtp;TypeOfSample",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6101",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6102", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6103",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6104", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6105", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6107",
    browseName="ns=wmtp;DeltaCondition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6108", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6109",
    browseName="ns=wmtp;TriggerSettings",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6110", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6111",
    browseName="ns=wmtp;TypeOfMeasurement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6112",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6113", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6114",
    browseName="ns=wmtp;TypeOfSample",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6115",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6116", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6117",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6118", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6119", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6121",
    browseName="ns=wmtp;DeltaCondition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6122", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6123",
    browseName="ns=wmtp;TriggerSettings",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6124", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6125",
    browseName="ns=wmtp;TypeOfMeasurement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6126",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6127", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6128",
    browseName="ns=wmtp;TypeOfSample",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6129",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6130", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6131",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6132", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6133", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6135",
    browseName="ns=wmtp;DeltaCondition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6136", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6137",
    browseName="ns=wmtp;TriggerSettings",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6138", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6139",
    browseName="ns=wmtp;TypeOfMeasurement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6140",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6141", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6142",
    browseName="ns=wmtp;TypeOfSample",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6143",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6144", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6145",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6146", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6147", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6149",
    browseName="ns=wmtp;DeltaCondition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6150", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=wmtp;i=6151",
    browseName="ns=wmtp;TriggerSettings",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6152", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6153",
    browseName="ns=wmtp;TypeOfMeasurement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6154",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("temperature")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("rotation speed")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("humidity")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("acceleration")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("force")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("torque")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("position")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("dimension")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6155", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6156",
    browseName="ns=wmtp;TypeOfSample",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6157",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("unspecified")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("instantaneous")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("arithmetic mean since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("root mean square (RMS) value since the beginning of the work cycle")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("maximum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("minimum value in the current work cycle")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("moving average")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6158", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=wmtp;i=6159",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6160", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6161", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6220",
    browseName="ns=machinery_processvalues;Status",
    description="Indicates if a limit has been reached.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6221", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6222", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(wmtp_objtypes.WMTPMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=6220"])
ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6223", browseName="ns=wmtp;OperationAboveHigh", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=wmtp;i=6220"], "i=46", o6.ns["ns=wmtp;i=6223"])
ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6224", browseName="ns=wmtp;OperationAboveHighHigh", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=wmtp;i=6220"], "i=46", o6.ns["ns=wmtp;i=6224"])
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=wmtp;i=5019",
    browseName="ns=wmtp;LimitCounters",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=wmtp;i=6223"]), o6.hasProperty(o6.ns["ns=wmtp;i=6224"])],
)
o6.reference(wmtp_objtypes.WMTPMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=5019"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wmtp;i=6229", browseName="ns=wmtp;WMTPOutputDataType", dataType=o6.String, value="WMTPOutputDataType")
o6.reference(o6.ns["ns=wmtp;i=5020"], "i=39", o6.ns["ns=wmtp;i=6229"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wmtp;i=6230", browseName="ns=wmtp;WMTPOutputDataType", dataType=o6.String, value="//xs:element[@name='WMTPOutputDataType']")
o6.reference(o6.ns["ns=wmtp;i=5021"], "i=39", o6.ns["ns=wmtp;i=6230"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=wmtp;i=6015",
    browseName="ns=wmtp;LifeCycleStatus",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6249",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("green")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("yellow")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("red")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6250", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=wmtp;i=5002",
    browseName="ns=wmtp;DeviceInformation",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6012", browseName="ns=wmtp;LicenseInformation", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6013", browseName="ns=wmtp;NextServiceDate", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6014", browseName="ns=wmtp;LastService", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=wmtp;i=5010"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6015"]),
        o6.hasAddIn(o6.ns["ns=wmtp;i=5009"]),
    ],
)
o6.reference(wmtp_objtypes.WirelessMachineToolPeripheralType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=5002"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashWMTPSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=wmtp;i=5023",
    browseName="ns=wmtp;http://opcfoundation.org/UA/WMTP/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6251", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6252", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-11-01T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6253", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WMTP/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6254", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6255", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6256", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6257", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6258", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6259", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6260", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=wmtp;i=6225",
    browseName="ns=wmtp;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/WMTP/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6226", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WMTP/")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6275",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6229"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ua="http://opcfoundation.org/UA/" xmlns:tns="http://opcfoundation.org/UA/WMTP/" TargetNamespace="http://opcfoundation.org/UA/WMTP/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="WMTPOutputDataType">\n  <opc:Field Name="EngineeringUnits" TypeName="ua:EUInformation"/>\n  <opc:Field Name="ActualValue" TypeName="opc:Double"/>\n  <opc:Field Name="TypeOfMeasurement" TypeName="opc:UInt32"/>\n  <opc:Field Name="TypeOfSample" TypeName="opc:UInt32"/>\n  <opc:Field Name="InstrumentRange" TypeName="ua:Range"/>\n  <opc:Field Name="EURange" TypeName="ua:Range"/>\n  <opc:Field Name="ValuePrecision" TypeName="opc:Double"/>\n  <opc:Field Name="Definition" TypeName="opc:CharArray"/>\n  <opc:Field Name="SignalTag" TypeName="opc:CharArray"/>\n  <opc:Field Name="RelativeUncertainty" TypeName="opc:Double"/>\n  <opc:Field Name="AbsoluteUncertainty" TypeName="opc:Double"/>\n  <opc:Field Name="Timestamp" TypeName="opc:DateTime"/>\n  <opc:Field Name="Index" TypeName="opc:UInt32"/>\n  <opc:Field Name="MeasurementPeriod" TypeName="opc:Double"/>\n  <opc:Field Name="InternalUpdateInterval" TypeName="opc:Double"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=wmtp;i=6227",
    browseName="ns=wmtp;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/WMTP/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6228", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WMTP/Types.xsd")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wmtp;i=6276",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6230"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://opcfoundation.org/UA/WMTP/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/WMTP/Types.xsd">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:complexType name="WMTPOutputDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="EngineeringUnits" type="ua:EUInformation" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ActualValue" type="xs:double" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="TypeOfMeasurement" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="TypeOfSample" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="InstrumentRange" type="ua:Range" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="EURange" type="ua:Range" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ValuePrecision" type="xs:double" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Definition" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SignalTag" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="RelativeUncertainty" type="xs:double" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AbsoluteUncertainty" type="xs:double" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Timestamp" type="xs:dateTime" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Index" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="MeasurementPeriod" type="xs:double" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="InternalUpdateInterval" type="xs:double" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="WMTPOutputDataType" type="tns:WMTPOutputDataType"/>\n <xs:complexType name="ListOfWMTPOutputDataType">\n  <xs:sequence>\n   <xs:element nillable="true" maxOccurs="unbounded" name="WMTPOutputDataType" type="tns:WMTPOutputDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" name="ListOfWMTPOutputDataType" type="tns:ListOfWMTPOutputDataType"/>\n</xs:schema>\n',
)


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6163",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DateTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="TimeZoneOffset", dataType=ns0.datatypes.TimeZoneDataType, valueRank=-1),
    ],
)
o6.call(nodeId="ns=wmtp;i=7001", browseName="ns=wmtp;SetDeviceTime", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6163"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6218",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirmwareData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=wmtp;i=7002", browseName="ns=wmtp;UpdateFirmware", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6218"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6219",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LicenseData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=wmtp;i=7003", browseName="ns=wmtp;SendLicenseData", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6219"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6231",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TargetMode", dataType=o6.UInt16, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7004", browseName="ns=wmtp;SwitchCalibrationMode", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6231"]))

ns0.objtypes.FolderType(
    nodeId="ns=wmtp;i=5001",
    browseName="ns=wmtp;DeviceConfiguration",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6005", browseName="ns=wmtp;CalibrationMode", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=wmtp;i=7001"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7002"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7003"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7004"]),
    ],
)
o6.reference(wmtp_objtypes.WirelessMachineToolPeripheralType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=5001"])


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6242",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=wmtp;i=7024", browseName="ns=wmtp;CombinedReportAll", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6242"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6175",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfStoredRecords", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7025", browseName="ns=wmtp;ReportNumberOfStoredRecords", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6175"]))

wmtp_objtypes.WMTPServiceCycleDataType(
    nodeId="ns=wmtp;i=5004",
    browseName="ns=wmtp;WMTPServiceCycleData",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.call(nodeId="ns=wmtp;i=7023", browseName="ns=wmtp;AbortOperation")),
        o6.hasComponent(o6.ns["ns=wmtp;i=7024"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7025"]),
    ],
)
o6.reference(wmtp_objtypes.WirelessMachineToolPeripheralType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=5004"])


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6234",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=-2)],
)
o6.call(nodeId="ns=wmtp;i=7027", browseName="ns=wmtp;CombinedReportAll", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6234"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6177",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfStoredRecords", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7028", browseName="ns=wmtp;ReportNumberOfStoredRecords", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6177"]))

wmtp_objtypes.WMTPWorkCycleDataType(
    nodeId="ns=wmtp;i=5003",
    browseName="ns=wmtp;WMTPWorkCycleData",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.call(nodeId="ns=wmtp;i=7026", browseName="ns=wmtp;AbortOperation")),
        o6.hasComponent(o6.ns["ns=wmtp;i=7027"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7028"]),
    ],
)
o6.reference(wmtp_objtypes.WirelessMachineToolPeripheralType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=5003"])


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6204",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7031", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6204"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6186",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7032", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6186"]))

wmtp_objtypes.WMTPMeasurementType(
    nodeId="ns=wmtp;i=5014",
    browseName="ns=wmtp;<Acceleration>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6064", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6051"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6055"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6058"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6061"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6095"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7031"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7032"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6208",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7033", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6208"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6190",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7034", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6190"]))

wmtp_objtypes.WMTPMeasurementType(
    nodeId="ns=wmtp;i=5018",
    browseName="ns=wmtp;<Dimension>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6078", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6065"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6069"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6072"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6075"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6151"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7033"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7034"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6205",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7035", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6205"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6187",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7036", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6187"]))

wmtp_objtypes.WMTPMeasurementType(
    nodeId="ns=wmtp;i=5015",
    browseName="ns=wmtp;<Force>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6092", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6079"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6083"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6086"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6089"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6109"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7035"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7036"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6203",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7037", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6203"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6185",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7038", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6185"]))

wmtp_objtypes.WMTPMeasurementType(
    nodeId="ns=wmtp;i=5013",
    browseName="ns=wmtp;<Humidity>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6106", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6081"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6093"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6097"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6100"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6103"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7037"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7038"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6207",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7039", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6207"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6189",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7040", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6189"]))

wmtp_objtypes.WMTPMeasurementType(
    nodeId="ns=wmtp;i=5017",
    browseName="ns=wmtp;<Position>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6120", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6107"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6111"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6114"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6117"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6137"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7039"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7040"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6202",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7041", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6202"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6184",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7042", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6184"]))

wmtp_objtypes.WMTPMeasurementType(
    nodeId="ns=wmtp;i=5012",
    browseName="ns=wmtp;<RotationSpeed>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6134", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6067"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6121"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6125"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6128"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6131"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7041"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7042"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6201",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7043", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6201"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6183",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7044", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6183"]))

wmtp_objtypes.WMTPMeasurementType(
    nodeId="ns=wmtp;i=5011",
    browseName="ns=wmtp;<Temperature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6148", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6053"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6135"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6139"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6142"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6145"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7043"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7044"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6206",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7045", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6206"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6188",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7046", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6188"]))

wmtp_objtypes.WMTPMeasurementType(
    nodeId="ns=wmtp;i=5016",
    browseName="ns=wmtp;<Torque>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6162", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=wmtp;i=6123"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6149"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6153"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6156"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=6159"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7045"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=7046"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=wmtp;i=5007",
    browseName="ns=wmtp;Measurements",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=wmtp;i=5011"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=5012"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=5013"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=5014"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=5015"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=5016"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=5017"]),
        o6.hasComponent(o6.ns["ns=wmtp;i=5018"]),
    ],
)
o6.reference(wmtp_objtypes.WirelessMachineToolPeripheralType, ns0.reftypes.HasComponent, o6.ns["ns=wmtp;i=5007"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, machinery, machinery_processvalues, ns0, padim, wmtp_datypes, wmtp_vartypes, wmtp_objtypes
