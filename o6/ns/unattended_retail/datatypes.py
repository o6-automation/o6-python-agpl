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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=unattended_retail;i=3003", browseName="OptionDescriptionDataType", defaultEncodingId="ns=unattended_retail;i=5009")
class OptionDescriptionDataType(ns0.datatypes.Structure):
    optionId: o6.String
    range: ns0.datatypes.Range
    step: o6.Double
    default: o6.Double
    engineeringUnit: ns0.datatypes.EUInformation


@o6.enumtype(nodeId="ns=unattended_retail;i=3004", browseName="AvailabilityEnum")
class AvailabilityEnum(ns0.datatypes.Enumeration):
    AVAILABLE = o6.enumfield(0, name="Available")
    OUT_OF_ORDER = o6.enumfield(1, name="OutOfOrder")
    TEMPORARY_NOT_AVAILABLE = o6.enumfield(2, name="TemporaryNotAvailable")
    EMPTY = o6.enumfield(3, name="Empty")


@o6.datatype(nodeId="ns=unattended_retail;i=3005", browseName="PriceDataType", defaultEncodingId="ns=unattended_retail;i=5017")
class PriceDataType(ns0.datatypes.Structure):
    amount: o6.UInt32
    currency: ns0.datatypes.CurrencyUnitType


@o6.datatype(nodeId="ns=unattended_retail;i=3006", browseName="OptionSelectionDataType", defaultEncodingId="ns=unattended_retail;i=5023")
class OptionSelectionDataType(ns0.datatypes.Structure):
    optionId: o6.String
    value: o6.Double


@o6.enumtype(nodeId="ns=unattended_retail;i=3007", browseName="AssetConfigurationEnum")
class AssetConfigurationEnum(ns0.datatypes.Enumeration):
    ACCEPT_TO_CASHBOX_OR_STACKER = o6.enumfield(0, name="AcceptToCashboxOrStacker")
    ACCEPT_TO_RECYCLER_OR_TUBE = o6.enumfield(1, name="AcceptToRecyclerOrTube")
    ACCEPT_TO_ESCROW_AND_STACKER = o6.enumfield(2, name="AcceptToEscrowAndStacker")
    ACCEPT_TO_ESCROW_AND_RECYCLER = o6.enumfield(3, name="AcceptToEscrowAndRecycler")
    REJECT = o6.enumfield(4, name="Reject")


@o6.datatype(nodeId="ns=unattended_retail;i=3008", browseName="SelectionDescriptionDataType", defaultEncodingId="ns=unattended_retail;i=5012")
class SelectionDescriptionDataType(ns0.datatypes.Structure):
    selectionId: o6.String
    availableOptionIds: list[o6.String] = o6.field(arrayDimensions=[0])
    isStoppable: o6.Boolean


@o6.datatype(nodeId="ns=unattended_retail;i=3009", browseName="DeliveryRequestDataType", defaultEncodingId="ns=unattended_retail;i=5020")
class DeliveryRequestDataType(ns0.datatypes.Structure):
    transactionId: o6.UInt64
    selectionId: o6.String
    options: list[OptionSelectionDataType] = o6.field(arrayDimensions=[0])


@o6.enumtype(nodeId="ns=unattended_retail;i=3010", browseName="MachineEngineWorkingStatusEnum")
class MachineEngineWorkingStatusEnum(ns0.datatypes.Enumeration):
    INITIALIZING = o6.enumfield(0, name="Initializing")
    WAITING_FOR_TEMPERATURE = o6.enumfield(1, name="WaitingForTemperature")
    READY = o6.enumfield(2, name="Ready")
    CLEANING = o6.enumfield(3, name="Cleaning")
    DISPENSING = o6.enumfield(4, name="Dispensing")
    BUSY = o6.enumfield(5, name="Busy")
    OUT_OF_ORDER = o6.enumfield(6, name="OutOfOrder")
    ENERGY_SAVING_MODE = o6.enumfield(7, name="EnergySavingMode")


@o6.enumtype(nodeId="ns=unattended_retail;i=3012", browseName="OutputStatusEnum")
class OutputStatusEnum(ns0.datatypes.Enumeration):
    FREE = o6.enumfield(0, name="Free")
    PRODUCT_NOT_TAKEN = o6.enumfield(1, name="ProductNotTaken")
    OUT_OF_ORDER = o6.enumfield(2, name="OutOfOrder")
    LOCKED = o6.enumfield(3, name="Locked")
    CLEANING_REQUIRED = o6.enumfield(4, name="CleaningRequired")
    VENDOR_SPECIFIC = o6.enumfield(5, name="VendorSpecific")


@o6.datatype(nodeId="ns=unattended_retail;i=3014", browseName="PriceAndContextDataType", defaultEncodingId="ns=unattended_retail;i=5065")
class PriceAndContextDataType(PriceDataType):
    amount: o6.UInt32
    currency: ns0.datatypes.CurrencyUnitType
    priceListId: o6.String
    tax: o6.Double
    discountSurcharge: o6.Int32


@o6.enumtype(nodeId="ns=unattended_retail;i=3015", browseName="DeliveryStatusEnum")
class DeliveryStatusEnum(ns0.datatypes.Enumeration):
    READY_TO_DELIVER = o6.enumfield(0, name="ReadyToDeliver")
    DELIVERY_STARTED = o6.enumfield(1, name="DeliveryStarted")
    DELIVERY_FINISHED = o6.enumfield(2, name="DeliveryFinished")
    DELIVERY_FAILED = o6.enumfield(3, name="DeliveryFailed")
    DELIVERY_CANNOT_START = o6.enumfield(4, name="DeliveryCannotStart")


@o6.datatype(nodeId="ns=unattended_retail;i=3011", browseName="OutputDeliveryStatusDataType", defaultEncodingId="ns=unattended_retail;i=5031")
class OutputDeliveryStatusDataType(ns0.datatypes.Structure):
    status: DeliveryStatusEnum
    outputId: o6.UInt16


@o6.datatype(nodeId="ns=unattended_retail;i=3013", browseName="DeliveryProgressDataType", defaultEncodingId="ns=unattended_retail;i=5026")
class DeliveryProgressDataType(ns0.datatypes.Structure):
    progressInPercent: o6.Byte
    status: list[OutputDeliveryStatusDataType] = o6.field(arrayDimensions=[0])
    transactionId: o6.UInt64


@o6.datatype(nodeId="ns=unattended_retail;i=3017", browseName="OutputStatusDataType", defaultEncodingId="ns=unattended_retail;i=5034")
class OutputStatusDataType(ns0.datatypes.Structure):
    outputId: o6.UInt16
    status: OutputStatusEnum
    vendorStatus: o6.Int32


@o6.datatype(nodeId="ns=unattended_retail;i=3020", browseName="AvailabilityStatusDataType", defaultEncodingId="ns=unattended_retail;i=5037")
class AvailabilityStatusDataType(ns0.datatypes.Structure):
    id: o6.String
    status: AvailabilityEnum
    estimatedRemainingStock: o6.UInt32


@o6.datatype(nodeId="ns=unattended_retail;i=3021", browseName="SlotConfigurationDataType", defaultEncodingId="ns=unattended_retail;i=5082")
class SlotConfigurationDataType(ns0.datatypes.Structure):
    slotIndex: o6.Int32
    supportedAssetListIndex: o6.UInt32


@o6.datatype(nodeId="ns=unattended_retail;i=3025", browseName="ActualPaymentDataType", defaultEncodingId="ns=unattended_retail;i=5071")
class ActualPaymentDataType(ns0.datatypes.Structure):
    paymentMode: o6.String
    paymentDevice: o6.String
    userId: o6.String
    monetaryValue: PriceDataType


@o6.enumtype(nodeId="ns=unattended_retail;i=3026", browseName="DeliveryAndPaymentStatusEnum")
class DeliveryAndPaymentStatusEnum(ns0.datatypes.Enumeration):
    DELIVERY_REQUEST_RECEIVED = o6.enumfield(0, name="DeliveryRequestReceived")
    PAYMENT_IN_EXECUTION = o6.enumfield(1, name="PaymentInExecution")
    PAYMENT_FINISHED = o6.enumfield(2, name="PaymentFinished")
    PAYMENT_FAILED = o6.enumfield(3, name="PaymentFailed")
    PAYMENT_CANCELLED_BY_USER = o6.enumfield(4, name="PaymentCancelledByUser")
    PAYMENT_FAILED_WRONG_PRICE = o6.enumfield(5, name="PaymentFailedWrongPrice")
    DELIVERY_IN_EXECUTION = o6.enumfield(6, name="DeliveryInExecution")
    DELIVERY_AND_PAYMENT_SUCCESS = o6.enumfield(7, name="DeliveryAndPaymentSuccess")
    DELIVERY_FAIL_REFUND_IN_EXECUTION = o6.enumfield(8, name="DeliveryFailRefundInExecution")
    DELIVERY_FAIL_REFUND_SUCCESS = o6.enumfield(9, name="DeliveryFailRefundSuccess")
    DELIVERY_AND_REFUND_FAILED = o6.enumfield(10, name="DeliveryAndRefundFailed")
    DELIVERY_MIX_RESULT_REFUND_IN_EXECUTION = o6.enumfield(11, name="DeliveryMixResultRefundInExecution")
    DELIVERY_MIX_RESULT_REFUND_SUCCESS = o6.enumfield(12, name="DeliveryMixResultRefundSuccess")
    DELIVERY_MIX_RESULT_REFUND_FAILED = o6.enumfield(13, name="DeliveryMixResultRefundFailed")
    CANCELLED_BY_USER_REFUND_IN_EXCECUTION = o6.enumfield(14, name="CancelledByUserRefundInExcecution")
    CANCELLED_BY_USER_REFUND_SUCCESS = o6.enumfield(15, name="CancelledByUserRefundSuccess")
    CANCELLED_BY_USER_REFUND_FAILED = o6.enumfield(16, name="CancelledByUserRefundFailed")


@o6.datatype(nodeId="ns=unattended_retail;i=3022", browseName="TransactionProgressDataType", defaultEncodingId="ns=unattended_retail;i=5068")
class TransactionProgressDataType(ns0.datatypes.Structure):
    transactionId: o6.UInt64
    status: DeliveryAndPaymentStatusEnum
    transactionFinished: o6.Boolean
    paymentMode: o6.String
    userId: o6.String
    usedPrice: PriceAndContextDataType


@o6.datatype(nodeId="ns=unattended_retail;i=3024", browseName="BasketProgressDataType", defaultEncodingId="ns=unattended_retail;i=5043")
class BasketProgressDataType(ns0.datatypes.Structure):
    basketId: o6.UInt64
    transactionIds: list[o6.UInt64] = o6.field(arrayDimensions=[0])
    status: DeliveryAndPaymentStatusEnum
    basketFinished: o6.Boolean
    paymentMode: o6.String
    userId: o6.String
    usedPrice: PriceAndContextDataType


@o6.datatype(nodeId="ns=unattended_retail;i=3027", browseName="SelectionPriceDataType", defaultEncodingId="ns=unattended_retail;i=5046")
class SelectionPriceDataType(ns0.datatypes.Structure):
    selectionId: o6.String
    price: PriceAndContextDataType
    optionsThatMayAffectThePrice: list[o6.String] = o6.field(arrayDimensions=[0])


@o6.enumtype(nodeId="ns=unattended_retail;i=3029", browseName="PayoutStatusEnum")
class PayoutStatusEnum(ns0.datatypes.Enumeration):
    IDLE = o6.enumfield(0, name="Idle")
    ONGOING = o6.enumfield(1, name="Ongoing")
    SUCCESSFULLY_FINISHED = o6.enumfield(2, name="SuccessfullyFinished")
    FAILED = o6.enumfield(3, name="Failed")


@o6.enumtype(nodeId="ns=unattended_retail;i=3032", browseName="OperationStatusEnum")
class OperationStatusEnum(ns0.datatypes.Enumeration):
    IDLE = o6.enumfield(0, name="Idle")
    ONGOING = o6.enumfield(1, name="Ongoing")
    SUCCESSFULLY_FINISHED = o6.enumfield(2, name="SuccessfullyFinished")
    FAILED = o6.enumfield(3, name="Failed")
    FAILED_NO_COMMUNICATION = o6.enumfield(4, name="Failed_NoCommunication")
    FAILED_NOT_ENOUGH_CREDIT = o6.enumfield(5, name="Failed_NotEnoughCredit")


@o6.datatype(nodeId="ns=unattended_retail;i=3033", browseName="SelectionDataType", defaultEncodingId="ns=unattended_retail;i=5052")
class SelectionDataType(ns0.datatypes.Structure):
    machineEngineProductInstanceUri: o6.String
    selectionListVersion: o6.String
    selectionId: o6.String
    options: list[OptionSelectionDataType] = o6.field(arrayDimensions=[0])


@o6.enumtype(nodeId="ns=unattended_retail;i=3036", browseName="PaymentModeOrDeviceStatusEnum")
class PaymentModeOrDeviceStatusEnum(ns0.datatypes.Enumeration):
    AVAILABLE = o6.enumfield(0, name="Available")
    OFFLINE = o6.enumfield(1, name="Offline")
    OUT_OF_ORDER = o6.enumfield(2, name="OutOfOrder")


@o6.enumtype(nodeId="ns=unattended_retail;i=3039", browseName="PaymentServiceStatusEnum")
class PaymentServiceStatusEnum(ns0.datatypes.Enumeration):
    AVAILABLE = o6.enumfield(0, name="Available")
    OFFLINE = o6.enumfield(1, name="Offline")
    OUT_OF_ORDER = o6.enumfield(2, name="OutOfOrder")
    EXTERNALLY_STOPPED = o6.enumfield(3, name="ExternallyStopped")


del Any, TYPE_CHECKING, uuid, o6, di, ns0
