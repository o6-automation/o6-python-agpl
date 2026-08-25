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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class JobOrderCommandEnum(enum.IntFlag):
    """Describes the possible job order commands."""

    UNDEFINED_0 = 0
    STORE_1 = 1
    STORE_AND_START_2 = 2
    START_3 = 3
    UPDATE_4 = 4
    STOP_5 = 5
    CANCEL_6 = 6
    CLEAR_7 = 7

class JobOrderStateEnum(enum.IntFlag):
    """Describes the possible serial number statesjob order states."""

    UNDEFINED_0 = 0
    WAITING_1 = 1
    READY_2 = 2
    LOADED_3 = 3
    RUNNING_4 = 4
    COMPLETED_5 = 5
    ABORTED_6 = 6
    HELD_7 = 7
    SUSPENDED_8 = 8
    CLOSED_9 = 9

class OPENSCSReturnEnum(enum.IntFlag):
    UNDEFINED0 = 0
    NO_ERROR1 = 1
    INVALID_SERIAL_NUMBER_COLLECTION2 = 2
    INSUFFICIENT_SERIAL_NUMBERS3 = 3
    INVALID_SERIAL_NUMBERS_FORMAT4 = 4
    INVALID_REQUEST_TOKEN5 = 5
    INVALID_SELECTION_CRITERIA6 = 6
    UNABLE_TO_ACCEPT_SERIAL_NUMBER_EVENTS7 = 7
    UNABLE_TO_ACCEPT_LABEL_EVENTS8 = 8
    UNABLE_TO_ACCEPT_SID_EVENTS9 = 9
    UNKNOWN_AGGREGATION_SID10 = 10
    INSUFFICIENT_PRIVILEGE_TO_EXECUTE11 = 11

class OPENSCSLabelPropertyDataType(ns0.datatypes.Structure):
    @property
    def propertyID(self) -> o6.String: ...
    @propertyID.setter
    def propertyID(self, value: o6.String) -> None: ...
    @property
    def propertyDescription(self) -> o6.String: ...
    @propertyDescription.setter
    def propertyDescription(self, value: o6.String) -> None: ...
    @property
    def propertyValue(self) -> o6.String: ...
    @propertyValue.setter
    def propertyValue(self, value: o6.String) -> None: ...

class OPENSCSSIDClassPropertyDataType(ns0.datatypes.Structure):
    @property
    def propertyID(self) -> o6.String: ...
    @propertyID.setter
    def propertyID(self, value: o6.String) -> None: ...
    @property
    def propertyDescription(self) -> o6.String: ...
    @propertyDescription.setter
    def propertyDescription(self, value: o6.String) -> None: ...
    @property
    def propertyValue(self) -> o6.String: ...
    @propertyValue.setter
    def propertyValue(self, value: o6.String) -> None: ...
    @property
    def labelProperty(self) -> list[OPENSCSLabelPropertyDataType]: ...
    @labelProperty.setter
    def labelProperty(self, value: Sequence[OPENSCSLabelPropertyDataType]) -> None: ...

class OPENSCSKeyValueDataType(ns0.datatypes.Structure):
    @property
    def key(self) -> o6.String: ...
    @key.setter
    def key(self, value: o6.String) -> None: ...
    @property
    def value(self) -> o6.String: ...
    @value.setter
    def value(self, value: o6.String) -> None: ...

class OPENSCSLabelDataType(ns0.datatypes.Structure):
    """Defines a single serial number and label, which may be associated with an SID, and collection of properties in the form of OPENSCSKeyValueDataType."""

    @property
    def iD(self) -> o6.String: ...
    @iD.setter
    def iD(self, value: o6.String) -> None: ...
    @property
    def labelProperties(self) -> list[OPENSCSKeyValueDataType]: ...
    @labelProperties.setter
    def labelProperties(self, value: Sequence[OPENSCSKeyValueDataType]) -> None: ...

class OPENSCSEventStreamArgumentDataType(ns0.datatypes.Structure):
    """Defines the generateOptions argument for an EPCISStream GenerateFileForWrite method. It defines the serial number format information for object events and for aggregation events, and event context information."""

    @property
    def sNFormat(self) -> o6.String: ...
    @sNFormat.setter
    def sNFormat(self, value: o6.String) -> None: ...
    @property
    def parentSNFormat(self) -> o6.String: ...
    @parentSNFormat.setter
    def parentSNFormat(self, value: o6.String) -> None: ...
    @property
    def packedElementSNFormat(self) -> o6.String: ...
    @packedElementSNFormat.setter
    def packedElementSNFormat(self, value: o6.String) -> None: ...
    @property
    def eventContext(self) -> list[OPENSCSKeyValueDataType]: ...
    @eventContext.setter
    def eventContext(self, value: Sequence[OPENSCSKeyValueDataType]) -> None: ...

class OPENSCSSerialNumberStateEnum(enum.IntFlag):
    UNASSIGNED0 = 0
    UNALLOCATED1 = 1
    ALLOCATED2 = 2
    SN_INVALID3 = 3
    ENCODED4 = 4
    LABEL_SAMPLED5 = 5
    LABEL_SCRAPPED6 = 6
    COMMISSIONED7 = 7
    SAMPLED8 = 8
    INACTIVE9 = 9
    DESTROYED10 = 10
    RELEASED11 = 11

class OPENSCSCollectionDataType(ns0.datatypes.Structure):
    @property
    def iD(self) -> o6.String: ...
    @iD.setter
    def iD(self, value: o6.String) -> None: ...
    @property
    def description(self) -> o6.String: ...
    @description.setter
    def description(self, value: o6.String) -> None: ...
    @property
    def state(self) -> OPENSCSSerialNumberStateEnum: ...
    @state.setter
    def state(self, value: _Integer) -> None: ...
    @property
    def associatedPoolID(self) -> o6.String: ...
    @associatedPoolID.setter
    def associatedPoolID(self, value: o6.String) -> None: ...
    @property
    def serialNumbers(self) -> list[o6.String]: ...
    @serialNumbers.setter
    def serialNumbers(self, value: Sequence[o6.String]) -> None: ...

class OPENSCSLabelCollectionDataType(OPENSCSCollectionDataType):
    @property
    def iD(self) -> o6.String: ...
    @iD.setter
    def iD(self, value: o6.String) -> None: ...
    @property
    def description(self) -> o6.String: ...
    @description.setter
    def description(self, value: o6.String) -> None: ...
    @property
    def state(self) -> OPENSCSSerialNumberStateEnum: ...
    @state.setter
    def state(self, value: _Integer) -> None: ...
    @property
    def associatedPoolID(self) -> o6.String: ...
    @associatedPoolID.setter
    def associatedPoolID(self, value: o6.String) -> None: ...
    @property
    def serialNumbers(self) -> list[o6.String]: ...
    @serialNumbers.setter
    def serialNumbers(self, value: Sequence[o6.String]) -> None: ...
    @property
    def labelCollection(self) -> list[OPENSCSLabelDataType]: ...
    @labelCollection.setter
    def labelCollection(self, value: Sequence[OPENSCSLabelDataType]) -> None: ...
    @property
    def labelCollectionProperties(self) -> list[OPENSCSKeyValueDataType] | None: ...
    @labelCollectionProperties.setter
    def labelCollectionProperties(self, value: Sequence[OPENSCSKeyValueDataType] | None) -> None: ...

class OPENSCSAggregationDataType(ns0.datatypes.Structure):
    """Iidentifies a parent element and a collection of packed elements. This is used in the aggregation packing and unpacking methods."""

    @property
    def parentElement(self) -> OPENSCSLabelDataType: ...
    @parentElement.setter
    def parentElement(self, value: OPENSCSLabelDataType) -> None: ...
    @property
    def parentElementCollection(self) -> OPENSCSLabelCollectionDataType: ...
    @parentElementCollection.setter
    def parentElementCollection(self, value: OPENSCSLabelCollectionDataType) -> None: ...

class OPENSCSSNCollectionDataType:
    pass
