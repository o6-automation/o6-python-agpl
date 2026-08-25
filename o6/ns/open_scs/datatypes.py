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

"""Generated OPC UA open_scs namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=open_scs;i=3006", browseName="JobOrderCommandEnum", description="Describes the possible job order commands.")
class JobOrderCommandEnum(ns0.datatypes.Enumeration):
    UNDEFINED_0 = o6.enumfield(0, name="Undefined_0")
    STORE_1 = o6.enumfield(1, name="Store_1")
    STORE_AND_START_2 = o6.enumfield(2, name="StoreAndStart_2")
    START_3 = o6.enumfield(3, name="Start_3")
    UPDATE_4 = o6.enumfield(4, name="Update_4")
    STOP_5 = o6.enumfield(5, name="Stop_5")
    CANCEL_6 = o6.enumfield(6, name="Cancel_6")
    CLEAR_7 = o6.enumfield(7, name="Clear_7")


@o6.enumtype(nodeId="ns=open_scs;i=3009", browseName="JobOrderStateEnum", description="Describes the possible serial number statesjob order states.")
class JobOrderStateEnum(ns0.datatypes.Enumeration):
    UNDEFINED_0 = o6.enumfield(0, name="Undefined_0")
    WAITING_1 = o6.enumfield(1, name="Waiting_1")
    READY_2 = o6.enumfield(2, name="Ready_2")
    LOADED_3 = o6.enumfield(3, name="Loaded_3")
    RUNNING_4 = o6.enumfield(4, name="Running_4")
    COMPLETED_5 = o6.enumfield(5, name="Completed_5")
    ABORTED_6 = o6.enumfield(6, name="Aborted_6")
    HELD_7 = o6.enumfield(7, name="Held_7")
    SUSPENDED_8 = o6.enumfield(8, name="Suspended_8")
    CLOSED_9 = o6.enumfield(9, name="Closed_9")


@o6.enumtype(nodeId="ns=open_scs;i=15001", browseName="OPENSCSReturnEnum")
class OPENSCSReturnEnum(ns0.datatypes.Enumeration):
    UNDEFINED0 = o6.enumfield(0, name="Undefined0")
    NO_ERROR1 = o6.enumfield(1, name="NoError1")
    INVALID_SERIAL_NUMBER_COLLECTION2 = o6.enumfield(2, name="InvalidSerialNumberCollection2")
    INSUFFICIENT_SERIAL_NUMBERS3 = o6.enumfield(3, name="InsufficientSerialNumbers3")
    INVALID_SERIAL_NUMBERS_FORMAT4 = o6.enumfield(4, name="InvalidSerialNumbersFormat4")
    INVALID_REQUEST_TOKEN5 = o6.enumfield(5, name="InvalidRequestToken5")
    INVALID_SELECTION_CRITERIA6 = o6.enumfield(6, name="InvalidSelectionCriteria6")
    UNABLE_TO_ACCEPT_SERIAL_NUMBER_EVENTS7 = o6.enumfield(7, name="UnableToAcceptSerialNumberEvents7")
    UNABLE_TO_ACCEPT_LABEL_EVENTS8 = o6.enumfield(8, name="UnableToAcceptLabelEvents8")
    UNABLE_TO_ACCEPT_SID_EVENTS9 = o6.enumfield(9, name="UnableToAcceptSIDEvents9")
    UNKNOWN_AGGREGATION_SID10 = o6.enumfield(10, name="UnknownAggregationSID10")
    INSUFFICIENT_PRIVILEGE_TO_EXECUTE11 = o6.enumfield(11, name="InsufficientPrivilegeToExecute11")


@o6.datatype(nodeId="ns=open_scs;i=15007", browseName="OPENSCSLabelPropertyDataType", defaultEncodingId="ns=open_scs;i=15190")
class OPENSCSLabelPropertyDataType(ns0.datatypes.Structure):
    propertyID: o6.String
    propertyDescription: o6.String
    propertyValue: o6.String


@o6.datatype(nodeId="ns=open_scs;i=15009", browseName="OPENSCSSIDClassPropertyDataType", defaultEncodingId="ns=open_scs;i=15192")
class OPENSCSSIDClassPropertyDataType(ns0.datatypes.Structure):
    propertyID: o6.String
    propertyDescription: o6.String
    propertyValue: o6.String
    labelProperty: list[OPENSCSLabelPropertyDataType] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=open_scs;i=15010", browseName="OPENSCSKeyValueDataType", defaultEncodingId="ns=open_scs;i=15193")
class OPENSCSKeyValueDataType(ns0.datatypes.Structure):
    key: o6.String
    value: o6.String


@o6.datatype(
    nodeId="ns=open_scs;i=3003",
    browseName="OPENSCSLabelDataType",
    description="Defines a single serial number and label, which may be associated with an SID, and collection of properties in the form of OPENSCSKeyValueDataType.",
    defaultEncodingId="ns=open_scs;i=5005",
)
class OPENSCSLabelDataType(ns0.datatypes.Structure):
    iD: o6.String
    labelProperties: list[OPENSCSKeyValueDataType] = o6.field(arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=open_scs;i=3005",
    browseName="OPENSCSEventStreamArgumentDataType",
    description="Defines the generateOptions argument for an EPCISStream GenerateFileForWrite method. It defines the serial number format information for object events and for aggregation events, and event context information.",
    defaultEncodingId="ns=open_scs;i=5008",
)
class OPENSCSEventStreamArgumentDataType(ns0.datatypes.Structure):
    sNFormat: o6.String
    parentSNFormat: o6.String
    packedElementSNFormat: o6.String
    eventContext: list[OPENSCSKeyValueDataType] = o6.field(arrayDimensions=[0])


@o6.enumtype(nodeId="ns=open_scs;i=15143", browseName="OPENSCSSerialNumberStateEnum")
class OPENSCSSerialNumberStateEnum(ns0.datatypes.Enumeration):
    UNASSIGNED0 = o6.enumfield(0, name="Unassigned0")
    UNALLOCATED1 = o6.enumfield(1, name="Unallocated1")
    ALLOCATED2 = o6.enumfield(2, name="Allocated2")
    SN_INVALID3 = o6.enumfield(3, name="SNInvalid3")
    ENCODED4 = o6.enumfield(4, name="Encoded4")
    LABEL_SAMPLED5 = o6.enumfield(5, name="LabelSampled5")
    LABEL_SCRAPPED6 = o6.enumfield(6, name="LabelScrapped6")
    COMMISSIONED7 = o6.enumfield(7, name="Commissioned7")
    SAMPLED8 = o6.enumfield(8, name="Sampled8")
    INACTIVE9 = o6.enumfield(9, name="Inactive9")
    DESTROYED10 = o6.enumfield(10, name="Destroyed10")
    RELEASED11 = o6.enumfield(11, name="Released11")


@o6.datatype(nodeId="ns=open_scs;i=15005", browseName="OPENSCSCollectionDataType", defaultEncodingId="ns=open_scs;i=15188", isAbstract=True)
class OPENSCSCollectionDataType(ns0.datatypes.Structure):
    iD: o6.String
    description: o6.String
    state: OPENSCSSerialNumberStateEnum
    associatedPoolID: o6.String
    serialNumbers: list[o6.String] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=open_scs;i=15006", browseName="OPENSCSLabelCollectionDataType", defaultEncodingId="ns=open_scs;i=15189")
class OPENSCSLabelCollectionDataType(OPENSCSCollectionDataType):
    iD: o6.String
    description: o6.String
    state: OPENSCSSerialNumberStateEnum
    associatedPoolID: o6.String
    serialNumbers: list[o6.String]
    labelCollection: list[OPENSCSLabelDataType] = o6.field(arrayDimensions=[0])
    labelCollectionProperties: list[OPENSCSKeyValueDataType] | None = o6.field(arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=open_scs;i=3002",
    browseName="OPENSCSAggregationDataType",
    description="Iidentifies a parent element and a collection of packed elements. This is used in the aggregation packing and unpacking methods.",
    defaultEncodingId="ns=open_scs;i=5002",
)
class OPENSCSAggregationDataType(ns0.datatypes.Structure):
    parentElement: OPENSCSLabelDataType
    parentElementCollection: OPENSCSLabelCollectionDataType


@o6.datatype(nodeId="ns=open_scs;i=15008", browseName="OPENSCSSNCollectionDataType", defaultEncodingId="ns=open_scs;i=15191", parent="ns=open_scs;i=15005")
class OPENSCSSNCollectionDataType:
    pass


del Any, TYPE_CHECKING, uuid, o6, ns0
