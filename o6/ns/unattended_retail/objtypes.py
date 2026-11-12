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

"""Generated OPC UA unattended_retail namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as unattended_retail_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=unattended_retail;i=1016", browseName="ns=unattended_retail;ConfigurationChangedEventType", displayName="ConfigurationChangedEventType", isAbstract=True)
class ConfigurationChangedEventType(ns0.objtypes.BaseEventType):
    pass


@o6.objecttype(nodeId="ns=unattended_retail;i=1021", browseName="ns=unattended_retail;PaymentModesType", displayName="PaymentModesType")
class PaymentModesType(ns0.objtypes.BaseObjectType):
    paymentMode_: PaymentModeType


@o6.objecttype(nodeId="ns=unattended_retail;i=1022", browseName="ns=unattended_retail;PaymentDevicesType", displayName="PaymentDevicesType")
class PaymentDevicesType(ns0.objtypes.BaseObjectType):
    paymentDevice_: PaymentDeviceType


@o6.objecttype(nodeId="ns=unattended_retail;i=1019", browseName="ns=unattended_retail;BaseComponentsType", displayName="BaseComponentsType")
class BaseComponentsType(ns0.objtypes.FolderType):
    component_: ns0.objtypes.BaseObjectType | None = o6.hasComponent(
        ns0.objtypes.BaseObjectType(nodeId="ns=unattended_retail;i=5040", browseName="ns=unattended_retail;<Component>", modellingRule="OptionalPlaceholder")
    )


@o6.objecttype(nodeId="ns=unattended_retail;i=1003", browseName="ns=unattended_retail;MachineEngineType", displayName="MachineEngineType")
class MachineEngineType(ns0.objtypes.BaseObjectType):
    capabilities: MachineEngineCapabilitiesType
    components: BaseComponentsType | None = o6.hasComponent(BaseComponentsType(nodeId="ns=unattended_retail;i=5041", browseName="ns=unattended_retail;Components"))
    configuration: BaseConfigurationType
    delivery: MachineEngineDeliveryType
    identification: IdentificationType
    status: MachineEngineStatusType


o6.reference(MachineEngineType, "i=41", ConfigurationChangedEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1005", browseName="ns=unattended_retail;PaymentServiceType", displayName="PaymentServiceType")
class PaymentServiceType(ns0.objtypes.BaseObjectType):
    components: BaseComponentsType | None = o6.hasComponent(BaseComponentsType(nodeId="ns=unattended_retail;i=5074", browseName="ns=unattended_retail;Components"))
    configuration: BaseConfigurationType
    delivery: PaymentServiceDeliveryType
    identification: IdentificationType
    paymentDevices: PaymentDevicesType | None
    paymentModes: PaymentModesType | None
    priceInformation: PriceInformationType
    status: PaymentServiceStatusType


o6.reference(PaymentServiceType, "i=41", ConfigurationChangedEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1004", browseName="ns=unattended_retail;UIType", displayName="UIType")
class UIType(ns0.objtypes.BaseObjectType):
    components: BaseComponentsType | None = o6.hasComponent(BaseComponentsType(nodeId="ns=unattended_retail;i=5080", browseName="ns=unattended_retail;Components"))
    configuration: BaseConfigurationType
    identification: IdentificationType


o6.reference(UIType, "i=41", ConfigurationChangedEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1009", browseName="ns=unattended_retail;MachineEngineCapabilitiesType", displayName="MachineEngineCapabilitiesType")
class MachineEngineCapabilitiesType(ns0.objtypes.BaseObjectType):
    options: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6045",
            browseName="ns=unattended_retail;Options",
            dataType=unattended_retail_datypes.OptionDescriptionDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    outputIds: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6002", browseName="ns=unattended_retail;OutputIds", dataType=o6.UInt16, valueRank=1, arrayDimensions=[0])
    )
    selectionList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6017",
            browseName="ns=unattended_retail;SelectionList",
            dataType=unattended_retail_datypes.SelectionDescriptionDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    selectionListVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6049", browseName="ns=unattended_retail;SelectionListVersion", dataType=ns0.datatypes.SemanticVersionString)
    )


@o6.objecttype(
    nodeId="ns=unattended_retail;i=1008", browseName="ns=unattended_retail;IdentificationType", displayName="IdentificationType", interfaces=[di.objtypes.IVendorNameplateType]
)
class IdentificationType(di.objtypes.FunctionalGroupType):
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6011", browseName="ns=di;DeviceClass", dataType=o6.String)
    )
    deviceManual: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6010", browseName="ns=di;DeviceManual", dataType=o6.String)
    )
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6009", browseName="ns=di;DeviceRevision", dataType=o6.String)
    )
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6007", browseName="ns=di;HardwareRevision", dataType=o6.String)
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6001", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)
    )
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6003", browseName="ns=di;ManufacturerUri", dataType=o6.String)
    )
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6005", browseName="ns=di;Model", dataType=o6.LocalizedText))
    patchIdentifiers: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6098", browseName="ns=di;PatchIdentifiers", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    productCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6006", browseName="ns=di;ProductCode", dataType=o6.String))
    productInstanceUri: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6013", browseName="ns=di;ProductInstanceUri", dataType=o6.String)
    )
    revisionCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6014", browseName="ns=di;RevisionCounter", dataType=o6.Int32)
    )
    serialNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6012", browseName="ns=di;SerialNumber", dataType=o6.String)
    )
    softwareReleaseDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6097", browseName="ns=di;SoftwareReleaseDate", dataType=o6.DateTime)
    )
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6008", browseName="ns=di;SoftwareRevision", dataType=o6.String)
    )


@o6.objecttype(nodeId="ns=unattended_retail;i=1014", browseName="ns=unattended_retail;PriceChangeEventType", displayName="PriceChangeEventType", isAbstract=True)
class PriceChangeEventType(ns0.objtypes.BaseEventType):
    machineEngineProductInstanceUri: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6106", browseName="ns=unattended_retail;MachineEngineProductInstanceUri", dataType=ns0.datatypes.UriString)
    )


@o6.objecttype(nodeId="ns=unattended_retail;i=1015", browseName="ns=unattended_retail;MachineEngineStatusType", displayName="MachineEngineStatusType")
class MachineEngineStatusType(ns0.objtypes.BaseObjectType):
    activeEVADTSStatusCodes: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6158", browseName="ns=unattended_retail;ActiveEVADTSStatusCodes", dataType=o6.String, valueRank=1, arrayDimensions=[0]
        )
    )
    mainColdTemperature: ns0.vartypes.AnalogUnitType | None
    mainHotTemperature: ns0.vartypes.AnalogUnitType | None
    optionIdStatus: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6115",
            browseName="ns=unattended_retail;OptionIdStatus",
            dataType=unattended_retail_datypes.AvailabilityStatusDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    outputStatus: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6004",
            browseName="ns=unattended_retail;OutputStatus",
            dataType=unattended_retail_datypes.OutputStatusDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    selectionIdStatus: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6032",
            browseName="ns=unattended_retail;SelectionIdStatus",
            dataType=unattended_retail_datypes.AvailabilityStatusDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    sensorData_: ns0.vartypes.AnalogUnitType | None
    workingStatus: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6033", browseName="ns=unattended_retail;WorkingStatus", dataType=unattended_retail_datypes.MachineEngineWorkingStatusEnum
        )
    )


@o6.objecttype(nodeId="ns=unattended_retail;i=1006", browseName="ns=unattended_retail;BaseConfigurationType", displayName="BaseConfigurationType")
class BaseConfigurationType(ns0.objtypes.BaseObjectType):
    defaultCurrency: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6199", browseName="ns=unattended_retail;DefaultCurrency", dataType=ns0.datatypes.CurrencyUnitType)
    )
    localTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6015", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType)
    )


@o6.objecttype(nodeId="ns=unattended_retail;i=1011", browseName="ns=unattended_retail;PriceServiceType", displayName="PriceServiceType")
class PriceServiceType(ns0.objtypes.BaseObjectType):
    components: BaseComponentsType | None = o6.hasComponent(BaseComponentsType(nodeId="ns=unattended_retail;i=5081", browseName="ns=unattended_retail;Components"))
    configuration: BaseConfigurationType = o6.hasComponent(BaseConfigurationType(nodeId="ns=unattended_retail;i=5059", browseName="ns=unattended_retail;Configuration"))
    identification: IdentificationType
    priceInformation: PriceInformationType


o6.reference(PriceServiceType, "i=41", ConfigurationChangedEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1026", browseName="ns=unattended_retail;PaymentDeviceType", displayName="PaymentDeviceType")
class PaymentDeviceType(ns0.objtypes.BaseObjectType):
    identification: IdentificationType
    isEmulated: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6200", browseName="ns=unattended_retail;IsEmulated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    slotConfigurationList: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6170",
            browseName="ns=unattended_retail;SlotConfigurationList",
            dataType=unattended_retail_datypes.SlotConfigurationDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    status: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6208",
            browseName="ns=unattended_retail;Status",
            dataType=unattended_retail_datypes.PaymentModeOrDeviceStatusEnum,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    supportedAssetList: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6167",
            browseName="ns=unattended_retail;SupportedAssetList",
            dataType=unattended_retail_datypes.PriceDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    supportedAssetListVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6168", browseName="ns=unattended_retail;SupportedAssetListVersion", dataType=ns0.datatypes.SemanticVersionString)
    )


@o6.objecttype(nodeId="ns=unattended_retail;i=1023", browseName="ns=unattended_retail;StandalonePaymentDeviceType", displayName="StandalonePaymentDeviceType", isAbstract=True)
class StandalonePaymentDeviceType(PaymentDeviceType):
    components: BaseComponentsType | None = o6.hasComponent(BaseComponentsType(nodeId="ns=unattended_retail;i=5086", browseName="ns=unattended_retail;Components"))
    configuration: BaseConfigurationType = o6.hasComponent(BaseConfigurationType(nodeId="ns=unattended_retail;i=5085", browseName="ns=unattended_retail;Configuration"))


o6.reference(StandalonePaymentDeviceType, "i=41", ConfigurationChangedEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1002", browseName="ns=unattended_retail;AuditCollectType", displayName="AuditCollectType")
class AuditCollectType(ns0.objtypes.BaseObjectType):
    components: BaseComponentsType | None = o6.hasComponent(BaseComponentsType(nodeId="ns=unattended_retail;i=5007", browseName="ns=unattended_retail;Components"))
    configuration: BaseConfigurationType = o6.hasComponent(BaseConfigurationType(nodeId="ns=unattended_retail;i=5006", browseName="ns=unattended_retail;Configuration"))
    identification: IdentificationType
    isCollectingAudit: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6245", browseName="ns=unattended_retail;IsCollectingAudit", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )


o6.reference(AuditCollectType, "i=41", ConfigurationChangedEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1013", browseName="ns=unattended_retail;VendingBaseAuditEventType", displayName="VendingBaseAuditEventType", isAbstract=True)
class VendingBaseAuditEventType(ns0.objtypes.BaseEventType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6031", browseName="ns=unattended_retail;Category", dataType=o6.String)
    )
    eVADTSStatusCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6250", browseName="ns=unattended_retail;EVADTSStatusCode", dataType=o6.String)
    )
    eVADTSStatusIsActive: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6251", browseName="ns=unattended_retail;EVADTSStatusIsActive", dataType=o6.Boolean)
    )
    inMaintenanceMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6085", browseName="ns=unattended_retail;InMaintenanceMode", dataType=o6.Boolean)
    )


o6.reference(MachineEngineType, "i=41", VendingBaseAuditEventType)
o6.reference(UIType, "i=41", VendingBaseAuditEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1020", browseName="ns=unattended_retail;VendingAuditEventType", displayName="VendingAuditEventType", isAbstract=True)
class VendingAuditEventType(VendingBaseAuditEventType):
    counter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6084", browseName="ns=unattended_retail;Counter", dataType=o6.UInt32)
    )
    failStatus: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6144", browseName="ns=unattended_retail;FailStatus", dataType=unattended_retail_datypes.DeliveryAndPaymentStatusEnum
        )
    )
    monetaryValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6146", browseName="ns=unattended_retail;MonetaryValue", dataType=unattended_retail_datypes.PriceDataType)
    )
    monetaryValueWithContext: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6086", browseName="ns=unattended_retail;MonetaryValueWithContext", dataType=unattended_retail_datypes.PriceAndContextDataType
        )
    )
    newSlotContent: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6147", browseName="ns=unattended_retail;NewSlotContent", dataType=o6.UInt32)
    )
    nonRefundedValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6246", browseName="ns=unattended_retail;NonRefundedValue", dataType=unattended_retail_datypes.PriceAndContextDataType
        )
    )
    paymentDetails: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6148",
            browseName="ns=unattended_retail;PaymentDetails",
            dataType=unattended_retail_datypes.ActualPaymentDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    paymentMode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6145", browseName="ns=unattended_retail;PaymentMode", dataType=o6.String)
    )
    selection: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6149", browseName="ns=unattended_retail;Selection", dataType=unattended_retail_datypes.SelectionDataType)
    )
    slotIndex: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6150", browseName="ns=unattended_retail;SlotIndex", dataType=o6.Int32)
    )
    userId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6151", browseName="ns=unattended_retail;UserId", dataType=o6.String)
    )


o6.reference(PaymentServiceType, "i=41", VendingAuditEventType)
o6.reference(PaymentDeviceType, "i=41", VendingAuditEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1029", browseName="ns=unattended_retail;VendingBasketAuditEventType", displayName="VendingBasketAuditEventType", isAbstract=True)
class VendingBasketAuditEventType(VendingAuditEventType):
    basketContent: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6247",
            browseName="ns=unattended_retail;BasketContent",
            dataType=unattended_retail_datypes.SelectionDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    monetaryValuePerBasketContent: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6248",
            browseName="ns=unattended_retail;MonetaryValuePerBasketContent",
            dataType=unattended_retail_datypes.PriceAndContextDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    partialSuccessful: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6249", browseName="ns=unattended_retail;PartialSuccessful", dataType=o6.Boolean, valueRank=1, arrayDimensions=[0])
    )


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6019",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="SelectionId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Options", dataType=o6.NodeId("ns=unattended_retail;i=3006"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="TransactionId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6152",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7001",
    browseName="ns=unattended_retail;Deliver",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6019"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6152"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6020",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Selection", dataType=o6.NodeId("ns=unattended_retail;i=3033"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Price", dataType=o6.NodeId("ns=unattended_retail;i=3005"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6057",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="TransactionId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7003",
    browseName="ns=unattended_retail;DeliverRequest",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6020"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6057"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6075",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="MachineEngineProductInstanceUri", dataType=o6.NodeId("i=23751"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="SelectionListVersion", dataType=o6.NodeId("i=24263"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6101",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="PriceInformationList", dataType=o6.NodeId("ns=unattended_retail;i=3027"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7005",
    browseName="ns=unattended_retail;GetPriceForSelections",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6075"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6101"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6102",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Selection", dataType=o6.NodeId("ns=unattended_retail;i=3033"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6103",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="PriceInformation", dataType=o6.NodeId("ns=unattended_retail;i=3014"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7006",
    browseName="ns=unattended_retail;GetPriceForOneSelection",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6102"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6103"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6104",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="BasketContent", dataType=o6.NodeId("ns=unattended_retail;i=3033"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6105",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="OverallPriceInformation", dataType=o6.NodeId("ns=unattended_retail;i=3005"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PriceInformationList", dataType=o6.NodeId("ns=unattended_retail;i=3014"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7007",
    browseName="ns=unattended_retail;GetPriceForBasket",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6104"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6105"]),
)


@o6.objecttype(nodeId="ns=unattended_retail;i=1007", browseName="ns=unattended_retail;PriceInformationType", displayName="PriceInformationType")
class PriceInformationType(ns0.objtypes.BaseObjectType):
    getPriceForBasket: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=unattended_retail;i=7007"])
    getPriceForOneSelection: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7006"])
    getPriceForSelections: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7005"])


o6.reference(PriceInformationType, "i=41", PriceChangeEventType)


@o6.objecttype(nodeId="ns=unattended_retail;i=1018", browseName="ns=unattended_retail;PaymentModeType", displayName="PaymentModeType")
class PaymentModeType(ns0.objtypes.BaseObjectType):
    availableCredit: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=unattended_retail;i=6110", browseName="ns=unattended_retail;AvailableCredit", dataType=unattended_retail_datypes.PriceDataType)
    )
    currentlyUsedUserId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=unattended_retail;i=6109", browseName="ns=unattended_retail;CurrentlyUsedUserId", dataType=o6.String)
    )
    escrowRefund: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=unattended_retail;i=7008", browseName="ns=unattended_retail;EscrowRefund"))
    paymentModeId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=unattended_retail;i=6108", browseName="ns=unattended_retail;PaymentModeId", dataType=o6.String)
    )
    status: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6107", browseName="ns=unattended_retail;Status", dataType=unattended_retail_datypes.PaymentModeOrDeviceStatusEnum
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6114",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestedState", dataType=o6.NodeId("ns=unattended_retail;i=3039"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=unattended_retail;i=7009", browseName="ns=unattended_retail;RequestStatusChange", inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6114"]))


@o6.objecttype(nodeId="ns=unattended_retail;i=1024", browseName="ns=unattended_retail;PaymentServiceStatusType", displayName="PaymentServiceStatusType")
class PaymentServiceStatusType(ns0.objtypes.BaseObjectType):
    requestStatusChange: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7009"])
    status: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6113", browseName="ns=unattended_retail;Status", dataType=unattended_retail_datypes.PaymentServiceStatusEnum
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6131",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="BasketContent", dataType=o6.NodeId("ns=unattended_retail;i=3033"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Price", dataType=o6.NodeId("ns=unattended_retail;i=3005"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6132",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="TransactionIds", dataType=o6.NodeId("i=9"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="BasketId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7015",
    browseName="ns=unattended_retail;DeliverBasketRequest",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6131"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6132"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6154",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TransactionId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6156",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7016",
    browseName="ns=unattended_retail;StopDelivery",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6154"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6156"]),
)


@o6.objecttype(nodeId="ns=unattended_retail;i=1012", browseName="ns=unattended_retail;MachineEngineDeliveryType", displayName="MachineEngineDeliveryType")
class MachineEngineDeliveryType(ns0.objtypes.BaseObjectType):
    deliver: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7001"])
    deliveryProgress: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6037",
            browseName="ns=unattended_retail;DeliveryProgress",
            dataType=unattended_retail_datypes.DeliveryProgressDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    deliveryRequests: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6064",
            browseName="ns=unattended_retail;DeliveryRequests",
            dataType=unattended_retail_datypes.DeliveryRequestDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    stopDelivery: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7016"])


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6160",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TransactionId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6161",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7018",
    browseName="ns=unattended_retail;CancelDeliverRequest",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6160"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6161"]),
)


@o6.objecttype(nodeId="ns=unattended_retail;i=1010", browseName="ns=unattended_retail;PaymentServiceDeliveryType", displayName="PaymentServiceDeliveryType")
class PaymentServiceDeliveryType(ns0.objtypes.BaseObjectType):
    cancelDeliverRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7018"])
    deliverRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7003"])
    transactionProgress: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6062",
            browseName="ns=unattended_retail;TransactionProgress",
            dataType=unattended_retail_datypes.TransactionProgressDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6164",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BasketId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6165",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7020",
    browseName="ns=unattended_retail;CancelDeliverBasketRequest",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6164"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6165"]),
)


@o6.objecttype(nodeId="ns=unattended_retail;i=1017", browseName="ns=unattended_retail;PaymentServiceBasketDeliveryType", displayName="PaymentServiceBasketDeliveryType")
class PaymentServiceBasketDeliveryType(PaymentServiceDeliveryType):
    basketProgress: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6130",
            browseName="ns=unattended_retail;BasketProgress",
            dataType=unattended_retail_datypes.BasketProgressDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    cancelDeliverBasketRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7020"])
    deliverBasketRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7015"])


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6218",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="NewAssetConfigurationList", dataType=o6.NodeId("ns=unattended_retail;i=3007"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6219",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7021",
    browseName="ns=unattended_retail;ChangeAssetConfigurationList",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6218"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6219"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6220",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="PayoutValue", dataType=o6.NodeId("ns=unattended_retail;i=3005"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6221",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7022",
    browseName="ns=unattended_retail;PayoutByValue",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6220"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6221"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6222",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfAssetsBySupportedAssetList", dataType=o6.NodeId("i=7"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6223",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7023",
    browseName="ns=unattended_retail;PayoutBySupportedAssetList",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6222"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6223"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6224",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ValueToConsume", dataType=o6.NodeId("ns=unattended_retail;i=3005"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6225",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7024",
    browseName="ns=unattended_retail;ConsumeAvailableValue",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6224"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6225"]),
)


@o6.objecttype(nodeId="ns=unattended_retail;i=1028", browseName="ns=unattended_retail;PaymentCashDeviceType", displayName="PaymentCashDeviceType", isAbstract=True)
class PaymentCashDeviceType(StandalonePaymentDeviceType):
    assetConfigurationList: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6215",
            browseName="ns=unattended_retail;AssetConfigurationList",
            dataType=unattended_retail_datypes.AssetConfigurationEnum,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    changeAssetConfigurationList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7021"])
    consumeAvailableValue: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7024"])
    currentAvailableValue: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6217",
            browseName="ns=unattended_retail;CurrentAvailableValue",
            dataType=unattended_retail_datypes.PriceDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    currentSlotContentList: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6214",
            browseName="ns=unattended_retail;CurrentSlotContentList",
            dataType=o6.UInt32,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    payoutBySupportedAssetList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=unattended_retail;i=7023"])
    payoutByValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=unattended_retail;i=7022"])
    payoutStatus: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6216",
            browseName="ns=unattended_retail;PayoutStatus",
            dataType=unattended_retail_datypes.PayoutStatusEnum,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    slotConfigurationList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6211",
            browseName="ns=unattended_retail;SlotConfigurationList",
            dataType=unattended_retail_datypes.SlotConfigurationDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    supportedAssetList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6212",
            browseName="ns=unattended_retail;SupportedAssetList",
            dataType=unattended_retail_datypes.PriceDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    supportedAssetListVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6213", browseName="ns=unattended_retail;SupportedAssetListVersion", dataType=ns0.datatypes.SemanticVersionString)
    )


@o6.objecttype(nodeId="ns=unattended_retail;i=1034", browseName="ns=unattended_retail;PaymentCoinDeviceType", displayName="PaymentCoinDeviceType")
class PaymentCoinDeviceType(PaymentCashDeviceType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6227",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=unattended_retail;i=7025", browseName="ns=unattended_retail;CancelPayout", outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6227"]))

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6228",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AcceptBill", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6229",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7026",
    browseName="ns=unattended_retail;HandleBillFromEscrow",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6228"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6229"]),
)


@o6.objecttype(nodeId="ns=unattended_retail;i=1031", browseName="ns=unattended_retail;PaymentBillDeviceType", displayName="PaymentBillDeviceType")
class PaymentBillDeviceType(PaymentCashDeviceType):
    cancelPayout: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7025"])
    currentValueInEscrow: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6226", browseName="ns=unattended_retail;CurrentValueInEscrow", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1
        )
    )
    handleBillFromEscrow: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7026"])


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6237",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Value", dataType=o6.NodeId("ns=unattended_retail;i=3005"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Selection", dataType=o6.NodeId("ns=unattended_retail;i=3033"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6238",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7027",
    browseName="ns=unattended_retail;Approve",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6237"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6238"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6239",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=unattended_retail;i=7028", browseName="ns=unattended_retail;CancelApproval", outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6239"]))

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6240",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Value", dataType=o6.NodeId("ns=unattended_retail;i=3005"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6241",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7029",
    browseName="ns=unattended_retail;Recharge",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6240"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6241"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6243",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Enable", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6244",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7030",
    browseName="ns=unattended_retail;EnableOrDisable",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6243"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6244"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6242",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=unattended_retail;i=7031", browseName="ns=unattended_retail;RefundLast", outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6242"]))


@o6.objecttype(nodeId="ns=unattended_retail;i=1037", browseName="ns=unattended_retail;PaymentCashlessDeviceType", displayName="PaymentCashlessDeviceType")
class PaymentCashlessDeviceType(StandalonePaymentDeviceType):
    approve: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7027"])
    approveStatus: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6233",
            browseName="ns=unattended_retail;ApproveStatus",
            dataType=unattended_retail_datypes.OperationStatusEnum,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    cancelApproval: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7028"])
    currentContentOnCard: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6232",
            browseName="ns=unattended_retail;CurrentContentOnCard",
            dataType=unattended_retail_datypes.PriceDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    enableOrDisable: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7030"])
    isEnabled: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=unattended_retail;i=6236", browseName="ns=unattended_retail;IsEnabled", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    maxRecharge: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=unattended_retail;i=6231", browseName="ns=unattended_retail;MaxRecharge", dataType=unattended_retail_datypes.PriceDataType, accessLevel=3, userAccessLevel=1
        )
    )
    recharge: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=unattended_retail;i=7029"])
    rechargeStatus: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6234",
            browseName="ns=unattended_retail;RechargeStatus",
            dataType=unattended_retail_datypes.OperationStatusEnum,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    refundLast: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=unattended_retail;i=7031"])
    refundLastStatus: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=unattended_retail;i=6235",
            browseName="ns=unattended_retail;RefundLastStatus",
            dataType=unattended_retail_datypes.OperationStatusEnum,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    userId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=unattended_retail;i=6230", browseName="ns=unattended_retail;UserId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, unattended_retail_datypes
