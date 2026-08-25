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

"""Generated OPC UA powertrain namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_ac as fx_ac
import o6.ns.fx_data as fx_data
import o6.ns.ia as ia
import o6.ns.irdi_v1_0_0 as irdi_v1_0_0
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import reftypes as powertrain_reftypes
from . import objtypes as powertrain_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

powertrain_objtypes.PtEncoderInterfaceAttributesType(
    nodeId="ns=powertrain;i=5070",
    browseName="ns=powertrain;PtEncoderInterfaceAttributes",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            powertrain_objtypes.PtEncoderInterfaceProtocolAttributesType(
                nodeId="ns=powertrain;i=5071",
                browseName="ns=powertrain;PtEncoderInterfaceProtocolAttributes",
                displayName="PtEncoderInterfaceProtocolsAttributes",
                modellingRule="MandatoryPlaceholder",
            )
        )
    ],
)
o6.reference(powertrain_objtypes.PtAssetEncoderType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5070"])
powertrain_objtypes.PtEncoderInterfaceAttributesType(
    nodeId="ns=powertrain;i=5072",
    browseName="ns=powertrain;<PtEncoderInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            powertrain_objtypes.PtEncoderInterfaceProtocolAttributesType(
                nodeId="ns=powertrain;i=5073",
                browseName="ns=powertrain;PtEncoderInterfaceProtocolAttributes",
                displayName="PtEncoderInterfaceProtocolsAttributes",
                modellingRule="MandatoryPlaceholder",
            )
        )
    ],
)
o6.reference(powertrain_objtypes.PtAssetOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5072"])
powertrain_objtypes.PtEncoderInterfaceAttributesType(
    nodeId="ns=powertrain;i=5074",
    browseName="ns=powertrain;<PtEncoderInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            powertrain_objtypes.PtEncoderInterfaceProtocolAttributesType(
                nodeId="ns=powertrain;i=5075",
                browseName="ns=powertrain;PtEncoderInterfaceProtocolAttributes",
                displayName="PtEncoderInterfaceProtocolsAttributes",
                modellingRule="MandatoryPlaceholder",
            )
        )
    ],
)
o6.reference(powertrain_objtypes.PtAssetControlModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5074"])
powertrain_objtypes.PtEncoderInterfaceAttributesType(
    nodeId="ns=powertrain;i=5076",
    browseName="ns=powertrain;<PtEncoderInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            powertrain_objtypes.PtEncoderInterfaceProtocolAttributesType(
                nodeId="ns=powertrain;i=5077",
                browseName="ns=powertrain;PtEncoderInterfaceProtocolAttributes",
                displayName="PtEncoderInterfaceProtocolsAttributes",
                modellingRule="MandatoryPlaceholder",
            )
        )
    ],
)
o6.reference(powertrain_objtypes.PtAssetIoModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5076"])
powertrain_objtypes.PtEncoderInterfaceAttributesType(
    nodeId="ns=powertrain;i=5078",
    browseName="ns=powertrain;<PtEncoderInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            powertrain_objtypes.PtEncoderInterfaceProtocolAttributesType(
                nodeId="ns=powertrain;i=5079",
                browseName="ns=powertrain;PtEncoderInterfaceProtocolAttributes",
                displayName="PtEncoderInterfaceProtocolsAttributes",
                modellingRule="MandatoryPlaceholder",
            )
        )
    ],
)
o6.reference(powertrain_objtypes.PtAssetSafetyModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5078"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6003",
    browseName="ns=powertrain;PwmSwitchingFrequency",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6004", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtOutputConverterAttributesType(
    nodeId="ns=powertrain;i=5002",
    browseName="ns=powertrain;<PtOutputConverterAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6003"])],
)
o6.reference(powertrain_objtypes.PtAssetDriveIntegratedMotorRotaryType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5002"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6005",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5053", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6005"])]
)
o6.reference(powertrain_objtypes.PtAssetDriveIntegratedMotorRotaryType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5053"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=powertrain;i=5001",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6001",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6002",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6007",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6008",
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
                nodeId="ns=powertrain;i=6009",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6010",
                browseName="ns=di;DeviceRevision",
                description="A string representation of the overall revision level of the component. Often, it is increased when either the SoftwareRevision and / or the HardwareRevision of the component is increased. As an example, it can be used in ERP systems together with the ProductCode.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6011",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6012",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6013",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6014",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6015",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6016",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6017",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6018",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6019",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
    ],
)
o6.reference(powertrain_objtypes.PtAssetType, ns0.reftypes.HasAddIn, o6.ns["ns=powertrain;i=5001"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6035",
    browseName="ns=powertrain;InputConverterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6036", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6037", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtInputConverterAttributesType(
    nodeId="ns=powertrain;i=5059", browseName="ns=powertrain;PtInputConverterAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6035"])]
)
o6.reference(powertrain_objtypes.PtAssetDriveIntegratedMotorRotaryType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5059"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6038",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6039", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6040", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5060",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6038"])],
)
o6.reference(powertrain_objtypes.PtAssetDriveIntegratedMotorRotaryType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5060"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6041",
    browseName="ns=powertrain;PwmSwitchingFrequency",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6042", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtOutputConverterAttributesType(
    nodeId="ns=powertrain;i=5061",
    browseName="ns=powertrain;<PtOutputConverterAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6041"])],
)
o6.reference(powertrain_objtypes.PtAssetDriveIntegratedMotorLinearType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5061"])
powertrain_objtypes.PtStandardAttributesType(
    nodeId="ns=powertrain;i=5008",
    browseName="ns=powertrain;<PtStandardAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6054", browseName="ns=powertrain;DefaultInstanceBrowsename", dataType=o6.QualifiedName, value=o6.QualifiedName("powertrain:")
            )
        )
    ],
)
o6.reference(powertrain_objtypes.PtAssetType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=5008"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPowertrainSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=powertrain;i=5019",
    browseName="ns=powertrain;http://opcfoundation.org/UA/Powertrain/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6065", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6066", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-11-01T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6067", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Powertrain/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6068", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6069", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6070", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6071", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6075",
    browseName="ns=powertrain;BrakeInertia",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6076", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6078",
    browseName="ns=powertrain;BrakeTurnOffDelayAC",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6079", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6080",
    browseName="ns=powertrain;BrakeTurnOffDelayDC",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6083",
    browseName="ns=powertrain;BrakeTurnOnDelay",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6084", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6086",
    browseName="ns=powertrain;BrakeVoltageRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6087", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6086"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6090",
    browseName="ns=powertrain;BrakingEnergySingleEngagementMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6091", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6094",
    browseName="ns=powertrain;<ResistanceValue>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6095", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBleedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6094"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6096",
    browseName="ns=powertrain;PowerRated",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6097", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBleedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6096"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6099",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6100", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5063", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6099"])]
)
o6.reference(powertrain_objtypes.PtAssetDriveIntegratedMotorLinearType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5063"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6102",
    browseName="ns=powertrain;FrequencyRange",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6103", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6102"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6106",
    browseName="ns=powertrain;PowerRated",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6107", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtBleedAttributesType(
    nodeId="ns=powertrain;i=5021", browseName="ns=powertrain;PtBleedAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6106"])]
)
o6.reference(powertrain_objtypes.PtAssetElectricalBrakingModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5021"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6108",
    browseName="ns=powertrain;PowerRated",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6109", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtBleedAttributesType(
    nodeId="ns=powertrain;i=5082", browseName="ns=powertrain;PtBleedAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6108"])]
)
o6.reference(powertrain_objtypes.PtAssetInputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5082"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6114",
    browseName="ns=powertrain;TemperatureMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6115", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6116",
    browseName="ns=powertrain;TemperatureMin",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6117", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6119",
    browseName="ns=powertrain;MeasuringRange",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6120", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6119"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6121",
    browseName="ns=powertrain;OperatingVoltage",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6122", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6121"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6123",
    browseName="ns=powertrain;FrequencyRange",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6124", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6128",
    browseName="ns=powertrain;BrakeInertia",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6131",
    browseName="ns=powertrain;BrakeTurnOffDelayAC",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6132", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6133",
    browseName="ns=powertrain;BrakeTurnOffDelayDC",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6134", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6082",
    browseName="ns=powertrain;BrakeTurnOffType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6098",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("AC"), description=o6.LocalizedText("AC-operated brake")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DC"), description=o6.LocalizedText("DC-operated brake")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("AC_DC"), description=o6.LocalizedText("AC- and DC-operated brake")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6135", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6082"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6136",
    browseName="ns=powertrain;BrakeTurnOnDelay",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6137", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6085",
    browseName="ns=powertrain;BrakeType",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6101",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("STOPPING"), description=o6.LocalizedText("Stopping brake type")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("HOLDING"), description=o6.LocalizedText("Holding brake type")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6138", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6085"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6139",
    browseName="ns=powertrain;MeasuringRange",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6140", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6143",
    browseName="ns=powertrain;BrakingEnergySingleEngagementMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6104",
    browseName="ns=powertrain;InputConverterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6105", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6146", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtInputConverterAttributesType(
    nodeId="ns=powertrain;i=5093", browseName="ns=powertrain;PtInputConverterAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6104"])]
)
o6.reference(powertrain_objtypes.PtAssetDriveIntegratedMotorLinearType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5093"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6151",
    browseName="ns=powertrain;<PwmSwitchingFrequency>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6152", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputConverterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6151"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6147",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6153", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6154", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5094",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6147"])],
)
o6.reference(powertrain_objtypes.PtAssetDriveIntegratedMotorLinearType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5094"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6158",
    browseName="ns=powertrain;PowerRated",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6159", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtBleedAttributesType(
    nodeId="ns=powertrain;i=5103", browseName="ns=powertrain;PtBleedAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6158"])]
)
o6.reference(powertrain_objtypes.PtAssetBleedType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5103"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6160",
    browseName="ns=powertrain;InputConverterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6161", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6162", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtInputConverterAttributesType(
    nodeId="ns=powertrain;i=5104", browseName="ns=powertrain;PtInputConverterAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6160"])]
)
o6.reference(powertrain_objtypes.PtAssetInputOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5104"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6164",
    browseName="ns=powertrain;MotorEfficiencyClass",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6165",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("IE1"), description=o6.LocalizedText("Standard Efficiency")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("IE2"), description=o6.LocalizedText("High Efficiency")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("IE3"), description=o6.LocalizedText("Premium Efficiency")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("IE4"), description=o6.LocalizedText("Super Premium Efficiency")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("IE5"), description=o6.LocalizedText("Ultra Premium Efficiency")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("IES0"), description=o6.LocalizedText("Relative losses are higher than 20 % of the value defined by the RPDS")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=6, displayName=o6.LocalizedText("IES1"), description=o6.LocalizedText("Relative losses are within &#177;20 % of the value defined by the RPDS")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7, displayName=o6.LocalizedText("IES2"), description=o6.LocalizedText("Relative losses are smaller than 20 % of the value defined by the RPDS")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6166", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtMotorRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6164"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6125",
    browseName="ns=powertrain;GearType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6149",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("PLANETARY_GEAR"), description=o6.LocalizedText("Gearbox with planetary gears")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("WORM_GEAR"), description=o6.LocalizedText("Gearbox with worm gear")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SPUR_GEAR"), description=o6.LocalizedText("Gearbox with spur gears")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("HARMONIC_DRIVE_GEAR"), description=o6.LocalizedText("Gearbox with harmonic drive gears")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("SYNCHRONOUS_BELT"), description=o6.LocalizedText("Gearbox with synchronous belt")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("V_BELT"), description=o6.LocalizedText("Gearbox with V-belt")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("RACK_AND_PINION"), description=o6.LocalizedText("Gearbox with rack and pinion")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("SPINDLE_BALLSCREW"), description=o6.LocalizedText("Gearbox with spindle and ball screw")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("SPINDLE_THREAD"), description=o6.LocalizedText("Gearbox with spindle and thread")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6167", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6125"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6110",
    browseName="ns=powertrain;MotorType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6111",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ASYNCHRONOUS"), description=o6.LocalizedText("Asynchronous motor")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("PM_AC_SYNCHRONOUS"), description=o6.LocalizedText("Permanent magnet synchronous motor")),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("PM_AC_SYNCHRONOUS_IRONLESS"), description=o6.LocalizedText("Permanent magnet synchronous motor ironless")
                    ),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("DC_BRUSHLESS"), description=o6.LocalizedText("Brushless DC motor")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("DC_BRUSHED"), description=o6.LocalizedText("Brushed DC motor")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("PM_STEPPER"), description=o6.LocalizedText("Permanent magnet stepper motor")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("HYBRID_STEPPER"), description=o6.LocalizedText("Hybrid stepper motor")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("SYNC_RELUCTANCE"), description=o6.LocalizedText("Synchronous reluctance motor")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6168", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtMotorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6110"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6112",
    browseName="ns=powertrain;TemperatureSensorTechnology",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6113",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("THERMOCOUPLE"), description=o6.LocalizedText("Thermocouple")),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("TEMPERATURE_DEPENDENT_RESITANCE"), description=o6.LocalizedText("Temperature dependent resistance")
                    ),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("KTY"), description=o6.LocalizedText("Semiconductor temperature tensor")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6169", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtTemperatureSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6112"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6171",
    browseName="ns=powertrain;TemperatureMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6172", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6173",
    browseName="ns=powertrain;TemperatureMin",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6174", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6176",
    browseName="ns=powertrain;FrequencyRange",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6177", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6178",
    browseName="ns=powertrain;MeasuringRange",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6179", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6180",
    browseName="ns=powertrain;FrequencyRange",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6181", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6170",
    browseName="ns=powertrain;TemperatureSensorTechnology",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6182", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6183", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6184",
    browseName="ns=powertrain;TemperatureMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6185", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6186",
    browseName="ns=powertrain;TemperatureMin",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6187", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6189",
    browseName="ns=powertrain;MeasuringRange",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6190", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6191",
    browseName="ns=powertrain;PreChargeType",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6192",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("AC/DC"), description=o6.LocalizedText("AC input, DC output")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DC/DC"), description=o6.LocalizedText("DC input, DC output")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6193", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtPrechargeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6191"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6194",
    browseName="ns=powertrain;PreChargeTime",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6195", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtPrechargeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6194"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6196",
    browseName="ns=powertrain;PreChargeTimeout",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6197", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtPrechargeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6196"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6050",
    browseName="ns=powertrain;MotorPowerRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6199", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6050"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6052",
    browseName="ns=powertrain;MotorWindingType",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6200",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("IE1"), description=o6.LocalizedText("Standard Efficiency")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("IE2"), description=o6.LocalizedText("High Efficiency")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("IE3"), description=o6.LocalizedText("Premium Efficiency")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("IE4"), description=o6.LocalizedText("Super Premium Efficiency")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("IE5"), description=o6.LocalizedText("Ultra Premium Efficiency")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("IES0"), description=o6.LocalizedText("Relative losses are higher than 20 % of the value defined by the RPDS")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=6, displayName=o6.LocalizedText("IES1"), description=o6.LocalizedText("Relative losses are within &#177;20 % of the value defined by the RPDS")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7, displayName=o6.LocalizedText("IES2"), description=o6.LocalizedText("Relative losses are smaller than 20 % of the value defined by the RPDS")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6201", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtMotorRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6052"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6204",
    browseName="ns=powertrain;<DcBusVoltageRated>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6205", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtDcBusAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6204"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6207",
    browseName="ns=powertrain;<DcBusVoltageRated>",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6210",
    browseName="ns=powertrain;Capacitance",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtCapacitanceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6210"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6233",
    browseName="ns=powertrain;<DcBusVoltageRated>",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6234", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtSoftStarterAttributesType(
    nodeId="ns=powertrain;i=5033",
    browseName="ns=powertrain;PtSoftStarterAttributes",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6214", browseName="ns=powertrain;IntegratedByPassSupported", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6215", browseName="ns=powertrain;MotorOverloadProtectionIntegrated", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6216", browseName="ns=powertrain;OperationalCurrent40CRated", dataType=o6.Float)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6238", browseName="ns=powertrain;OperationalVoltageRangeRated", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
    ],
)
o6.reference(powertrain_objtypes.PtAssetSoftStarterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5033"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6245",
    browseName="ns=powertrain;Inductance",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6246", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(powertrain_objtypes.PtReactorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6245"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6155",
    browseName="ns=powertrain;LineFilterEmcCategory",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6224",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Other")),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("CATEGORY_C1"),
                        description=o6.LocalizedText(
                            "Installed in an equipment of rated voltage less than 1000 V, intended for use in residential premises and establishments directly connected without intermediate transformers to a low-voltage power supply network which supplies buildings used for residential purposes"
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("CATEGORY_C2"),
                        description=o6.LocalizedText(
                            "Installed in an equipment of rated voltage less than 1000 V, which is neither a plug-in device nor a movable device and, when used as described for Category C1, is intended to be installed and commissioned only by a professional"
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3,
                        displayName=o6.LocalizedText("CATEGORY_C3"),
                        description=o6.LocalizedText(
                            "Installed in an equipment of rated voltage less than 1000 V, intended for use in establishments other than those directly connected to a low voltage power supply network which supplies buildings used for residential purposes"
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4,
                        displayName=o6.LocalizedText("CATEGORY_C4"),
                        description=o6.LocalizedText(
                            "Installed in an equipment of rated voltage equal to or above 1000 V, or rated current equal to or above 400 A, or intended for use in complex systems (in Industrial areas or technical areas of any building)"
                        ),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6247", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtInputFilterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6155"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6156",
    browseName="ns=powertrain;LineFilterEmcClass",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6225",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0,
                        displayName=o6.LocalizedText("CLASS_A"),
                        description=o6.LocalizedText(
                            "Installed in an equipment suitable for use in all locations other than those allocated in residential environments and those directly connected to a low voltage power supply network which supplies buildings used for domestic purposes"
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("CLASS_B"),
                        description=o6.LocalizedText(
                            "Installed in an equipment suitable for use in locations in residential environments and in establishments directly connected to a low voltage power supply network which supplies buildings used for domestic purposes"
                        ),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6248", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtInputFilterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6156"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6157",
    browseName="ns=powertrain;LineFilterEmcGroup",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6226",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Other group")),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("GROUP_1"),
                        description=o6.LocalizedText("Installed in an equipment which is not covered by the one referred to in group 2"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("GROUP_2"),
                        description=o6.LocalizedText(
                            "Installed in an equipment in which radio-frequency energy in the frequency range 9 kHz to 400 GHz is intentionally generated and used or only used locally, in the form of electromagnetic radiation, inductive and/or capacitive coupling, for the treatment of material, for inspection/analysis purposes, or for transfer of electromagnetic energy"
                        ),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6249", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtInputFilterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6157"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6250",
    browseName="ns=powertrain;LineFilterPowerLoss",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6251", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtInputFilterAttributesType(
    nodeId="ns=powertrain;i=5024", browseName="ns=powertrain;PtInputFilterAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6250"])]
)
o6.reference(powertrain_objtypes.PtAssetInputFilterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5024"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6252",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6253", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5025", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6252"])]
)
o6.reference(powertrain_objtypes.PtAssetInputFilterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5025"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6254",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6255", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5026", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6254"])]
)
o6.reference(powertrain_objtypes.PtAssetReactorFilterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5026"])
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5027",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6256", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetReactorFilterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5027"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6258",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6259", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5028", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6258"])]
)
o6.reference(powertrain_objtypes.PtAssetOutputFilterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5028"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6260",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6261", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5029", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6260"])]
)
o6.reference(powertrain_objtypes.PtAssetOutputReactorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5029"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6239",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6263", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6264", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5034",
    browseName="ns=powertrain;PtCommunicationInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6239"])],
)
o6.reference(powertrain_objtypes.PtAssetSoftStarterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5034"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6218",
    browseName="ns=powertrain;EfficiencyClass",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6221",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("IE1"), description=o6.LocalizedText("Standard Efficiency")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("IE2"), description=o6.LocalizedText("High Efficiency")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("IE3"), description=o6.LocalizedText("Premium Efficiency")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("IE4"), description=o6.LocalizedText("Super Premium Efficiency")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("IE5"), description=o6.LocalizedText("Ultra Premium Efficiency")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("IES0"), description=o6.LocalizedText("Relative losses are higher than 20 % of the value defined by the RPDS")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=6, displayName=o6.LocalizedText("IES1"), description=o6.LocalizedText("Relative losses are within &#177;20 % of the value defined by the RPDS")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7, displayName=o6.LocalizedText("IES2"), description=o6.LocalizedText("Relative losses are smaller than 20 % of the value defined by the RPDS")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6267", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtInputConverterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6218"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6219",
    browseName="ns=powertrain;PowerFactorCorrection",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6268", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputConverterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6219"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6220",
    browseName="ns=powertrain;<PwmSwitchingFrequency>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6269", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputConverterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6220"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6223",
    browseName="ns=powertrain;RegenerativePowerRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6270", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputConverterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6223"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6150",
    browseName="ns=powertrain;EfficiencyClass",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6237",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("IE1"), description=o6.LocalizedText("Standard Efficiency")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("IE2"), description=o6.LocalizedText("High Efficiency")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("IE3"), description=o6.LocalizedText("Premium Efficiency")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("IE4"), description=o6.LocalizedText("Super Premium Efficiency")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("IE5"), description=o6.LocalizedText("Ultra Premium Efficiency")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("IES0"), description=o6.LocalizedText("Relative losses are higher than 20 % of the value defined by the RPDS")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=6, displayName=o6.LocalizedText("IES1"), description=o6.LocalizedText("Relative losses are within &#177;20 % of the value defined by the RPDS")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7, displayName=o6.LocalizedText("IES2"), description=o6.LocalizedText("Relative losses are smaller than 20 % of the value defined by the RPDS")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6271", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtOutputConverterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6150"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6241",
    browseName="ns=powertrain;OutputFilterType",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6273",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("SINE_WAVE_FILTER"), description=o6.LocalizedText("Component is a sine-wave filter")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DV_DT_FILTER"), description=o6.LocalizedText("Component is a dv/dt filter")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6280", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtOutputFilterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6241"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6290",
    browseName="ns=powertrain;TripClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6291", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6292", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6294",
    browseName="ns=powertrain;<DcBusVoltageRated>",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6295", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtMotorManagementDeviceAttributesType(
    nodeId="ns=powertrain;i=5035",
    browseName="ns=powertrain;PtMotorManagementDeviceAttributes",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6265", browseName="ns=powertrain;ControlVoltageAC50HzRangeRated", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6266", browseName="ns=powertrain;CosPhiVariationDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6274", browseName="ns=powertrain;CurrentImbalanceDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6275", browseName="ns=powertrain;GroundEarthFaultDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6276", browseName="ns=powertrain;HMIPortSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6277", browseName="ns=powertrain;JamDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6278", browseName="ns=powertrain;LoadSheddingSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6279", browseName="ns=powertrain;NumberOfAnalogInputs", dataType=o6.UInt16, value=0)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6281", browseName="ns=powertrain;NumberOfDigitalInputs", dataType=o6.UInt16, value=0)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6282", browseName="ns=powertrain;NumberOfDigitalOutputs", dataType=o6.UInt16, value=0)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6283", browseName="ns=powertrain;NumberOfPtcThermistorInputs", dataType=o6.UInt16, value=0)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6284", browseName="ns=powertrain;OverloadCurrentSettingRange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6285", browseName="ns=powertrain;OverUnderCurrentDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6286", browseName="ns=powertrain;OverUnderVoltageDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6287", browseName="ns=powertrain;PhaseLossSensitiveSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6288", browseName="ns=powertrain;PhaseReversalDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6289", browseName="ns=powertrain;StallDetectionSuported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6293", browseName="ns=powertrain;UnderPowerDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6297", browseName="ns=powertrain;VoltageMonitoringSupported", dataType=o6.Boolean, value=False)),
        o6.hasComponent(o6.ns["ns=powertrain;i=6290"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetMotorManagementDeviceType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5035"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6198",
    browseName="ns=powertrain;PrechargeThreshold",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6299", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtPrechargeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6198"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6300",
    browseName="ns=powertrain;PreChargeMaximumCapacitance",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6301", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtPrechargeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6300"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6303",
    browseName="ns=powertrain;PressureMin",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6304", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAmbientAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6303"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6163",
    browseName="ns=powertrain;PwmSwitchingFrequency",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6305", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtOutputConverterAttributesType(
    nodeId="ns=powertrain;i=5105", browseName="ns=powertrain;PtOutputConverterAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6163"])]
)
o6.reference(powertrain_objtypes.PtAssetInputOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5105"])
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5106",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6306", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetInputOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5106"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6298",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6308", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6309", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5036",
    browseName="ns=powertrain;PtCommunicationInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6298"])],
)
o6.reference(powertrain_objtypes.PtAssetMotorManagementDeviceType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5036"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6311",
    browseName="ns=powertrain;IpClass",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6312",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[52],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("IP00"), description=o6.LocalizedText("non-protected / non-protected")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("IP01"), description=o6.LocalizedText("non-protected / vertically dripping")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("IP02"), description=o6.LocalizedText("non-protected / dripping (15&#176; tilted)")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("IP10"), description=o6.LocalizedText("; 50 mm diameter / non-protected")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("IP11"), description=o6.LocalizedText("; 50 mm diameter / vertically dripping")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("IP12"), description=o6.LocalizedText("; 50 mm diameter / dripping (15&#176; tilted)")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("IP20"), description=o6.LocalizedText("; 12,5 mm diameter / non-protected")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("IP21"), description=o6.LocalizedText("; 12,5 mm diameter / vertically dripping")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("IP22"), description=o6.LocalizedText("; 12,5 mm diameter / dripping (15&#176; tilted)")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("IP30"), description=o6.LocalizedText("; 2,5 mm diameter / non-protected")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("IP31"), description=o6.LocalizedText("; 2,5 mm diameter / vertically dripping")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("IP32"), description=o6.LocalizedText("; 2,5 mm diameter / dripping (15&#176; tilted)")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("IP33"), description=o6.LocalizedText("; 2,5 mm diameter / spraying")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("IP40"), description=o6.LocalizedText("; 1,0 mm diameter / non-protected")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("IP41"), description=o6.LocalizedText("; 1,0 mm diameter / vertically dripping")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("IP42"), description=o6.LocalizedText("; 1,0 mm diameter / dripping (15&#176; tilted)")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("IP43"), description=o6.LocalizedText("; 1,0 mm diameter / spraying")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("IP44"), description=o6.LocalizedText("; 1,0 mm diameter / splashing")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("IP45"), description=o6.LocalizedText("; 1,0 mm diameter / jetting")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("IP50"), description=o6.LocalizedText("dust-protected / non-protected")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("IP51"), description=o6.LocalizedText("dust-protected / vertically dripping")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("IP52"), description=o6.LocalizedText("dust-protected / dripping (15&#176; tilted)")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("IP53"), description=o6.LocalizedText("dust-protected / spraying")),
                    ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("IP54"), description=o6.LocalizedText("dust-protected / splashing")),
                    ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("IP55"), description=o6.LocalizedText("dust-protected / jetting")),
                    ns0.datatypes.EnumValueType(value=25, displayName=o6.LocalizedText("IP56"), description=o6.LocalizedText("dust-protected / powerful jetting")),
                    ns0.datatypes.EnumValueType(value=26, displayName=o6.LocalizedText("IP57"), description=o6.LocalizedText("dust-protected / temporary immersion")),
                    ns0.datatypes.EnumValueType(value=27, displayName=o6.LocalizedText("IP58"), description=o6.LocalizedText("dust-protected / continuous immersion")),
                    ns0.datatypes.EnumValueType(value=28, displayName=o6.LocalizedText("IP60"), description=o6.LocalizedText("dust-tight / non-protected")),
                    ns0.datatypes.EnumValueType(value=29, displayName=o6.LocalizedText("IP61"), description=o6.LocalizedText("dust-tight / vertically dripping")),
                    ns0.datatypes.EnumValueType(value=30, displayName=o6.LocalizedText("IP62"), description=o6.LocalizedText("dust-tight / dripping (15&#176; tilted)")),
                    ns0.datatypes.EnumValueType(value=31, displayName=o6.LocalizedText("IP63"), description=o6.LocalizedText("dust-tight / spraying")),
                    ns0.datatypes.EnumValueType(value=32, displayName=o6.LocalizedText("IP64"), description=o6.LocalizedText("dust-tight / splashing")),
                    ns0.datatypes.EnumValueType(value=33, displayName=o6.LocalizedText("IP65"), description=o6.LocalizedText("dust-tight / jetting")),
                    ns0.datatypes.EnumValueType(value=34, displayName=o6.LocalizedText("IP66"), description=o6.LocalizedText("dust-tight / powerful jetting")),
                    ns0.datatypes.EnumValueType(value=35, displayName=o6.LocalizedText("IP67"), description=o6.LocalizedText("dust-tight / temporary immersion")),
                    ns0.datatypes.EnumValueType(value=36, displayName=o6.LocalizedText("IP68"), description=o6.LocalizedText("dust-tight / continuous immersion")),
                    ns0.datatypes.EnumValueType(
                        value=37, displayName=o6.LocalizedText("IP69"), description=o6.LocalizedText("dust-tight / high pressure and temperature water jet")
                    ),
                    ns0.datatypes.EnumValueType(value=38, displayName=o6.LocalizedText("IPX1"), description=o6.LocalizedText("not defined / vertically dripping")),
                    ns0.datatypes.EnumValueType(value=39, displayName=o6.LocalizedText("IPX2"), description=o6.LocalizedText("not defined / dripping (15&#176; tilted)")),
                    ns0.datatypes.EnumValueType(value=40, displayName=o6.LocalizedText("IPX3"), description=o6.LocalizedText("not defined / spraying")),
                    ns0.datatypes.EnumValueType(value=41, displayName=o6.LocalizedText("IPX4"), description=o6.LocalizedText("not defined / splashing")),
                    ns0.datatypes.EnumValueType(value=42, displayName=o6.LocalizedText("IPX5"), description=o6.LocalizedText("not defined / jetting")),
                    ns0.datatypes.EnumValueType(value=43, displayName=o6.LocalizedText("IPX6"), description=o6.LocalizedText("not defined / powerful jetting")),
                    ns0.datatypes.EnumValueType(value=44, displayName=o6.LocalizedText("IPX7"), description=o6.LocalizedText("not defined / temporary immersion")),
                    ns0.datatypes.EnumValueType(value=45, displayName=o6.LocalizedText("IPX8"), description=o6.LocalizedText("not defined / continuous immersion")),
                    ns0.datatypes.EnumValueType(value=46, displayName=o6.LocalizedText("IP1X"), description=o6.LocalizedText("; 50 mm diameter / not defined")),
                    ns0.datatypes.EnumValueType(value=47, displayName=o6.LocalizedText("IP2X"), description=o6.LocalizedText("; 12,5 mm diameter / not defined")),
                    ns0.datatypes.EnumValueType(value=48, displayName=o6.LocalizedText("IP3X"), description=o6.LocalizedText("; 2,5 mm diameter / not defined")),
                    ns0.datatypes.EnumValueType(value=49, displayName=o6.LocalizedText("IP4X"), description=o6.LocalizedText("; 1,0 mm diameter / not defined")),
                    ns0.datatypes.EnumValueType(value=50, displayName=o6.LocalizedText("IP5X"), description=o6.LocalizedText("dust-protected / not defined")),
                    ns0.datatypes.EnumValueType(value=51, displayName=o6.LocalizedText("IP6X"), description=o6.LocalizedText("dust-tight / not defined")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6313", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtProtectionClassAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6311"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6322",
    browseName="ns=powertrain;BrakeCurrentRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6323", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6322"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6321",
    browseName="ns=powertrain;TripClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6324", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6325", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    value=0,
)
powertrain_objtypes.PtElectronicOverloadRelayAttributesType(
    nodeId="ns=powertrain;i=5037",
    browseName="ns=powertrain;PtElectronicOverloadRelayAttributes",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6314", browseName="ns=powertrain;GroundEarthFaultDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6315", browseName="ns=powertrain;JamDetectionSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6316", browseName="ns=powertrain;NumberofAuxiliaryContactsNC", dataType=o6.UInt16, value=0)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6317", browseName="ns=powertrain;OverloadCurrentSettingRange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6318", browseName="ns=powertrain;PhaseLossSensitiveSupported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6320", browseName="ns=powertrain;StallDetectionSuported", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6326", browseName="ns=powertrain;VoltageRated", dataType=o6.UInt16, value=0)),
        o6.hasComponent(o6.ns["ns=powertrain;i=6321"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetElectricOverloadRelayType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5037"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6202",
    browseName="ns=powertrain;DutyType",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6329",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[10],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("S1"), description=o6.LocalizedText("Continuous duty")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("S2"), description=o6.LocalizedText("Short-time duty")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("S3"), description=o6.LocalizedText("Intermittent periodic duty")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("S4"), description=o6.LocalizedText("Intermittent periodic duty with starting")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("S5"), description=o6.LocalizedText("Intermittent periodic duty with electric braking")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("S6"), description=o6.LocalizedText("Continuous operation with intermittent load")),
                    ns0.datatypes.EnumValueType(
                        value=6, displayName=o6.LocalizedText("S7"), description=o6.LocalizedText("Continuous operation periodic duty with electric braking")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7, displayName=o6.LocalizedText("S8"), description=o6.LocalizedText("Continuous operation with periodic changes in load and speed")
                    ),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("S9"), description=o6.LocalizedText("Duty with non-periodic load and speed variations")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("S10"), description=o6.LocalizedText("Duty with discrete constant loads and speeds")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6330", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtMotorDutyAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6202"])
powertrain_objtypes.PtOutputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5107",
    browseName="ns=powertrain;PtOutputInterfaceAttributes",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6336", browseName="ns=powertrain;NumberOfOutputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetInputOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5107"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6337",
    browseName="ns=powertrain;<DcBusVoltageRated>",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6338", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6206",
    browseName="ns=powertrain;DcBusVoltageRange",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6340", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
)
o6.reference(powertrain_objtypes.PtDcBusAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6206"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6209",
    browseName="ns=powertrain;DcBusVoltageRange",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6341", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
)
powertrain_objtypes.PtDcBusAttributesType(
    nodeId="ns=powertrain;i=5022",
    browseName="ns=powertrain;PtDcBusAttributes",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6207"]), o6.hasComponent(o6.ns["ns=powertrain;i=6209"])],
)
o6.reference(powertrain_objtypes.PtAssetDcBusModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5022"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6235",
    browseName="ns=powertrain;DcBusVoltageRange",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6343", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6296",
    browseName="ns=powertrain;DcBusVoltageRange",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6344", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6345",
    browseName="ns=powertrain;BrakePowerRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6346", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6345"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6347",
    browseName="ns=powertrain;BrakeSurroundingAirTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6348", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6347"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6351",
    browseName="ns=powertrain;OutputCurrentMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6352", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtDigitalOutputElectricalAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6351"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6353",
    browseName="ns=powertrain;BreakingCapacity",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6354", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtFuseAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6353"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6355",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6356", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5067", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6355"])]
)
o6.reference(powertrain_objtypes.PtAssetInputReactorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5067"])
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5068",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6357", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetInputReactorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5068"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6349",
    browseName="ns=powertrain;DcBusVoltageRange",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6358", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
)
powertrain_objtypes.PtDcBusAttributesType(
    nodeId="ns=powertrain;i=5108", browseName="ns=powertrain;PtDcBusAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6349"])]
)
o6.reference(powertrain_objtypes.PtAssetInputOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5108"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6359",
    browseName="ns=powertrain;BrakeTorqueRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6360", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6359"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6361",
    browseName="ns=powertrain;OutputFilterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6362", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6363", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtOutputFilterAttributesType(
    nodeId="ns=powertrain;i=5110", browseName="ns=powertrain;PtOutputFilterAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6361"])]
)
o6.reference(powertrain_objtypes.PtAssetInputOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5110"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6339",
    browseName="ns=powertrain;DcBusVoltageRange",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6364", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6307",
    browseName="ns=powertrain;<PwmSwitchingFrequency>",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6365", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6327",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6342", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6366", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5038",
    browseName="ns=powertrain;PtCommunicationInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6327"])],
)
o6.reference(powertrain_objtypes.PtAssetElectricOverloadRelayType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5038"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6368",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6369", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5113",
    browseName="ns=powertrain;<PtReactorAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6368"])],
)
o6.reference(powertrain_objtypes.PtAssetInputOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5113"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6370",
    browseName="ns=powertrain;AltitudeMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6371", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAmbientAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6370"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6272",
    browseName="ns=powertrain;InputConverterType",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6372",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("AC/DC_PASSIVE"), description=o6.LocalizedText("Passive AC/DC converter")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AC/DC_ACTIVE"), description=o6.LocalizedText("Active AC/DC converter")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("DC/DC"), description=o6.LocalizedText("DC/DC converter")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6373", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtInputConverterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6272"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6319",
    browseName="ns=powertrain;OutputFilterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6375", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6376", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6377",
    browseName="ns=powertrain;TemperatureMin",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6379", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAmbientAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6377"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6380",
    browseName="ns=powertrain;PressureMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6381", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAmbientAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6380"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6382",
    browseName="ns=powertrain;TemperatureMax",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6383", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAmbientAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6382"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6386",
    browseName="ns=powertrain;FrequencyRange",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6387", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Range,
)
o6.reference(powertrain_objtypes.PtAnalogOutputElectricalAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6386"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6227",
    browseName="ns=powertrain;LineFilterPowerLoss",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6389", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6240",
    browseName="ns=powertrain;OutputFilterPowerLoss",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6390", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6394",
    browseName="ns=powertrain;TripClass",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6395",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[12],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CLASS_2E"), description=o6.LocalizedText("Thermal protection class 2E")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CLASS_3E"), description=o6.LocalizedText("Thermal protection class 3E")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CLASS_5"), description=o6.LocalizedText("Thermal protection class 5")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CLASS_5E"), description=o6.LocalizedText("Thermal protection class 5E")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("CLASS_10"), description=o6.LocalizedText("Thermal protection class 10")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("CLASS_10A"), description=o6.LocalizedText("Thermal protection class 10A")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("CLASS_10E"), description=o6.LocalizedText("Thermal protection class 10E")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("CLASS_20"), description=o6.LocalizedText("Thermal protection class 20")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("CLASS_20E"), description=o6.LocalizedText("Thermal protection class 20E")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("CLASS_30"), description=o6.LocalizedText("Thermal protection class 30")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CLASS_30E"), description=o6.LocalizedText("Thermal protection class 30E")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("CLASS_40E"), description=o6.LocalizedText("Thermal protection class 40E")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6396", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    value=0,
)
o6.reference(powertrain_objtypes.PtMotorStarterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6394"])
o6.reference(o6.ns["ns=powertrain;i=6394"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE213")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6388",
    browseName="ns=powertrain;InputCurrentRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6398", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6388"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6399",
    browseName="ns=powertrain;InputFrequencyMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6400", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6399"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6401",
    browseName="ns=powertrain;InputPowerRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6402", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6401"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6403",
    browseName="ns=powertrain;InputVoltageRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6404", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6403"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6409",
    browseName="ns=powertrain;ProtocolTypes",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6410",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[25],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0, displayName=o6.LocalizedText("ETHERCAT"), description=o6.LocalizedText("Ethernet for control automation technology for real-time systems")
                    ),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("PROFINET"), description=o6.LocalizedText("Process field network for real-time systems")),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("PROFINET_RT"), description=o6.LocalizedText("PROFINET class A, class B realtime communication")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3, displayName=o6.LocalizedText("PROFINET_IRT"), description=o6.LocalizedText("PROFINET class C isochronous realtime communication")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4, displayName=o6.LocalizedText("ETHERNET_IP"), description=o6.LocalizedText("Ethernet Industrial Protocol for real time system")
                    ),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("PROFIBUS"), description=o6.LocalizedText("Process field bus")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("PROFIBUS_DP"), description=o6.LocalizedText("Process field bus distributed peripherals")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("PROFIBUS_PA"), description=o6.LocalizedText("Process field bus process automation")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("SERCOS"), description=o6.LocalizedText("Serial realtime communication system")),
                    ns0.datatypes.EnumValueType(
                        value=9, displayName=o6.LocalizedText("SERCOS_III_SERCOS_II"), description=o6.LocalizedText("Serial realtime communication system III / II")
                    ),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CC_LINK"), description=o6.LocalizedText("Control &amp; communications fieldbus")),
                    ns0.datatypes.EnumValueType(
                        value=11, displayName=o6.LocalizedText("CANOPEN"), description=o6.LocalizedText("Control area network &#8211; open communications protocol")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=12,
                        displayName=o6.LocalizedText("IO_LINK"),
                        description=o6.LocalizedText("Simple communications protocol, short distances, bi-directional, digital and point-to-point"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=13, displayName=o6.LocalizedText("MODBUS"), description=o6.LocalizedText("Communications protocol over serial lines or via ethernet")
                    ),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("MODBUS_TCP"), description=o6.LocalizedText("Modbus over TCP/IP")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("MODBUS_RTU"), description=o6.LocalizedText("Modbus over serial lines")),
                    ns0.datatypes.EnumValueType(
                        value=16, displayName=o6.LocalizedText("DEVICENET"), description=o6.LocalizedText("DeviceNet - digital, multi-drop fieldbus protocol")
                    ),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("POWERLINK"), description=o6.LocalizedText("Ethernet powerlink")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("OPC_UA"), description=o6.LocalizedText("OPC Unified Architecture")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("MQTT"), description=o6.LocalizedText("Message queuing telemetry transport (MQTT)")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("INTERBUS"), description=o6.LocalizedText("Interbus")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("AS-I"), description=o6.LocalizedText("AS-I")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("CC_Link_IE_TSN"), description=o6.LocalizedText("CC-Link IE TSN")),
                    ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("CC_Link_IE_FIELD"), description=o6.LocalizedText("CC-Link IE Field Network")),
                    ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("CC_Link_IE_FIELD_BASIC"), description=o6.LocalizedText("CC-Link IE Field Network Basic")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6411", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(powertrain_objtypes.PtCommunicationInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6409"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6412",
    browseName="ns=powertrain;SafetyProtocolTypes",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6413",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[11],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("FF-SIS"), description=o6.LocalizedText("Fieldbus Foundation Safety Instrumented Systems")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CIP_SAFTEY"), description=o6.LocalizedText("Common Industrial Protocol Safety")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("PROFISAFE"), description=o6.LocalizedText("Process field safety")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("INTERBUS_SAFETY"), description=o6.LocalizedText("INTERBUS Safety")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("CC-Link_SAFETY"), description=o6.LocalizedText("CC-Link Safety")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("FAIL_SAFE_OVER_ETHERCAT_"), description=o6.LocalizedText("FailSafe over EtherCAT (FSoE)")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("ETHERNET_POWERLINK_SAFTETY"), description=o6.LocalizedText("Ethernet POWERLINK Safety")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("EPASAFETY"), description=o6.LocalizedText("EPASafety")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("RAPIENET_SAFETY"), description=o6.LocalizedText("RAPIEnet Safety")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("SAFETYNET_P"), description=o6.LocalizedText("SafetyNET p")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("OPENSAFETY"), description=o6.LocalizedText("openSAFETY")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6414", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(powertrain_objtypes.PtCommunicationInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6412"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6415",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6416", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6418", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5030",
    browseName="ns=powertrain;PtCommunicationInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6415"])],
)
o6.reference(powertrain_objtypes.PtAssetMotorStarterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5030"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6422",
    browseName="ns=powertrain;NoiseLevel",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6424", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtHardwareAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6422"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6425",
    browseName="ns=powertrain;HeatDissipationPower",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6426", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtHardwareAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6425"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6427",
    browseName="ns=powertrain;OutputCurrentRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6428", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6427"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6430",
    browseName="ns=powertrain;OutputPowerRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6431", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6430"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6384",
    browseName="ns=powertrain;DutyType",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6385",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[10],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("S1"), description=o6.LocalizedText("Continuous duty")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("S2"), description=o6.LocalizedText("Short-time duty")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("S3"), description=o6.LocalizedText("Intermittent periodic duty")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("S4"), description=o6.LocalizedText("Intermittent periodic duty with starting")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("S5"), description=o6.LocalizedText("Intermittent periodic duty with electric braking")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("S6"), description=o6.LocalizedText("Continuous operation with intermittent load")),
                    ns0.datatypes.EnumValueType(
                        value=6, displayName=o6.LocalizedText("S7"), description=o6.LocalizedText("Continuous operation periodic duty with electric braking")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7, displayName=o6.LocalizedText("S8"), description=o6.LocalizedText("Continuous operation with periodic changes in load and speed")
                    ),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("S9"), description=o6.LocalizedText("Duty with non-periodic load and speed variations")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("S10"), description=o6.LocalizedText("Duty with discrete constant loads and speeds")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6438", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtCertificateAttributesType(
    nodeId="ns=powertrain;i=5009",
    browseName="ns=powertrain;PtCertificateAttributes",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6055",
                browseName="ns=powertrain;Certificates",
                displayName="DefaultInstanceBrowsename",
                dataType=o6.QualifiedName,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6439",
                browseName="ns=powertrain;Certificates",
                displayName="DefaultInstanceBrowsename",
                dataType=o6.QualifiedName,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
o6.reference(powertrain_objtypes.PtAssetType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=5009"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6429",
    browseName="ns=powertrain;OutputFrequencyRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6441", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6429"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6442",
    browseName="ns=powertrain;CurrentRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6445", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtFuseAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6442"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6444",
    browseName="ns=powertrain;VoltageRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6446", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtFuseAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6444"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6447",
    browseName="ns=powertrain;OutputVoltageRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6448", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6447"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6450",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6451", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5065", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6450"])]
)
o6.reference(powertrain_objtypes.PtAssetInputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5065"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6452",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6453", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5066", browseName="ns=powertrain;PtReactorAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6452"])]
)
o6.reference(powertrain_objtypes.PtAssetOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5066"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6461",
    browseName="ns=powertrain;LubricantType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6474",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[28],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Other viscosity grade")),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("ISO_VG_2"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 2")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("ISO_VG_3"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 3")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3, displayName=o6.LocalizedText("ISO_VG_5"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 5")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4, displayName=o6.LocalizedText("ISO_VG_7"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 7")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("ISO_VG_10"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 10")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=6, displayName=o6.LocalizedText("ISO_VG_15"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 15")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7, displayName=o6.LocalizedText("ISO_VG_22"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 22")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=8, displayName=o6.LocalizedText("ISO_VG_32"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 32")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=9, displayName=o6.LocalizedText("ISO_VG_46"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 46")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=10, displayName=o6.LocalizedText("ISO_VG_68"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 68")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=11, displayName=o6.LocalizedText("ISO_VG_100"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 100")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=12, displayName=o6.LocalizedText("ISO_VG_150"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 150")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=13, displayName=o6.LocalizedText("ISO_VG_220"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 220")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=14, displayName=o6.LocalizedText("ISO_VG_320"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 320")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=15, displayName=o6.LocalizedText("ISO_VG_460"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 460")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=16, displayName=o6.LocalizedText("ISO_VG_680"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 680")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=17, displayName=o6.LocalizedText("ISO_VG_1000"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 1000")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=18, displayName=o6.LocalizedText("ISO_VG_1500"), description=o6.LocalizedText("International Organization for Standardization Viscosity Grade 1500")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=19, displayName=o6.LocalizedText("NLGI_000"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 000")
                    ),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("NLGI_00"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 00")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("NLGI_0"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 0")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("NLGI_1"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 1")),
                    ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("NLGI_2"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 2")),
                    ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("NLGI_3"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 3")),
                    ns0.datatypes.EnumValueType(value=25, displayName=o6.LocalizedText("NLGI_4"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 4")),
                    ns0.datatypes.EnumValueType(value=26, displayName=o6.LocalizedText("NLGI_5"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 5")),
                    ns0.datatypes.EnumValueType(value=27, displayName=o6.LocalizedText("NLGI_6"), description=o6.LocalizedText("National Lubricating Grease Institute_Class 6")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6478", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6461"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6333",
    browseName="ns=powertrain;EncoderTechnology",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6334",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OPTICAL"), description=o6.LocalizedText("Optical encoder")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MAGNETIC"), description=o6.LocalizedText("Magnetic encoder")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("INDUCTIVE"), description=o6.LocalizedText("Inductive encoder")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CAPACITIVE"), description=o6.LocalizedText("Capacitive encoder")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("DRAW_WIRE"), description=o6.LocalizedText("Encoder with draw wire mechanics")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("MEASURING_WHEEL"), description=o6.LocalizedText("Encoder with measuring wheel mechanics")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("RESOLVER"), description=o6.LocalizedText("Resolver")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6479", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtEncoderAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6333"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6462",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6473", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6489", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5116",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6462"])],
)
o6.reference(powertrain_objtypes.PtAssetInputOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5116"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6485",
    browseName="ns=powertrain;EncoderType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6487",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ROT_SINGLE_TURN"), description=o6.LocalizedText("Rotary absolute single-turn")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ROT_MULTI_TURN"), description=o6.LocalizedText("Rotary absolute multi-turn")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ROT_INCREMENTAL"), description=o6.LocalizedText("Rotary incremental")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("LINEAR_INCREMENTAL"), description=o6.LocalizedText("Linear incremental")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("LINEAR_ABSOLUTE"), description=o6.LocalizedText("Linear absolute")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("LINEAR_DIST_CODE"), description=o6.LocalizedText("Linear absolute distance coded")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6491", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtEncoderAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6485"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6492",
    browseName="ns=powertrain;EncoderSignal",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6493",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0, displayName=o6.LocalizedText("RS-422_5V_TTL"), description=o6.LocalizedText("RS-422 (TTL - transistor transistor logic), 5 V signal level")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("RS-422_5-30V"), description=o6.LocalizedText("RS-422 signal level depend from entry level 5 V to 30 V")
                    ),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SINCOS_1VPP"), description=o6.LocalizedText("SinCos, 1 Vss output level")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("RESOLVER"), description=o6.LocalizedText("Resolver signal")),
                    ns0.datatypes.EnumValueType(
                        value=4,
                        displayName=o6.LocalizedText("HTL_PUSH-PULL"),
                        description=o6.LocalizedText("High threshold logic (HTL), typically voltage ranges from 5 to 30 VDC"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("RS-485"), description=o6.LocalizedText("RS-485, signal is transmitted over a Sig+ line and a Sig- line")
                    ),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("RS-485_SINCOS"), description=o6.LocalizedText("RS-485, sin-/cos-signal")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("RS-485_HTL"), description=o6.LocalizedText("RS-485, high threshold logic (HTL) signal")),
                    ns0.datatypes.EnumValueType(
                        value=8, displayName=o6.LocalizedText("RS-485_TTL"), description=o6.LocalizedText("RS-485, transistor transistor logic (TTL) signal")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6494", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtEncoderInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6492"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6302",
    browseName="ns=powertrain;PreChargeCycleTimeLimit",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6500", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(powertrain_objtypes.PtPrechargeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6302"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6503",
    browseName="ns=powertrain;OutputFilterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6504", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6505", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6511",
    browseName="ns=powertrain;ProfileTypes",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6512",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0, displayName=o6.LocalizedText("CIA_402"), description=o6.LocalizedText("CANopen device profile for drives and motion control")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("PROFIDRIVE"),
                        description=o6.LocalizedText(
                            "PROFIdrive is the modular, manufacturer-independent device profile for drive devices from Profibus &amp; Profinet International"
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("PROFIENERGY"), description=o6.LocalizedText("PROFIenergy is a profile for energy management in production plants")
                    ),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("COE"), description=o6.LocalizedText("CANopen over EtherCAT")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("SOE"), description=o6.LocalizedText("Servo Drive Profile over EtherCAT")),
                    ns0.datatypes.EnumValueType(
                        value=5,
                        displayName=o6.LocalizedText("CIP_MOTION"),
                        description=o6.LocalizedText("CIP motion technology provides application profiles that allow position, speed and torque loops to be set within a drive"),
                    ),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("SERCOS"), description=o6.LocalizedText("Serial Real-time Communication System")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6513", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(powertrain_objtypes.PtCommunicationInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6511"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6521",
    browseName="ns=powertrain;FunctionalSafetyCategory",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6523",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CAT_B"), description=o6.LocalizedText("Category B")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CAT_1"), description=o6.LocalizedText("Category 1")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CAT_2"), description=o6.LocalizedText("Category 2")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CAT_3"), description=o6.LocalizedText("Category 3")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("CAT_4"), description=o6.LocalizedText("Category 4")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6524", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtSafetyFunctionsAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6521"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6495",
    browseName="ns=powertrain;EncoderProtocol",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6496",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[15],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("BISS_C"), description=o6.LocalizedText("BiSS interface continuous mode")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ENDAT_2.1"), description=o6.LocalizedText("EnDat (encoder data), operating mode 2.1")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ENDAT_2.2"), description=o6.LocalizedText("EnDat (encoder data), operating mode 2.2")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ENDAT_3"), description=o6.LocalizedText("EnDat (encoder data), operating mode 3")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("HIPERFACE"), description=o6.LocalizedText("Hiperface")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("HIPERFACE_DSL"), description=o6.LocalizedText("Hiperface DSL (digital servo link)")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("SSI_BINARY"), description=o6.LocalizedText("Binary synchronous serial output (SSI)")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("SSI_GRAY_CODE"), description=o6.LocalizedText("Gray code synchronous serial output (SSI)")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("SCS_OPEN_LINK"), description=o6.LocalizedText("Single cable solution (open link)")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("DRIVE-CLIQ"), description=o6.LocalizedText("DRIVE-CLiQ")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("BISS_LINE"), description=o6.LocalizedText("BiSS Line")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("FANUC_37BIT_SERIAL_COMM"), description=o6.LocalizedText("Fanuc 37 bit serial interface")),
                    ns0.datatypes.EnumValueType(
                        value=12, displayName=o6.LocalizedText("MITSUBISHI_40BIT_SERIAL_COMM"), description=o6.LocalizedText("Mitsubishi 40 bit serial interface")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=13, displayName=o6.LocalizedText("OMRON/PANASONIC_48BIT_SERIAL_COMM"), description=o6.LocalizedText("OMRON/Panasonic 48 bit serial interface")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=14, displayName=o6.LocalizedText("YASKAWA_36BIT_SERIAL_COMM"), description=o6.LocalizedText("Yaskawa 36 bit serial interface")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6526", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtEncoderInterfaceProtocolAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6495"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6335",
    browseName="ns=powertrain;BrakeDesignType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6350",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0,
                        displayName=o6.LocalizedText("MAGNETIC"),
                        description=o6.LocalizedText("Slow, prevent or stop the motion using electromagnetic force to apply friction"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("SPRING"),
                        description=o6.LocalizedText("A spring continuously presses the friction brake against an armature and decreases, prevent or stop the motion"),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6528", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6335"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6529",
    browseName="ns=powertrain;BrakeTorqueHolding",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6530", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6529"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6490",
    browseName="ns=powertrain;PreChargeType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6531", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6532", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtPrechargeAttributesType(
    nodeId="ns=powertrain;i=5117", browseName="ns=powertrain;PtPrechargeAttributes", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6490"])]
)
o6.reference(powertrain_objtypes.PtAssetPrechargeType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5117"])
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5118",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6533", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetPrechargeType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5118"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6534",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6535", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6536", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5121",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6534"])],
)
o6.reference(powertrain_objtypes.PtAssetPrechargeType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5121"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6537",
    browseName="ns=powertrain;BrakeType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6538", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6539", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6540",
    browseName="ns=powertrain;BrakeDesignType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6541", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6542", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6543",
    browseName="ns=powertrain;BrakeType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6544", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6545", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6546",
    browseName="ns=powertrain;BrakeDesignType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6547", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6548", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6549",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6550", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6551", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=5122",
    browseName="ns=powertrain;PtCommunicationInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6549"])],
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5122"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6552",
    browseName="ns=powertrain;PowerRated",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6553", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtBleedAttributesType(
    nodeId="ns=powertrain;i=5123", browseName="ns=powertrain;PtBleedAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6552"])]
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5123"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6497",
    browseName="ns=powertrain;TemperatureSensorTechnology",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6498", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6555", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6556",
    browseName="ns=powertrain;TemperatureSensorTechnology",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6557", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6558", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6499",
    browseName="ns=powertrain;AnalogInputElectricalType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6559",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[13],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("VOLTAGE_0-10V"), description=o6.LocalizedText("Voltage range 0-10 volt")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("VOLTAGE_-10-10V"), description=o6.LocalizedText("Voltage range -10-10 volt")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CURRENT_0-20MA"), description=o6.LocalizedText("Current range 0-20 milliampere")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CURRENT_4-20MA"), description=o6.LocalizedText("Current range 4-20 milliampere")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("TEMPERATURE_PT1000"), description=o6.LocalizedText("PT1000 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("TEMPERATURE_PT100"), description=o6.LocalizedText("PT100 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("TEMPERATURE_KTY"), description=o6.LocalizedText("KTY temperature sensor")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("TEMPERATURE_KTY84"), description=o6.LocalizedText("KTY84 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("TEMPERATURE_PTC"), description=o6.LocalizedText("PTC temperature sensor")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("VOLTAGE"), description=o6.LocalizedText("Other voltage interface")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CURRENT"), description=o6.LocalizedText("Other current interface")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("TEMPERATURE"), description=o6.LocalizedText("Other temperature interface")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("CONFIGURABLE"), description=o6.LocalizedText("Configurable")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6560", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6499"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6561",
    browseName="ns=powertrain;AnalogOutputElectricalType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6562",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[13],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("VOLTAGE_0-10V"), description=o6.LocalizedText("Voltage range 0-10 volt")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("VOLTAGE_-10-10V"), description=o6.LocalizedText("Voltage range -10-10 volt")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CURRENT_0-20MA"), description=o6.LocalizedText("Current range 0-20 milliampere")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CURRENT_4-20MA"), description=o6.LocalizedText("Current range 4-20 milliampere")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("TEMPERATURE_PT1000"), description=o6.LocalizedText("PT1000 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("TEMPERATURE_PT100"), description=o6.LocalizedText("PT100 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("TEMPERATURE_KTY"), description=o6.LocalizedText("KTY temperature sensor")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("TEMPERATURE_KTY84"), description=o6.LocalizedText("KTY84 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("TEMPERATURE_PTC"), description=o6.LocalizedText("PTC temperature sensor")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("VOLTAGE"), description=o6.LocalizedText("Other voltage interface")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CURRENT"), description=o6.LocalizedText("Other current interface")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("TEMPERATURE"), description=o6.LocalizedText("Other temperature interface")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("CONFIGURABLE"), description=o6.LocalizedText("Configurable")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6563", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6561"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6564",
    browseName="ns=powertrain;DigitalInputElectricalType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6565",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("TTL"), description=o6.LocalizedText("Transistor-transistor logic (0..5 V)")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("HTL"), description=o6.LocalizedText("High threshold logic (0..24 V)")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("PNP"), description=o6.LocalizedText("PNP transistor type")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("NPN"), description=o6.LocalizedText("NPN transistor type")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("CONFIGURABLE"), description=o6.LocalizedText("Configurable")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("PULSE_TRAIN"), description=o6.LocalizedText("Pulse train")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("RELAY"), description=o6.LocalizedText("Electromechanical relay")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6566", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6564"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6567",
    browseName="ns=powertrain;DigitalOutputElectricalType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6568",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("TTL"), description=o6.LocalizedText("Transistor-transistor logic (0..5 V)")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("HTL"), description=o6.LocalizedText("High threshold logic (0..24 V)")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("PNP"), description=o6.LocalizedText("PNP transistor type")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("NPN"), description=o6.LocalizedText("NPN transistor type")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("CONFIGURABLE"), description=o6.LocalizedText("Configurable")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("PULSE_TRAIN"), description=o6.LocalizedText("Pulse train")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("RELAY"), description=o6.LocalizedText("Electromechanical relay")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6569", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6567"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6570",
    browseName="ns=powertrain;OutputFunction",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6571",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ACTIVE_OPEN"), description=o6.LocalizedText("Active function signal by open output")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ACTIVE_CLOSED"), description=o6.LocalizedText("Active function signal by closed output")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6572", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6570"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6573",
    browseName="ns=powertrain;Resolution",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6574", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6573"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6501",
    browseName="ns=powertrain;Capacitance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6575", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtCapacitanceAttributesType(
    nodeId="ns=powertrain;i=5023", browseName="ns=powertrain;PtCapacitanceAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6501"])]
)
o6.reference(powertrain_objtypes.PtAssetDcBusModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5023"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6576",
    browseName="ns=powertrain;Capacitance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6577", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtCapacitanceAttributesType(
    nodeId="ns=powertrain;i=5081", browseName="ns=powertrain;PtCapacitanceAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6576"])]
)
o6.reference(powertrain_objtypes.PtAssetInputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5081"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6578",
    browseName="ns=powertrain;Capacitance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6579", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtCapacitanceAttributesType(
    nodeId="ns=powertrain;i=5083", browseName="ns=powertrain;PtCapacitanceAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6578"])]
)
o6.reference(powertrain_objtypes.PtAssetOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5083"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6581",
    browseName="ns=powertrain;InputConverterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6582", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6583", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6592",
    browseName="ns=powertrain;TripClass",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6593", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6594", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6508",
    browseName="ns=powertrain;HumidityMin",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6604", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAmbientAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6508"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6605",
    browseName="ns=powertrain;HumidityMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6606", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAmbientAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6605"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6607",
    browseName="ns=powertrain;TemperatureMin",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6608", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6609",
    browseName="ns=powertrain;TemperatureMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6610", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtAmbientAttributesType(
    nodeId="ns=powertrain;i=5010",
    browseName="ns=powertrain;PtAmbientAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6607"]), o6.hasComponent(o6.ns["ns=powertrain;i=6609"])],
)
o6.reference(powertrain_objtypes.PtAssetType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=5010"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6509",
    browseName="ns=powertrain;AnalogInputElectricalType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6611",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[13],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("VOLTAGE_0-10V"), description=o6.LocalizedText("Voltage range 0-10 volt")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("VOLTAGE_-10-10V"), description=o6.LocalizedText("Voltage range -10-10 volt")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CURRENT_0-20MA"), description=o6.LocalizedText("Current range 0-20 milliampere")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CURRENT_4-20MA"), description=o6.LocalizedText("Current range 4-20 milliampere")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("TEMPERATURE_PT1000"), description=o6.LocalizedText("PT1000 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("TEMPERATURE_PT100"), description=o6.LocalizedText("PT100 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("TEMPERATURE_KTY"), description=o6.LocalizedText("KTY temperature sensor")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("TEMPERATURE_KTY84"), description=o6.LocalizedText("KTY84 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("TEMPERATURE_PTC"), description=o6.LocalizedText("PTC temperature sensor")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("VOLTAGE"), description=o6.LocalizedText("Other voltage interface")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CURRENT"), description=o6.LocalizedText("Other current interface")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("TEMPERATURE"), description=o6.LocalizedText("Other temperature interface")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("CONFIGURABLE"), description=o6.LocalizedText("Configurable")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6612", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtAnalogInputElectricalAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6509"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6510",
    browseName="ns=powertrain;AnalogOutputElectricalType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6616",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[13],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("VOLTAGE_0-10V"), description=o6.LocalizedText("Voltage range 0-10 volt")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("VOLTAGE_-10-10V"), description=o6.LocalizedText("Voltage range -10-10 volt")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CURRENT_0-20MA"), description=o6.LocalizedText("Current range 0-20 milliampere")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CURRENT_4-20MA"), description=o6.LocalizedText("Current range 4-20 milliampere")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("TEMPERATURE_PT1000"), description=o6.LocalizedText("PT1000 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("TEMPERATURE_PT100"), description=o6.LocalizedText("PT100 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("TEMPERATURE_KTY"), description=o6.LocalizedText("KTY temperature sensor")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("TEMPERATURE_KTY84"), description=o6.LocalizedText("KTY84 temperature sensor")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("TEMPERATURE_PTC"), description=o6.LocalizedText("PTC temperature sensor")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("VOLTAGE"), description=o6.LocalizedText("Other voltage interface")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CURRENT"), description=o6.LocalizedText("Other current interface")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("TEMPERATURE"), description=o6.LocalizedText("Other temperature interface")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("CONFIGURABLE"), description=o6.LocalizedText("Configurable")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6617", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtAnalogOutputElectricalAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6510"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6554",
    browseName="ns=powertrain;InputConverterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6623", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6624", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtInputConverterAttributesType(
    nodeId="ns=powertrain;i=5124", browseName="ns=powertrain;PtInputConverterAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6554"])]
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5124"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6626",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6627", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6628", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6629",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6630", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6631", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6632",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6633", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6634", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6635",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6636", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6637", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6641",
    browseName="ns=powertrain;ProtocolTypes",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6642", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6643", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6625",
    browseName="ns=powertrain;PwmSwitchingFrequency",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6644", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtOutputConverterAttributesType(
    nodeId="ns=powertrain;i=5125",
    browseName="ns=powertrain;<PtOutputConverterAttributes>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6625"])],
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5125"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6645",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6646", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5126", browseName="ns=powertrain;PtInputReactorAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6645"])]
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5126"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6514",
    browseName="ns=powertrain;CoolingMethod",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6647",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0, displayName=o6.LocalizedText("AIR_COOLED_STATIC"), description=o6.LocalizedText("Cooled by just free ventilation openings")
                    ),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AIR_COOLED_FORCED"), description=o6.LocalizedText("Cooled using a fan")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("LIQUID_COOLED"), description=o6.LocalizedText("Cooled using liquid")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6648", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtCoolingAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6514"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6515",
    browseName="ns=powertrain;DigitalInputElectricalType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6516",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("TTL"), description=o6.LocalizedText("Transistor-transistor logic (0..5 V)")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("HTL"), description=o6.LocalizedText("High threshold logic (0..24 V)")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("PNP"), description=o6.LocalizedText("PNP transistor type")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("NPN"), description=o6.LocalizedText("NPN transistor type")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("CONFIGURABLE"), description=o6.LocalizedText("Configurable")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("PULSE_TRAIN"), description=o6.LocalizedText("Pulse train")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("RELAY"), description=o6.LocalizedText("Electromechanical relay")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6649", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtDigitalInputElectricalAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6515"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6517",
    browseName="ns=powertrain;DigitalOutputElectricalType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6650",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("TTL"), description=o6.LocalizedText("Transistor-transistor logic (0..5 V)")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("HTL"), description=o6.LocalizedText("High threshold logic (0..24 V)")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("PNP"), description=o6.LocalizedText("PNP transistor type")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("NPN"), description=o6.LocalizedText("NPN transistor type")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("CONFIGURABLE"), description=o6.LocalizedText("Configurable")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("PULSE_TRAIN"), description=o6.LocalizedText("Pulse train")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("RELAY"), description=o6.LocalizedText("Electromechanical relay")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6651", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtDigitalOutputElectricalAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6517"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6518",
    browseName="ns=powertrain;FuseElementSpeedMarking",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6652",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[19],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("FF"), description=o6.LocalizedText("Very fast acting")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("F"), description=o6.LocalizedText("Fast acting")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("M"), description=o6.LocalizedText("Medium acting")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("T"), description=o6.LocalizedText("Slow acting")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("TT"), description=o6.LocalizedText("Very slow acting")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("AR"), description=o6.LocalizedText("Partial-range breaking capacity (short-circuit protection only)")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=6, displayName=o6.LocalizedText("GR"), description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection)")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7, displayName=o6.LocalizedText("GS"), description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection)")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=8, displayName=o6.LocalizedText("GRL"), description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection)")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=9,
                        displayName=o6.LocalizedText("GG"),
                        description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection) for general applications"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=10,
                        displayName=o6.LocalizedText("GL"),
                        description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection) for general applications"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=11,
                        displayName=o6.LocalizedText("GF"),
                        description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection) for general applications"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=12,
                        displayName=o6.LocalizedText("AM"),
                        description=o6.LocalizedText("Partial-range breaking capacity (short-circuit protection only) for the protection of motor circuits"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=13,
                        displayName=o6.LocalizedText("GM"),
                        description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection) for the protection of motor circuits"),
                    ),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("GPV"), description=o6.LocalizedText("Protection of solar photovoltaic arrays")),
                    ns0.datatypes.EnumValueType(
                        value=15,
                        displayName=o6.LocalizedText("GB"),
                        description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection) robust for mining application"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=16,
                        displayName=o6.LocalizedText("GTR"),
                        description=o6.LocalizedText("Full-range breaking capacity (overload and short-circuit protection) for protection of transformers"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=17, displayName=o6.LocalizedText("GN"), description=o6.LocalizedText("North American general purpose for protection of conductors")
                    ),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("GD"), description=o6.LocalizedText("North American general purpose, time delay")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6653", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtFuseAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6518"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6654",
    browseName="ns=powertrain;InputVoltageMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6655", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6654"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6657",
    browseName="ns=powertrain;InputVoltageRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6658", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6657"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6659",
    browseName="ns=powertrain;InputCurrentRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6660", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6659"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6661",
    browseName="ns=powertrain;FunctionalSafetyPerformanceLevel",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6662",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("PLA"), description=o6.LocalizedText("Performance level a")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("PLB"), description=o6.LocalizedText("Performance level b")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("PLC"), description=o6.LocalizedText("Performance level c")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("PLD"), description=o6.LocalizedText("Performance level d")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("PLE"), description=o6.LocalizedText("Performance level e")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6663", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtSafetyFunctionsAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6661"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6664",
    browseName="ns=powertrain;FunctionalSafetySilLevel",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6665",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("SIL_1"), description=o6.LocalizedText("Safety integrity level 1")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("SIL_2"), description=o6.LocalizedText("Safety integrity level 2")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SIL_3"), description=o6.LocalizedText("Safety integrity level 3")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("SIL_4"), description=o6.LocalizedText("Safety integrity level 4")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6666", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtSafetyFunctionsAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6664"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6667",
    browseName="ns=powertrain;SafetyFunctions",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6668",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[16],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("STO"), description=o6.LocalizedText("Safe torque off")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("SS1"), description=o6.LocalizedText("Safe stop 1")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SS2"), description=o6.LocalizedText("Safe stop 2")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("SOS"), description=o6.LocalizedText("Safe operating stop")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("SLS"), description=o6.LocalizedText("Safely limited speed")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("SSM"), description=o6.LocalizedText("Safe speed monitor")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("SSR"), description=o6.LocalizedText("Safe speed range")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("SLP"), description=o6.LocalizedText("Safe limited position")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("SP"), description=o6.LocalizedText("Safe position")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("SDI"), description=o6.LocalizedText("Safe direction")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("SBC"), description=o6.LocalizedText("Safe brake control")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("SBT"), description=o6.LocalizedText("Safe brake test")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("S-DI"), description=o6.LocalizedText("Safe digital input")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("S-DO"), description=o6.LocalizedText("Safe digital output")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("S-AI"), description=o6.LocalizedText("Safe analog input")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("S-AO"), description=o6.LocalizedText("Safe analog output")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6669", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtSafetyFunctionsAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6667"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6670",
    browseName="ns=powertrain;MotorInertia",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6671", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6670"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6672",
    browseName="ns=powertrain;MotorBackEMF",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6673", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6672"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6674",
    browseName="ns=powertrain;MotorPolePairPitch",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6675", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6674"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6676",
    browseName="ns=powertrain;ForcerWeight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6677", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6676"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6678",
    browseName="ns=powertrain;MotorBackEMF",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6679", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6678"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6680",
    browseName="ns=powertrain;MotorSpeedMax",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6681", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRotaryRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6680"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6682",
    browseName="ns=powertrain;MotorSpeedRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6683", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRotaryRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6682"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6684",
    browseName="ns=powertrain;MotorTorqueMax",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6685", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRotaryRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6684"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6686",
    browseName="ns=powertrain;MotorTorqueRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6687", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRotaryRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6686"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6688",
    browseName="ns=powertrain;MotorTorqueContinuousStall",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6689", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRotaryRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6688"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6690",
    browseName="ns=powertrain;MotorTorqueConstant",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6691", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRotaryRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6690"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6692",
    browseName="ns=powertrain;MotorSpeedMax",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6693", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6692"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6694",
    browseName="ns=powertrain;MotorSpeedRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6695", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6694"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6696",
    browseName="ns=powertrain;MotorForceMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6697", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6696"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6698",
    browseName="ns=powertrain;MotorForceRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6698"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6700",
    browseName="ns=powertrain;MotorForceContinuousStall",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6701", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6700"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6702",
    browseName="ns=powertrain;MotorForceConstant",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6703", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorLinearRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6702"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6705",
    browseName="ns=powertrain;FeedbackResolverExcitationVoltage",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6706", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6705"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6707",
    browseName="ns=powertrain;FeedbackResolverExcitationFrequency",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6708", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6707"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6710",
    browseName="ns=powertrain;EncoderRotarySpeedMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6711", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6710"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6712",
    browseName="ns=powertrain;ResolutionRotaryIncremental",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6713", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6712"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6714",
    browseName="ns=powertrain;ResolutionSingleturnAbsolute",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6715", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6714"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6716",
    browseName="ns=powertrain;ResolutionMultiturnAbsolute",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6717", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6716"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6718",
    browseName="ns=powertrain;EncoderFlangeSize",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6719", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6718"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6720",
    browseName="ns=powertrain;EncoderFlangeType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6721",
                browseName="EnumValues",
                description="Contactless encoder",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CONTACTLESS"), description=o6.LocalizedText("Contactless encoder")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("SYNCHRO"), description=o6.LocalizedText("Synchro flange")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CLAMPING"), description=o6.LocalizedText("Clamping flange")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("HOLLOW_SHAFT"), description=o6.LocalizedText("Hollow shaft flange")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("BLIND_HOLLOW"), description=o6.LocalizedText("Blind hollow shaft flange")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("SERVO_FLANGE"), description=o6.LocalizedText("Centered flange mount")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("FACE_MOUNT"), description=o6.LocalizedText("Face mount with torque compensator")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6722", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6720"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6723",
    browseName="ns=powertrain;EncoderShaftType",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6724",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("THROUGH-HOLLOW"), description=o6.LocalizedText("Through hollow shaft type")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("BLIND-HOLLOW"), description=o6.LocalizedText("Blind hollow shaft type")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("TAPERED"), description=o6.LocalizedText("Tapered shaft type")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("STRAIGHT"), description=o6.LocalizedText("Straight shaft type")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("SOLID"), description=o6.LocalizedText("Solid shaft type")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("CONE"), description=o6.LocalizedText("Cone shaft type")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6725", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6723"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6726",
    browseName="ns=powertrain;EncoderShaftSize",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6727", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(powertrain_objtypes.PtEncoderRotaryAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6726"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6729",
    browseName="ns=powertrain;ResolutionLinearAbsolute",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6730", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtEncoderLinearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6729"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6731",
    browseName="ns=powertrain;RangeLinear",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6732", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
)
o6.reference(powertrain_objtypes.PtEncoderLinearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6731"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6734",
    browseName="ns=powertrain;EncoderReadingDistance",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6735", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtEncoderLinearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6734"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6736",
    browseName="ns=powertrain;EncoderSpeedLinearMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6737", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtEncoderLinearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6736"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6739",
    browseName="ns=powertrain;TripClass",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6740",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[12],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CLASS_2E"), description=o6.LocalizedText("Thermal protection class 2E")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CLASS_3E"), description=o6.LocalizedText("Thermal protection class 3E")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CLASS_5"), description=o6.LocalizedText("Thermal protection class 5")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CLASS_5E"), description=o6.LocalizedText("Thermal protection class 5E")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("CLASS_10"), description=o6.LocalizedText("Thermal protection class 10")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("CLASS_10A"), description=o6.LocalizedText("Thermal protection class 10A")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("CLASS_10E"), description=o6.LocalizedText("Thermal protection class 10E")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("CLASS_20"), description=o6.LocalizedText("Thermal protection class 20")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("CLASS_20E"), description=o6.LocalizedText("Thermal protection class 20E")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("CLASS_30"), description=o6.LocalizedText("Thermal protection class 30")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CLASS_30E"), description=o6.LocalizedText("Thermal protection class 30E")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("CLASS_40E"), description=o6.LocalizedText("Thermal protection class 40E")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6741", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    value=0,
)
o6.reference(powertrain_objtypes.PtElectronicOverloadRelayAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6739"])
o6.reference(o6.ns["ns=powertrain;i=6739"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE213")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6753",
    browseName="ns=powertrain;TripClass",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6754",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[12],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CLASS_2E"), description=o6.LocalizedText("Thermal protection class 2E")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CLASS_3E"), description=o6.LocalizedText("Thermal protection class 3E")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CLASS_5"), description=o6.LocalizedText("Thermal protection class 5")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CLASS_5E"), description=o6.LocalizedText("Thermal protection class 5E")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("CLASS_10"), description=o6.LocalizedText("Thermal protection class 10")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("CLASS_10A"), description=o6.LocalizedText("Thermal protection class 10A")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("CLASS_10E"), description=o6.LocalizedText("Thermal protection class 10E")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("CLASS_20"), description=o6.LocalizedText("Thermal protection class 20")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("CLASS_20E"), description=o6.LocalizedText("Thermal protection class 20E")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("CLASS_30"), description=o6.LocalizedText("Thermal protection class 30")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CLASS_30E"), description=o6.LocalizedText("Thermal protection class 30E")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("CLASS_40E"), description=o6.LocalizedText("Thermal protection class 40E")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6755", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
    value=0,
)
o6.reference(powertrain_objtypes.PtMotorManagementDeviceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=6753"])
o6.reference(o6.ns["ns=powertrain;i=6753"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE213")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6774",
    browseName="ns=powertrain;MotorSpeedMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6775", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6776",
    browseName="ns=powertrain;MotorTorqueMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6777", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6778",
    browseName="ns=powertrain;MotorWindingType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6779", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6780", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5086",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6781", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
powertrain_objtypes.PtMotorRotaryRatedAttributesType(
    nodeId="ns=powertrain;i=5085",
    browseName="ns=powertrain;<PtMotorRotaryRatedAttributes>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=powertrain;i=5086"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6774"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6776"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6778"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetMotorRotaryType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5085"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6782",
    browseName="ns=powertrain;MotorSpeedMax",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6783", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6784",
    browseName="ns=powertrain;MotorWindingType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6785", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6786", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5090",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6787", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
powertrain_objtypes.PtMotorLinearRatedAttributesType(
    nodeId="ns=powertrain;i=5089",
    browseName="ns=powertrain;<PtMotorLinearRatedAttributes>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=5090"]), o6.hasComponent(o6.ns["ns=powertrain;i=6782"]), o6.hasComponent(o6.ns["ns=powertrain;i=6784"])],
)
o6.reference(powertrain_objtypes.PtAssetMotorLinearType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5089"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=6788",
    browseName="ns=powertrain;Inductance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6789", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
)
powertrain_objtypes.PtReactorAttributesType(
    nodeId="ns=powertrain;i=5127",
    browseName="ns=powertrain;<PtOutputReactorAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6788"])],
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5127"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=powertrain;i=6790",
    browseName="ns=powertrain;OutputFilterType",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6791", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6792", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.UInt16,
)
powertrain_objtypes.PtOutputFilterAttributesType(
    nodeId="ns=powertrain;i=5129",
    browseName="ns=powertrain;<PtOutputFilterAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6790"])],
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5129"])
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5130",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6793", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5130"])
powertrain_objtypes.PtOutputInterfaceAttributesType(
    nodeId="ns=powertrain;i=5131",
    browseName="ns=powertrain;<PtOutputInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6794", browseName="ns=powertrain;NumberOfOutputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5131"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=powertrain;i=6795",
    browseName="ns=powertrain;DcBusVoltageRange",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6796", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
)
powertrain_objtypes.PtDcBusAttributesType(
    nodeId="ns=powertrain;i=5133", browseName="ns=powertrain;PtDcBusAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6795"])]
)
o6.reference(powertrain_objtypes.PtAssetDriveType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=5133"])
powertrain_objtypes.PtBrakeAttributesType(
    nodeId="ns=powertrain;i=15091",
    browseName="ns=powertrain;PtBrakeAttributes",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6072", browseName="ns=powertrain;BrakeCoolingMethod", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6073", browseName="ns=powertrain;BrakeDutyType", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6074", browseName="ns=powertrain;BrakeEmergencySwitchOffCount", dataType=o6.Int16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6077", browseName="ns=powertrain;SafetyPropertySupported", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6088", browseName="ns=powertrain;BrakeVoltageType", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6089", browseName="ns=powertrain;BrakeWireTerminalCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=powertrain;i=6075"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6078"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6080"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6083"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6090"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6537"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6540"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetMotorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15091"])
powertrain_objtypes.PtTemperatureSensorAttributesType(
    nodeId="ns=powertrain;i=15092",
    browseName="ns=powertrain;PtTemperatureSensorAttributes",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6118", browseName="ns=powertrain;TemperatureSensorType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=powertrain;i=6114"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6116"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6170"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetMotorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15092"])
powertrain_objtypes.PtVibrationSensorAttributesType(
    nodeId="ns=powertrain;i=15093",
    browseName="ns=powertrain;PtVibrationSensorAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6123"]), o6.hasComponent(o6.ns["ns=powertrain;i=6139"])],
)
o6.reference(powertrain_objtypes.PtAssetMotorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15093"])
powertrain_objtypes.PtBrakeAttributesType(
    nodeId="ns=powertrain;i=15121",
    browseName="ns=powertrain;PtBrakeAttributes",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6053", browseName="ns=powertrain;BrakeCoolingMethod", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6126", browseName="ns=powertrain;BrakeDutyType", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6127", browseName="ns=powertrain;BrakeEmergencySwitchOffCount", dataType=o6.Int16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6130", browseName="ns=powertrain;SafetyPropertySupported", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6141", browseName="ns=powertrain;BrakeVoltageType", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6142", browseName="ns=powertrain;BrakeWireTerminalCount", dataType=o6.Int16)),
        o6.hasComponent(o6.ns["ns=powertrain;i=6128"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6131"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6133"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6136"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6143"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6543"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6546"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetBrakeType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15121"])
powertrain_objtypes.PtTemperatureSensorAttributesType(
    nodeId="ns=powertrain;i=15128",
    browseName="ns=powertrain;PtTemperatureSensorAttributes",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6175", browseName="ns=powertrain;TemperatureSensorType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=powertrain;i=6171"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6173"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6497"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetGearType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15128"])
powertrain_objtypes.PtVibrationSensorAttributesType(
    nodeId="ns=powertrain;i=15129",
    browseName="ns=powertrain;PtVibrationSensorAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6176"]), o6.hasComponent(o6.ns["ns=powertrain;i=6178"])],
)
o6.reference(powertrain_objtypes.PtAssetGearType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15129"])
powertrain_objtypes.PtTemperatureSensorAttributesType(
    nodeId="ns=powertrain;i=15135",
    browseName="ns=powertrain;PtTemperatureSensorAttributes",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6188", browseName="ns=powertrain;TemperatureSensorType", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=powertrain;i=6184"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6186"]),
        o6.hasComponent(o6.ns["ns=powertrain;i=6556"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetTemperatureSensorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15135"])
powertrain_objtypes.PtVibrationSensorAttributesType(
    nodeId="ns=powertrain;i=15141",
    browseName="ns=powertrain;PtVibrationSensorAttributes",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6180"]), o6.hasComponent(o6.ns["ns=powertrain;i=6189"])],
)
o6.reference(powertrain_objtypes.PtAssetVibrationSensorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15141"])
powertrain_objtypes.PtDcBusAttributesType(
    nodeId="ns=powertrain;i=15155",
    browseName="ns=powertrain;PtDcBusAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6233"]), o6.hasComponent(o6.ns["ns=powertrain;i=6235"])],
)
o6.reference(powertrain_objtypes.PtAssetElectricalBrakingModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15155"])
powertrain_objtypes.PtInputConverterAttributesType(
    nodeId="ns=powertrain;i=15173", browseName="ns=powertrain;PtInputConverterAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6581"])]
)
o6.reference(powertrain_objtypes.PtAssetInputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15173"])
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=15174",
    browseName="ns=powertrain;<PtInputInterfaceAttributes>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6228", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetInputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15174"])
powertrain_objtypes.PtDcBusAttributesType(
    nodeId="ns=powertrain;i=15175",
    browseName="ns=powertrain;PtDcBusAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6294"]), o6.hasComponent(o6.ns["ns=powertrain;i=6296"])],
)
o6.reference(powertrain_objtypes.PtAssetInputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15175"])
powertrain_objtypes.PtInputFilterAttributesType(
    nodeId="ns=powertrain;i=15178", browseName="ns=powertrain;PtInputFilterAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6227"])]
)
o6.reference(powertrain_objtypes.PtAssetInputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15178"])
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=15181",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6626"])],
)
o6.reference(powertrain_objtypes.PtAssetInputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15181"])
powertrain_objtypes.PtOutputConverterAttributesType(
    nodeId="ns=powertrain;i=15187",
    browseName="ns=powertrain;<PtOutputConverterAttributes>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6307"])],
)
o6.reference(powertrain_objtypes.PtAssetOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15187"])
powertrain_objtypes.PtOutputInterfaceAttributesType(
    nodeId="ns=powertrain;i=15188",
    browseName="ns=powertrain;PtOutputInterfaceAttributes",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6242", browseName="ns=powertrain;NumberOfOutputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15188"])
powertrain_objtypes.PtDcBusAttributesType(
    nodeId="ns=powertrain;i=15189",
    browseName="ns=powertrain;PtDcBusAttributes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6337"]), o6.hasComponent(o6.ns["ns=powertrain;i=6339"])],
)
o6.reference(powertrain_objtypes.PtAssetOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15189"])
powertrain_objtypes.PtOutputFilterAttributesType(
    nodeId="ns=powertrain;i=15192",
    browseName="ns=powertrain;<PtOutputFilterAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6240"]), o6.hasComponent(o6.ns["ns=powertrain;i=6319"])],
)
o6.reference(powertrain_objtypes.PtAssetOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15192"])
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=15195",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6629"])],
)
o6.reference(powertrain_objtypes.PtAssetOutputConverterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15195"])
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=15202",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=15240", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetInputFilterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15202"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=15311",
    browseName="ns=powertrain;OutputFilterPowerLoss",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=15316", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
powertrain_objtypes.PtOutputFilterAttributesType(
    nodeId="ns=powertrain;i=15308",
    browseName="ns=powertrain;PtOutputFilterAttributes",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6503"]), o6.hasComponent(o6.ns["ns=powertrain;i=15311"])],
)
o6.reference(powertrain_objtypes.PtAssetOutputFilterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15308"])
powertrain_objtypes.PtOutputInterfaceAttributesType(
    nodeId="ns=powertrain;i=15317",
    browseName="ns=powertrain;PtOutputInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=15367", browseName="ns=powertrain;NumberOfOutputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetOutputFilterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15317"])
powertrain_objtypes.PtOutputInterfaceAttributesType(
    nodeId="ns=powertrain;i=15379",
    browseName="ns=powertrain;PtOutputInterfaceAttributes",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=15429", browseName="ns=powertrain;NumberOfOutputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtAssetOutputReactorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15379"])
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=15435",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6632"])],
)
o6.reference(powertrain_objtypes.PtAssetCommunicationModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15435"])
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=15452",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6635"])],
)
o6.reference(powertrain_objtypes.PtAssetControlModuleType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15452"])
powertrain_objtypes.PtCoolingAttributesType(
    nodeId="ns=powertrain;i=15546",
    browseName="ns=powertrain;<PtCoolingAttributes>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6405",
                browseName="DefaultInstanceBrowseName",
                dataType=o6.QualifiedName,
                value=o6.QualifiedName("PtAssetCooling_01"),
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(powertrain_objtypes.PtAssetCoolingType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15546"])
powertrain_objtypes.PtContactorAttributesType(
    nodeId="ns=powertrain;i=15554",
    browseName="ns=powertrain;PtContactorAttributes",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6391", browseName="ns=powertrain;NumberofAuxiliaryContactsNC", dataType=o6.UInt16, value=0)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6392", browseName="ns=powertrain;NumberofAuxiliaryContactsNO", dataType=o6.UInt16, value=0)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6506", browseName="ns=powertrain;ControlVoltageAC50HzRangeRated", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6591", browseName="ns=powertrain;OperationalCurrentAC3At400VRated", dataType=o6.Float)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=15557", browseName="ns=powertrain;NumberofMainContactsNO", dataType=o6.UInt16)),
    ],
)
o6.reference(powertrain_objtypes.PtAssetContactorType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15554"])
powertrain_objtypes.PtMotorStarterAttributesType(
    nodeId="ns=powertrain;i=15566",
    browseName="ns=powertrain;PtMotorStarterAttributes",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6507", browseName="ns=powertrain;OverloadCurrentSettingRange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6595", browseName="ns=powertrain;OperationalCurrentAC3At400VRated", dataType=o6.Float, value=0.0)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6600", browseName="ns=powertrain;NumberofMainContactsNO", dataType=o6.UInt16, value=0)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=powertrain;i=6601", browseName="ns=powertrain;ControlVoltageAC50HzRangeRated", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6602", browseName="ns=powertrain;NumberofAuxiliaryContactsNO", dataType=o6.UInt16, value=0)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6603", browseName="ns=powertrain;NumberofAuxiliaryContactsNC", dataType=o6.UInt16, value=0)),
        o6.hasComponent(o6.ns["ns=powertrain;i=6592"]),
    ],
)
o6.reference(powertrain_objtypes.PtAssetMotorStarterType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=15566"])
powertrain_objtypes.PtCommunicationInterfaceAttributesType(
    nodeId="ns=powertrain;i=16161",
    browseName="ns=powertrain;<PtCommunicationInterfaceAttributes>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=powertrain;i=6641"])],
)
o6.reference(powertrain_objtypes.PtAssetEncoderType, powertrain_reftypes.HasPtAttributes, o6.ns["ns=powertrain;i=16161"])
powertrain_objtypes.PtInputInterfaceAttributesType(
    nodeId="ns=powertrain;i=16401",
    browseName="ns=powertrain;PtInputInterfaceAttributes",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16439", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte))],
)
o6.reference(powertrain_objtypes.PtMotorRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16401"])
powertrain_objtypes.PtMotorDutyAttributesType(
    nodeId="ns=powertrain;i=16440", browseName="ns=powertrain;PtMotorDutyAttributes", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=powertrain;i=6384"])]
)
o6.reference(powertrain_objtypes.PtMotorRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16440"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16444",
    browseName="ns=powertrain;MotorCurrentContinuousStall",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16449", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16444"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16492",
    browseName="ns=powertrain;MotorPowerFactor",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16497", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtMotorRatedAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16492"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16505",
    browseName="ns=powertrain;<GearRatio>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6331", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16505"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16507",
    browseName="ns=powertrain;Backlash",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6332", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16507"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16508",
    browseName="ns=powertrain;TorsionalRigidity",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16513", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16508"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16514",
    browseName="ns=powertrain;GearInertia",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16519", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16514"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16520",
    browseName="ns=powertrain;TorqueRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16525", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16520"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16526",
    browseName="ns=powertrain;SpeedRated",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16531", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16526"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16538",
    browseName="ns=powertrain;AxialForceMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16543", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16538"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16544",
    browseName="ns=powertrain;<Efficiency>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16549", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtGearAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16544"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16613",
    browseName="ns=powertrain;B10dValue",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16618", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt32,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16613"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16619",
    browseName="ns=powertrain;BrakingEnergySingleEngagementMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16624", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16619"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16631",
    browseName="ns=powertrain;BrakeAccelerationVoltage",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16636", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16631"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16637",
    browseName="ns=powertrain;BrakeHoldingVoltage",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16642", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16637"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16655",
    browseName="ns=powertrain;BrakeTurnOnDelay",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16660", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16655"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16661",
    browseName="ns=powertrain;BrakeTurnOffDelayAC",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16666", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16661"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16667",
    browseName="ns=powertrain;BrakeTurnOffDelayDC",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16672", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16667"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16691",
    browseName="ns=powertrain;BrakeInertia",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16696", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16691"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16697",
    browseName="ns=powertrain;BrakeWearMaximum",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16702", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtBrakeAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16697"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16723",
    browseName="ns=powertrain;Accuracy",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16728", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtTemperatureSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16723"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16729",
    browseName="ns=powertrain;TemperatureMin",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16734", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtTemperatureSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16729"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16735",
    browseName="ns=powertrain;TemperatureMax",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16740", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtTemperatureSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16735"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16766",
    browseName="ns=powertrain;Accuracy",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16771", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16766"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16772",
    browseName="ns=powertrain;Linearity",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16777", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtVibrationSensorAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16772"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16829",
    browseName="ns=powertrain;LineFilterPowerLoss",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16834", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputFilterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16829"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16841",
    browseName="ns=powertrain;OutputFilterPowerLoss",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16846", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputFilterAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16841"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16912",
    browseName="ns=powertrain;InternalResistance",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6408", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAnalogInputElectricalAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16912"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16916",
    browseName="ns=powertrain;LoadResistance",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16921", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAnalogOutputElectricalAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16916"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16930",
    browseName="ns=powertrain;SupplyVoltageDc",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16935", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAuxiliarySupplyAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16930"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16936",
    browseName="ns=powertrain;SupplyVoltageAc",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16941", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAuxiliarySupplyAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16936"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16942",
    browseName="ns=powertrain;CurrentMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16947", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAuxiliarySupplyAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16942"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16948",
    browseName="ns=powertrain;PowerConsumptionMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16953", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAuxiliarySupplyAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16948"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16954",
    browseName="ns=powertrain;FuseProtectionCurrentMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16959", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtAuxiliarySupplyAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16954"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16975",
    browseName="ns=powertrain;Length",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16980", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtHardwareAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16975"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16981",
    browseName="ns=powertrain;Width",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16986", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtHardwareAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16981"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16987",
    browseName="ns=powertrain;Height",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16992", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtHardwareAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16987"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=16993",
    browseName="ns=powertrain;Weight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16998", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtHardwareAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=16993"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=17060",
    browseName="ns=powertrain;InputCurrentMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17065", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=17060"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=17072",
    browseName="ns=powertrain;InputPowerMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17077", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtInputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=17072"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=17087",
    browseName="ns=powertrain;OutputVoltageMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17092", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=17087"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=17099",
    browseName="ns=powertrain;OutputFrequencyMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17104", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=17099"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=17111",
    browseName="ns=powertrain;OutputCurrentMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17116", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=17111"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=powertrain;i=17123",
    browseName="ns=powertrain;OutputPowerMax",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17128", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(powertrain_objtypes.PtOutputInterfaceAttributesType, ns0.reftypes.HasComponent, o6.ns["ns=powertrain;i=17123"])


del Any, TYPE_CHECKING, uuid, o6, di, fx_ac, fx_data, ia, irdi_v1_0_0, machinery, ns0, powertrain_reftypes, powertrain_objtypes
